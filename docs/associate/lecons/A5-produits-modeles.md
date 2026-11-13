# A5 — Product and Model Selection (12 %)

> **Source des objectifs** : guide officiel CCAO-F v1.0 (juillet 2026), §6, Domain 3. Cours, exemples et questions **originaux**. Fil rouge : [cas ConseilNova](../cas-conseilnova.md) (fictif).

## Objectifs officiels
- choisir les fonctionnalités Claude adaptées (Projects, mode recherche, chat, artifacts) ;
- différencier **Haiku, Sonnet, Opus** ;
- aligner le modèle sur le compromis coût / vitesse / qualité ;
- gérer les limites de contexte (repartir à neuf, résumer, conserver).

**Prérequis** : aucun prérequis de programmation.

**Compétence** : choisir le **bon point d'entrée** et la bonne capacité Claude pour une tâche, avant de rédiger le prompt.

## Matrice de choix

| Besoin | Surface à considérer | Question à vérifier |
|---|---|---|
| Discussion / rédaction individuelle | Claude chat | traitement autorisé des informations |
| Travail répété avec contexte d'équipe | Claude Projects / connaissances | droits, pertinence et fraîcheur des sources |
| Travail guidé sur fichiers | Claude Cowork, si disponible | accès aux fichiers, actions et validations |
| Aide au développement | Claude Code | permissions outils, tests, revue |
| Intégration dans application | API / SDK | coût, support du modèle et sécurité |

Ne pas affirmer qu'une fonctionnalité, un modèle ou un connecteur existe pour **tous les comptes**. Vérifier les surfaces disponibles, licences, politiques et capacités au moment de l'utilisation.

**Choix du modèle** : qualité requise, complexité, volume, latence, prix, longueur du contexte, formats de fichiers. Un petit modèle peut suffire au tri ; une analyse complexe peut justifier plus de capacité, **à prouver par des essais**. Les familles de modèles et tarifs évoluent.

## Exercice guidé

Une personne veut classer 200 notes mensuelles en 5 thèmes ; une autre veut arbitrer une stratégie avec 150 pages contradictoires. **Corrigé** : cadrer les exigences et budget, utiliser un lot/outil adapté au premier ; retrieval/synthèse avec vérification de sources pour le second. Le meilleur choix ne se limite pas à « toujours Opus ».

**À produire** : tableau tâche → surface → modèle candidat → risque → méthode de vérification.

## Exercice à toi
- **E1.** Quelle fonctionnalité : (a) synthèse sourcée de l'état de l'art sur un sujet ; (b) travail récurrent d'équipe sur les mêmes 20 procédures ; (c) produire un tableau de bord réutilisable ?
- **E2.** Haiku, Sonnet ou Opus : (a) trier 500 courriels ; (b) rédiger une note standard ; (c) analyser 150 pages contradictoires pour une décision stratégique.
- **E3.** Après une très longue conversation, les réponses perdent le fil. Trois options ?

## Correction
<details><summary>Voir la correction</summary>

- **E1.** (a) **Mode recherche** (sources citées, à vérifier). (b) **Project** avec instructions et connaissances. (c) **Artifact**.
- **E2.** (a) **Haiku** (rapide, économique). (b) **Sonnet** (équilibre). (c) **Opus** (raisonnement complexe), avec vérification des sources.
- **E3.** **Repartir** d'une nouvelle conversation ; **résumer** les points clés et les coller au début ; **conserver** les éléments stables dans un Project (instructions, documents).
</details>

## Questions d'entraînement (originales)
**Q1.** Modèle le plus adapté pour classer rapidement un gros volume de messages simples ?
A. Opus · B. Haiku · C. Toujours le plus gros · D. Aucun

**Q2.** (2 réponses) Gérer une conversation devenue trop longue :
A. Résumer et repartir à neuf · B. Continuer indéfiniment · C. Mettre les éléments stables dans un Project · D. Copier tout l'historique dans chaque message

<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | Rapide et économique. |
| Q2 | **A, C** | B et D aggravent. |
</details>

## À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Chat, Projects, mode recherche, artifacts : selon la tâche.
- Haiku (rapide, économique) / Sonnet (équilibre) / Opus (le plus capable).
- Choisir sur coût, vitesse, qualité ; à prouver par essais.
- Contexte : repartir, résumer, conserver dans un Project.
</details>
