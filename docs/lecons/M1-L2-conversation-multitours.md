# M1 · Leçon 2 — Conversation multi-tours : l'application porte l'état

> **Statut du code** : `labs/m1/conversation.py` proposé, compilé, **non exécuté** contre l'API par le formateur.

## 1. Objectif et utilité
Construire une vraie conversation au-dessus d'une API **stateless**, et mesurer ce que ça coûte.
C'est la mise en pratique de M0·L1, et la base de la boucle agentique (D1) où l'on renverra aussi les **résultats d'outils** dans l'historique.

## 2. Prérequis
M1·L1 (anatomie requête/réponse, `stop_reason`, `usage`).

## 3. Cours

### a) Le motif de base
```
historique = []
à chaque tour :
    historique += message utilisateur
    réponse = appel API(system, historique)
    historique += réponse COMPLÈTE de l'assistant
```
Trois règles :
1. **L'ordre** : `user`, `assistant`, `user`, `assistant`…
2. **La réponse complète** : on ajoute `response.content` (tous les blocs), pas seulement le texte extrait. Les blocs `thinking` et `tool_use` doivent revenir intacts au tour suivant, sinon on casse la continuité (et en M3 la boucle d'outils).
3. **Le `system` reste à part** : il n'est pas dans `messages`, on le renvoie à chaque appel.

### b) Le coût cumulatif
À chaque tour, **tout** l'historique est renvoyé. `input_tokens` grossit donc tour après tour.
Une conversation de 30 tours ne coûte pas 30 × un tour : beaucoup plus.
Leviers (approfondis en M7 et M2) :
- garder les **faits critiques** dans un bloc structuré plutôt que de compter sur des vieux messages ;
- **résumer** les anciens échanges ;
- **réduire** les gros contenus (n'envoyer que les extraits utiles d'un document) ;
- le **prompt caching** existe pour réduire le coût des préfixes répétés, mais ses détails sont **hors programme** Foundations (dossier §3.8).

### c) Traiter les cas d'arrêt
- `end_turn` → normal.
- `max_tokens` → réponse tronquée : ne pas l'enregistrer comme complète.
- `refusal` → ne pas ajouter ce tour comme s'il avait réussi.

## 4. Exemple commenté : `labs/m1/conversation.py`
- `historique = []` : l'état vit dans **ton** processus. Si le script redémarre, la conversation est perdue → en production on le persiste (base, cache…).
- `messages=historique` : tout est renvoyé à chaque appel.
- `historique.append({"role": "assistant", "content": response.content})` : la réponse complète, pas juste le texte.
- La ligne `[stop_reason=… | in=… | out=…]` te permet de **voir** `input_tokens` grimper.

## 5. Exercice guidé
Lis ce code d'un collègue :
```python
reponse = client.messages.create(model=MODEL, max_tokens=1024,
                                 messages=[{"role": "user", "content": question}])
```
appelé à chaque tour d'un chatbot.
1. Que contient `messages` ? Uniquement la dernière question.
2. Conséquence ? Aucun souvenir du tour précédent : « Et pour l'autre contrat ? » n'a aucun sens pour Claude.
3. Correction ? Maintenir `historique`, y ajouter question **et** réponse, et l'envoyer entier.

## 6. Exercice à toi
- **E1.** (avec clé) Lance `conversation.py`, fais 5 échanges sur un même sinistre. Relève `input_tokens` à chaque tour. Comment évolue-t-il, et pourquoi ?
- **E2.** (avec clé) Commente la ligne qui ajoute la réponse de l'assistant à l'historique. Pose une question qui fait référence à la réponse précédente. Que se passe-t-il ?
- **E3.** (papier) Propose une modification du script pour qu'il ne garde que les 10 derniers messages. Quel risque cela introduit-il, et comment le compenser ?

## 7. Correction
<details><summary>Voir la correction</summary>

- **E1.** `input_tokens` **augmente à chaque tour** : tout l'historique est renvoyé.
- **E2.** Claude ne « se souvient » plus de sa réponse précédente : il voit deux questions utilisateur d'affilée sans sa réponse, la référence n'a plus de sens.
- **E3.** `historique = historique[-10:]` (en gardant un nombre pair et en commençant par un message `user`). Risque : perdre un fait donné au début (contrat, montant). Compensation : un **bloc de faits** permanent ou un **résumé guidé** des messages retirés (M7·L1).

</details>

## 8. À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- L'application ajoute question **et réponse complète** (`response.content`) à chaque tour.
- Le coût **croît** avec la longueur de la conversation.
- Ne pas enregistrer comme complet un tour `max_tokens` ou `refusal`.

</details>
