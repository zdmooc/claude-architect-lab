# M7 · Leçon 3 — Provenance, contradictions et mesure de la qualité (D5)

> **Statut** : `labs/m7/mesure.py` **exécuté** (observé : 6/8 global, mais 2/2 sur les factures et 1/2 sur les déclarations ; une contradiction détectée et conservée). Données et sources **fictives**.

## 1. Objectif et utilité
Rendre les résultats **vérifiables** (d'où vient chaque affirmation ?) et **mesurer** la qualité là où elle compte, au lieu d'une moyenne trompeuse.
Dossier D5 : calibrer les seuils sur données annotées, mesurer par type de document et par champ, conserver le lien affirmation–source, y compris dates et contradictions.

## 2. Prérequis
M2·L2 (extraction), M6·L2 (multi-agent).

## 3. Cours
### a) Provenance
Chaque affirmation garde : **extrait**, **source**, **date de la source**. Sans cela, impossible de vérifier ou de corriger.

### b) Contradictions
Deux sources disent 2028 et 2030 → on **conserve les deux**, attribuées et datées. Choisir en silence fait perdre l'information ; la décision revient à l'humain (ou à une règle explicite : source officielle la plus récente…).

### c) Mesurer par segment
Une exactitude globale de 75 % peut cacher : 100 % sur les factures, 50 % sur les déclarations. Mesurer **par type de document et par champ** révèle où mettre la revue humaine.
👉 Comme un SLO global qui masque un endpoint en échec.

### d) Calibrer les seuils de revue
Pour décider « on revoit tout ce qui a une confiance < X », on **mesure** sur un **jeu annoté** quelle valeur de X donne le taux d'erreur acceptable. Sans jeu annoté, le seuil est une supposition.

## 4. Exemple commenté : `mesure.py`
- `exactitude()` : compteurs `(type, champ)` → `declaration/date : 1/2`, `declaration/montant_ttc : 1/2`.
- `contradictions()` : regroupe par sujet, signale les valeurs divergentes **sans en supprimer**.

## 5. Exercice guidé
Décision sur la base du résultat observé : les factures peuvent passer en traitement automatique avec revue par échantillon ; les déclarations passent en **revue humaine systématique** sur date et montant, le temps d'améliorer prompt/exemples (M2) et de re-mesurer.

## 6. Exercice à toi
- **E1.** Dans `mesure.py`, ajoute un 3ᵉ type « avis d'échéance » avec deux documents, dont un faux. Quel est le nouveau résultat global, et que montre-t-il de plus que lui ?
- **E2.** Un rapport de recherche affirme « la migration coûtera 300 k€ » sans source. Que manque-t-il, selon cette leçon ?
- **E3.** Pourquoi une valeur de confiance déclarée par le modèle ne suffit-elle pas à fixer un seuil de revue ?

## 7. Correction
*Après ta réponse.*
## 8. À retenir pour l'examen
*Avec la correction.*
