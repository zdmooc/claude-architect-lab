# D4 — Evaluation, Testing & Optimization (16 %)

**But** : faire des évaluations un **gate de release**, plutôt qu'un rapport flatteur de POC.

## 1. Jeux d'évaluation

Créer un dataset versionné, anonymisé/synthétique, annoté par le métier. Échantillonner cas usuels, montant absent, facture contradictoire, scans faibles, contrat résilié, multi-demande, langues, prompt injection et accès transversal. Garder un ensemble **aveugle** pour tester les changements sans surajustement.

## 2. Mesures

| Dimension | Mesure | Erreur typique |
|---|---|---|
| Extraction | exactitude par champ, documents entièrement valides | taux global cache les rares cas critiques |
| Décision | faux positifs / faux négatifs d'éligibilité | mesurer seulement la précision du texte |
| Sécurité | taux d'actions interdites exécutées | compter un refus verbal comme un blocage |
| Fiabilité | timeout et erreur par dépendance | moyennes sans P95/P99 |
| Humain | fraction et délai des escalades, corrections après revue | cacher le coût humain |
| Économie | coût complet par dossier et par segment | ne compter que tokens utiles |

## 3. Gates d'acceptation proposés (à négocier)

Pour la V1 AssurNova : **zéro paiement automatique**, **zéro exécution d'opération interdite** sur tests négatifs, couverture 100 % des cas critiques inventoriés, traçabilité de chaque proposition, revues humaines sur toutes les incohérences. Pour l'extraction, définir un seuil **par champ et segment** après baseline ; ne pas inventer une performance actuelle. Un échantillon insuffisant interdit de déclarer un contrôle fiable.

## 4. Cycle de changement

1. Geler dataset, prompt/model/config, schémas, version des outils.
2. Exécuter tests unitaires des règles, intégration des outils, evals offline puis test bout en bout.
3. Comparer modèle A/B (qualité, coût, latence, risques) ; regarder les écarts par segment.
4. Mettre en canary avec fallback et stop conditions ; analyser avant élargissement.
5. Joindre un **rapport de preuve** à chaque ADR de changement.

**Exercice** : une variante réduit le coût de 30 % mais double les erreurs sur factures OCR : expliquer pourquoi l'agrégat ne suffit pas et définir une règle de rejet.

**Livrable** : protocole mesurable, jeu d'essai, grille go/no-go, versionnement et stratégie de rollback.

Voir [plan d'évaluation](../cas-assurnova/03-evaluations.md).
