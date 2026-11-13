# A7 — Troubleshooting and Optimization (10 %)

> **Source des objectifs** : guide officiel CCAO-F v1.0 (juillet 2026), §6, Domain 7. Cours, exemples et questions **originaux**. Fil rouge : [cas ConseilNova](../cas-conseilnova.md) (fictif).

## Objectifs officiels
- diagnostiquer les prompts peu performants et les mauvaises sorties ;
- ajuster selon les retours ;
- optimiser les flux de travail.

**Prérequis** : aucun prérequis de programmation.

**Compétence** : localiser la cause d'une réponse insuffisante et corriger le **bon levier**.

## Tableau de diagnostic

| Symptôme | Causes à vérifier d'abord | Mesure / correction |
|---|---|---|
| Réponse trop générique | objectif, audience ou exemples absents | clarifier le prompt |
| Réponse factuellement fausse | source absente, obsolète ou contradictoire | vérifier source, contexte et citations |
| Format ignoré | instructions multiples ou format flou | gabarit de sortie et exemple |
| Réponse interrompue | longueur ou limite d'outil | fractionner, ajuster format/budget |
| Informations inappropriées | droits ou partage trop larges | suspendre l'usage, revoir ACL/politique |
| Temps/coût excessif | contexte trop long, répétition, modèle non adapté | mesurer avant d'optimiser |

**Cycle** : reproduire sur entrée sauvegardée (synthétique), isoler une cause, modifier **une variable à la fois**, comparer avec les mêmes critères, documenter le résultat et vérifier qu'une autre catégorie de cas ne régresse pas.

## Exercice guidé

Claude se trompe sur une remise commerciale pourtant expliquée dans un document. **Corrigé** : vérifier que le document fourni est celui qui fait autorité, que la bonne date est retenue et que le montant est calculé par une source de vérité. Réécrire le prompt seul n'est pas le bon premier geste si la grille tarifaire est obsolète.

**À produire** : fiche incident « entrée, attendu, observé, hypothèse, expérience, résultat, décision ».

## Exercice à toi
- **E1.** Les réponses sont trop longues pour les clients. Propose deux corrections et comment vérifier.
- **E2.** Remplis une fiche incident (entrée, attendu, observé, hypothèse, expérience, résultat, décision) pour : « Claude donne un délai de retour de 14 jours au lieu de 30 ».
- **E3.** Le flux prend 20 minutes par dossier, dont 12 de relecture. Où optimiser en premier ?

## Correction
<details><summary>Voir la correction</summary>

- **E1.** Contrainte explicite (« 5 phrases maximum ») + exemple de réponse courte ; vérifier sur 10 cas sauvegardés avec le même critère.
- **E2.** Entrée : question retour produit. Attendu : 30 jours. Observé : 14 jours. Hypothèse : ancienne procédure dans le Project. Expérience : retirer l'ancien document, rejouer 3 cas. Résultat : 30 jours. Décision : purge + revue mensuelle.
- **E3.** La **relecture** (12 min) : améliorer la qualité et la traçabilité des sorties (sources citées, format standard) pour la raccourcir, plutôt que gagner quelques secondes de génération.
</details>

## Questions d'entraînement (originales)
**Q1.** Méthode correcte pour améliorer un prompt :
A. Changer plusieurs choses à la fois · B. Une variable à la fois, sur les mêmes cas, avec les mêmes critères · C. Tester sur un seul exemple · D. Demander à Claude s'il est content

**Q2.** (2 réponses) Réponse factuellement fausse alors que le prompt est clair. À vérifier d'abord :
A. La source est-elle à jour ? · B. La couleur de l'interface · C. Le bon document a-t-il été fourni ? · D. La longueur du prompt

<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | Comparaison fiable. |
| Q2 | **A, C** | Cause côté source. |
</details>

## À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Symptôme → cause probable → correction du **bon levier**.
- Reproduire, une variable à la fois, mêmes critères, pas de régression ailleurs.
- Optimiser le flux là où le temps est réellement perdu.
</details>
