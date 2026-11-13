# M3 · Leçon 1 — La boucle agentique : `tool_use` → résultat → `end_turn` (D1)

> **Statut** : `labs/m3/boucle_manuelle.py` suit la boucle manuelle documentée pour le SDK Python (13/11/2026), compilé, **non exécuté** contre l'API.

## 1. Objectif et utilité
Comprendre — et savoir coder — le cycle **requête → appel d'outil → exécution → résultat → nouvelle requête**.
Premier point D1 du dossier (27 % de l'examen) : distinguer `stop_reason: tool_use` et `end_turn`, et conserver les résultats d'outils dans l'historique.

## 2. Prérequis
M1·L2 (historique porté par l'application), M2·L2 (schémas JSON).

## 3. Cours

### a) Claude n'exécute rien
Quand tu déclares des outils, Claude peut répondre : *« appelle `consulter_contrat` avec `{numero: "AUTO-4471"}` »*.
C'est **ton code** qui exécute, puis qui renvoie le résultat. Claude ne touche jamais directement ton SI.
👉 Analogie : Claude est un orchestrateur qui émet des ordres ; ton code est le bus/ESB qui les exécute et rapporte.

### b) Le cycle
```
1. Appel API (system, tools, messages)
2. Réponse :
   - stop_reason == "tool_use" → la réponse contient un ou plusieurs blocs tool_use
       a. ajouter la réponse COMPLÈTE de l'assistant à messages
       b. exécuter chaque outil
       c. ajouter UN message user contenant TOUS les tool_result (avec tool_use_id)
       d. retour en 1
   - stop_reason == "end_turn" → réponse finale, on sort
   - autre (max_tokens, refusal…) → cas à traiter explicitement
```

### c) Trois erreurs classiques
1. **Oublier d'ajouter la réponse de l'assistant** avant les résultats → l'API ne peut pas relier `tool_result` à son `tool_use` (`tool_use_id`).
2. **Arrêter la boucle sur « il y a du texte »** : Claude peut écrire une phrase *et* demander un outil dans la même réponse. Seul `stop_reason` fait foi.
3. **Utiliser le compteur d'itérations comme condition d'arrêt** : `MAX_TOURS` est un **garde-fou** contre les boucles infinies, pas la fin normale. Le dossier le cite comme piège d'examen.

### d) Plusieurs appels dans une réponse
Claude peut demander **plusieurs outils d'un coup** (appels parallèles). On les exécute tous et on renvoie **tous les résultats dans un seul message user**. Les éclater en plusieurs messages dégrade le comportement.

## 4. Exemple commenté : `boucle_manuelle.py`
- `for tour in range(MAX_TOURS)` : garde-fou ; si on l'atteint → message d'escalade, pas une réponse normale.
- `if response.stop_reason == "end_turn"` : **la** condition de fin.
- `messages.append({"role": "assistant", "content": response.content})` : réponse complète.
- `"tool_use_id": bloc.id` : la corrélation entre demande et résultat.
- `"is_error": r["is_error"]` : le modèle sait que l'outil a échoué (L2).

## 5. Exercice guidé — dérouler un échange
Question : *« Quels sinistres sur le contrat de Mme Durand ? »*
1. Tour 1 → `tool_use` : `rechercher_client(nom="Durand")` → résultat : client C-1001.
2. Tour 2 → Claude n'a **pas d'outil** pour passer d'un client à ses contrats ! Il peut : demander le numéro de contrat à l'utilisateur, ou (mauvais) deviner. Avec le prompt système « n'invente pas », il doit demander.
3. Leçon d'architecte : **le jeu d'outils définit ce que l'agent peut faire**. Un trou fonctionnel produit soit une question, soit une hallucination. → E3.

## 6. Exercice à toi
- **E1.** Une réponse contient un bloc `text` (« Je vais consulter le contrat… ») et un bloc `tool_use`. Le code d'un collègue affiche le texte et s'arrête. Quel `stop_reason` aurait-il dû tester, et quelle valeur avait-il ici ?
- **E2.** Pourquoi `MAX_TOURS = 10` ne doit-il pas être la condition d'arrêt normale ? Que doit faire le code quand il est atteint ?
- **E3.** Propose un 4ᵉ outil qui comble le trou de l'exercice guidé : nom, description (2 phrases), schéma d'entrée.

## 7. Correction
<details><summary>Voir la correction</summary>

- **E1.** Il fallait tester `stop_reason` ; ici il valait **`tool_use`**. Le texte n'est qu'un commentaire intermédiaire : le code devait exécuter l'outil, renvoyer le `tool_result` et relancer.
- **E2.** L'arrêt normal, c'est `end_turn`. `MAX_TOURS` est un **garde-fou** contre une boucle infinie (outil qui échoue en boucle, modèle qui tourne en rond). L'atteindre est une **anomalie** : journaliser, ne pas présenter la dernière réponse comme finale, escalader vers un humain.
- **E3.** `lister_contrats_client` — « Renvoie la liste des contrats (numéro, produit, statut) d'un client identifié par son identifiant interne. À utiliser après `rechercher_client` ; ne renvoie ni sinistres ni montants. » Schéma : `{"type":"object","properties":{"client_id":{"type":"string","pattern":"^C-\\d{4}$"}},"required":["client_id"]}`.

</details>

## 8. À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- La boucle tourne tant que `stop_reason == "tool_use"` ; on s'arrête sur `end_turn`.
- Renvoyer la réponse **complète** de l'assistant, puis **tous** les `tool_result` dans un seul message user.
- Le jeu d'outils définit le périmètre : un trou → une question ou une hallucination.

</details>
