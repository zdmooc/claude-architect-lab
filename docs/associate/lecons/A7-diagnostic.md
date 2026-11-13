# A7 — Troubleshooting and Optimization (10 %)

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

## Exercice

Claude se trompe sur une remise commerciale pourtant expliquée dans un document. **Corrigé** : vérifier que le document fourni est celui qui fait autorité, que la bonne date est retenue et que le montant est calculé par une source de vérité. Réécrire le prompt seul n'est pas le bon premier geste si la grille tarifaire est obsolète.

**À produire** : fiche incident « entrée, attendu, observé, hypothèse, expérience, résultat, décision ».
