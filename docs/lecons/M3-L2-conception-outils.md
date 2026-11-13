# M3 · Leçon 2 — Concevoir de bons outils : descriptions, erreurs, `tool_choice` (D2)

> **Statut** : `labs/m3/outils_contrats.py` et `test_outils.py` **exécutés localement** (4 tests OK, sans API).
> `tool_choice` : notion décrite dans le guide (dossier §3.3) **et** contrainte actuelle relevée dans la documentation API du 13/11/2026 — les deux sont présentées.

## 1. Objectif et utilité
Faire en sorte que le modèle **choisisse le bon outil** et **réagisse correctement à un échec**.
D2 (18 %) : descriptions qui distinguent des outils proches, erreurs structurées, absence de résultat ≠ échec, outils limités au rôle, `tool_choice`.

## 2. Prérequis
M3·L1.

## 3. Cours

### a) La description est le premier levier
Le modèle choisit un outil **en lisant sa description**. Une bonne description dit :
- **ce que fait** l'outil et **quand** l'utiliser ;
- **ce qu'il ne fait pas**, en renvoyant vers l'outil voisin ;
- le **format** des entrées (avec exemple) et de la sortie.
Le dossier relève un raisonnement récurrent dans les exemples du guide : **améliorer les descriptions avant d'ajouter une couche de routage**.

### b) Erreurs structurées
Un outil qui échoue renvoie un `tool_result` avec `is_error: true` et un contenu **exploitable** :
```json
{"categorie": "introuvable", "message": "Aucun contrat AUTO-9999. Vérifie le numéro.", "reessayable": false}
```
Catégories utiles (dossier §3.3) :
| Catégorie | Que faire |
|---|---|
| **transitoire** (timeout) | réessayer (souvent côté code, avec backoff) |
| **validation** (entrée invalide) | corriger l'entrée |
| **permission** | ne pas réessayer ; escalader |
| **règle métier** (ex. contrat résilié) | expliquer à l'utilisateur |

### c) Vide ≠ échec
`rechercher_client("Inconnu")` → **succès** avec une liste vide.
`consulter_contrat` sur un référentiel en panne → **erreur transitoire**.
Confondre les deux mène à dire « ce client n'existe pas » alors que la base était simplement indisponible. Piège cité dans le dossier.

### d) Moins d'outils, mieux ciblés
Chaque agent ne reçoit que **les outils de son rôle** (principe du moindre privilège). Moins d'outils = moins de confusion **et** moins de risques. Un agent de consultation n'a pas d'outil `rembourser`.

### e) `tool_choice`
Valeurs décrites dans le guide (dossier) : `auto` (le modèle décide), `any` (doit appeler un outil), choix **forcé** d'un outil précis ; `none` interdit les outils.
⚠️ **Fait relevé dans la doc actuelle** : les modèles récents comme `claude-opus-5-5` **refusent** `any` et le choix forcé (erreur 400). On utilise `auto` + une consigne explicite (« utilise l'outil X ») + `strict: true` sur l'outil, et on **vérifie** qu'un appel a bien eu lieu.
→ Pour l'examen : connais les trois modes et leur intention ; en pratique, vérifie le modèle utilisé.

## 4. Exemple commenté : `outils_contrats.py`
- `rechercher_client` : « Ne renvoie PAS de contrats : pour un contrat, utilise consulter_contrat » → frontière explicite.
- `_erreur(categorie, message, reessayable)` : erreur structurée.
- `return _ok({"clients": trouves, "nombre": len(trouves)})` : la liste vide est un succès.
- `TAUX_PANNE` : pour **provoquer** une panne et voir la réaction de l'agent.

## 5. Exercice guidé
Deux outils existants : `chercher_document(query)` — « Cherche des documents » et `chercher_procedure(query)` — « Cherche des procédures ». Le modèle se trompe une fois sur deux.
Réécriture :
- `chercher_procedure` : « Cherche dans le **référentiel des procédures internes validées** (sinistres, souscription). À utiliser pour *comment faire*. Ne contient pas les documents clients. »
- `chercher_document` : « Cherche dans la **GED des pièces clients** (factures, constats, courriers) d'un dossier donné. À utiliser pour *ce qu'un client a envoyé*. Requiert un numéro de dossier. »
Les deux descriptions disent **quand** et **quand pas**.

## 6. Exercice à toi
- **E1.** Lance `python test_outils.py` (sans clé). Puis modifie `rechercher_client` pour qu'il renvoie une **erreur** quand la liste est vide. Quel test casse, et pourquoi ce changement serait-il une mauvaise idée ?
- **E2.** Écris l'erreur structurée que doit renvoyer `consulter_contrat` si l'utilisateur n'a pas le **droit** de consulter ce contrat. Le modèle doit-il réessayer ?
- **E3.** Un agent « relation client » a les outils `consulter_contrat`, `lister_sinistres`, `modifier_iban`, `rembourser`. Lesquels retirerais-tu et pourquoi ?

## 7. Correction
*Ajoutée après ta réponse.*

## 8. À retenir pour l'examen
*Ajouté avec la correction.*
