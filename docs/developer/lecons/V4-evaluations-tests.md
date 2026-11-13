# V4 — Eval, Testing, and Debugging (2,6 %)

## Compétence

**Isoler la couche défaillante** et mettre en place une boucle d'évaluation : entrée → résultat attendu → sortie observée → erreur → remédiation.

### Test pyramid

| Couche | Test |
|---|---|
| Politique métier | autorisation, montant, seuil, fail-closed |
| Outil | schéma, erreur structurée, retry, résultats vides |
| API / SDK | `stop_reason`, budget, timeout, blocs de contenu |
| Qualité LLM | exactitude, hallucination, provenance par segment |
| Sécurité | injections, BOLA, refus d'outil, secrets |
| E2E | taux de correction humaine, coût et latence réelle |

**Une sortie au bon format n'est pas une preuve d'exactitude.** Utiliser tests déterministes pour les règles, évaluations avec référence annotée pour le sens, et revue humaine sur les cas à impact.

### Diagnostic

1. Capture `correlation_id`, versions des modèles/prompts/outils et segments ;
2. Reproduis le cas avec des données synthétiques ;
3. Identifie la première couche qui diverge ;
4. Corrige une seule variable, puis exécute la suite de régression ;
5. Documente le rollback si qualité/latence se dégrade.

## Exercice

Le modèle génère un JSON valide avec un TTC incohérent ; un développeur veut augmenter `max_tokens`. **Corrigé** : échec de cohérence métier → validation déterministe + retour à la source, pas problème de longueur.

**Preuve** : [test suite offline](../../../tests/), [évaluations Professional](../../professional/cas-assurnova/03-evaluations.md).
