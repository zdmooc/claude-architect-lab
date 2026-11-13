# M3 · Leçon 3 — Le Tool Runner : déléguer la boucle sans perdre le contrôle

> **Statut** : `labs/m3/tool_runner.py` suit la documentation du SDK Python (`@beta_tool`, `client.beta.messages.tool_runner`) ; présence de `tool_runner` vérifiée dans `anthropic` 2.8.0 ; compilé, **non exécuté**. Le Tool Runner est en **bêta**.

## 1. Objectif et utilité
Savoir quand écrire la boucle soi-même et quand la confier au SDK. C'est aussi la transition vers M6 (Agent SDK), qu'il ne faut pas confondre avec le Tool Runner (M0·L2).

## 2. Prérequis
M3·L1, M3·L2.

## 3. Cours
### a) Ce que fait le Tool Runner
- génère le schéma d'outil depuis la **signature et la docstring** de ta fonction (`@beta_tool`) ;
- appelle l'API, exécute tes fonctions, renvoie les résultats, **boucle** jusqu'à la fin ;
- te laisse **itérer** sur chaque réponse (`for message in runner`).

### b) Boucle manuelle ou Tool Runner ?
| Besoin | Choix |
|---|---|
| Cas standard, tes propres outils | **Tool Runner** (moins de code) |
| Pas de dépendance bêta, transport spécifique, contrôle total de chaque requête | **Boucle manuelle** |
| Outils fichiers/bash intégrés, sous-agents, hooks | **Claude Agent SDK** (M6) — autre produit |

Une **validation humaine** ne nécessite pas forcément la boucle manuelle : on peut la placer **dans la fonction outil** (elle refuse et renvoie « en attente de validation »).

### c) La docstring est la description
Avec `@beta_tool`, la docstring **est** la description vue par le modèle : tout ce qu'on a dit en L2 s'applique.

## 4. Exemple commenté : `tool_runner.py`
- Les fonctions **réutilisent** `executer()` de `outils_contrats.py` : la logique métier reste testable sans API.
- `for message in runner` : on voit chaque étape, utile pour journaliser.

## 5. Exercice guidé
Une équipe veut qu'aucun remboursement > 1 000 € ne parte sans validation. Où mettre le contrôle ?
- ❌ Dans le prompt seulement → le modèle peut l'ignorer.
- ✅ Dans la fonction `rembourser` : `if montant > 1000: return "REFUSÉ : validation humaine requise (ticket créé)"`.
Le contrôle est **déterministe**, côté code, quel que soit le mode (manuel ou runner).

## 6. Exercice à toi
- **E1.** Cite deux raisons de préférer la boucle manuelle au Tool Runner.
- **E2.** Un collègue dit : « Le Tool Runner, c'est l'Agent SDK. » Corrige-le en deux phrases.
- **E3.** (avec clé, facultatif) Lance `tool_runner.py`. Combien d'itérations observes-tu ? Les deux outils ont-ils été appelés dans la même réponse ?

## 7. Correction
*Ajoutée après ta réponse.*

## 8. À retenir pour l'examen
*Ajouté avec la correction.*
