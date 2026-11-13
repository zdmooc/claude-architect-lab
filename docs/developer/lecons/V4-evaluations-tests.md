# V4 — Eval, Testing, and Debugging (2,6 %)

> **Source des objectifs** : guide officiel CCDV-F v1.0, §6, Domain 4. Cours et questions **originaux**.

## 1. Objectif
Compétence officielle **Debugging and Error Handling (2,6 %)** : types d'erreurs, stratégie de reprise, analyse de traces, **isoler** un problème de couche d'intégration d'un problème de sortie du modèle.

## 2. Prérequis
V2. Architect Foundations M7·L3 (mesure).

## 3. Cours

### a) Types d'erreurs
| Couche | Exemples | Réaction |
|---|---|---|
| Transport/API | 400 requête invalide, 401/403 clé, 429 débit, 5xx/surcharge, timeout | corriger (4xx) ; reprise bornée (429/5xx) |
| Réponse | `max_tokens`, `refusal`, bloc inattendu | traiter comme incomplet/refus, pas comme succès |
| Outil | exception, accès refusé, vide, panne | erreur **structurée** (`is_error`, catégorie, réessayable) ; vide ≠ échec |
| Sortie du modèle | JSON valide mais faux, hallucination, consigne ignorée | validation métier, sources, prompt/exemples, modèle |
| Données | document illisible, index périmé | qualité des entrées, ré-indexation |

### b) Isoler la couche
1. Récupérer la **trace** : `correlation_id`, requête envoyée (prompt, version), réponse brute, `stop_reason`, outils appelés et résultats, versions (modèle, prompt, schéma).
2. **Reproduire** avec des données synthétiques.
3. Trouver la **première** étape qui diverge : la requête était-elle correcte (intégration) ? le contexte était-il bon (données/récupération) ? la sortie est-elle fausse malgré un bon contexte (modèle/prompt) ?
4. Changer **une** variable, rejouer la suite de régression, documenter.

### c) Tester
Pyramide : règles métier et outils (tests déterministes), adaptateur API avec **faux client** (`stop_reason`, blocs), évaluations de qualité sur jeu annoté par segment, tests de sécurité (injection, accès inter-clients), bout en bout. Un format correct n'est pas une preuve d'exactitude.

## 4. Exemple — DevBank
Plainte : « résumé faux pour le client C-17 ». Trace : `consulter_contrat` a renvoyé le contrat **d'un autre client** → défaut d'intégration (autorisation), pas du modèle. Correctif dans l'outil + test inter-clients.

## 5. Exercice guidé
JSON valide, TTC incohérent ; un collègue propose d'augmenter `max_tokens`.
→ Ce n'est pas une troncature (`stop_reason == "end_turn"`). C'est une erreur de sens : validation déterministe HT+TVA=TTC, relance ciblée avec le message d'erreur, puis revue humaine si la source est incohérente.

## 6. Exercice à toi
- **E1.** Classe la couche fautive : (a) 401 depuis ce matin ; (b) le modèle cite une procédure abrogée que la recherche lui a fournie ; (c) l'agent boucle 20 fois sur le même outil qui renvoie toujours « timeout ».
- **E2.** Quels champs ajoutes-tu à tes journaux pour diagnostiquer, sans exposer de données personnelles ?
- **E3.** Écris un test unitaire (pseudo-code) qui vérifie qu'une réponse `max_tokens` est rejetée par ton adaptateur.

## 7. Correction
<details><summary>Voir la correction</summary>

- **E1.** (a) **Intégration** (clé révoquée/expirée ou mal injectée). (b) **Données/récupération** (index périmé) : le modèle a suivi son contexte. (c) **Outil + boucle** : l'erreur doit être structurée et marquée non réessayable après N essais, avec budget de tours et escalade.
- **E2.** `correlation_id`, horodatage, modèle et version, version de prompt et schéma, `stop_reason`, `usage`, latence, outils appelés + statut, décision finale, escalade ; identifiants pseudonymisés, pas de contenu brut.
- **E3.**
```python
def test_max_tokens_rejete():
    faux = FauxClient(stop_reason="max_tokens", blocs=[Texte("{\"montant\": 12")])
    with pytest.raises(ClaudeResponseError):
        complete_text(faux, model="m", prompt="p")
```
(Voir `tests/test_developer_gateway.py`.)
</details>

## 8. Questions d'entraînement (originales)
**Q1.** Réponses fausses depuis la mise à jour de la base documentaire ; modèle et prompt inchangés. Première piste ?
A. Le modèle · B. La récupération / l'index · C. La température · D. Le réseau

**Q2.** (2 réponses) Erreurs à ne **pas** relancer automatiquement :
A. 400 requête invalide · B. 429 limite de débit · C. 401 authentification · D. 5xx transitoire

<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | Le changement est côté données. |
| Q2 | **A, C** | Permanentes : à corriger, pas à relancer. |
</details>

## 9. À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Classer l'erreur par couche ; 4xx permanents ≠ 429/5xx transitoires.
- Trace complète + reproduction + première divergence + une variable à la fois.
- Intégration vs données vs modèle : ne pas accuser le modèle par défaut.
- Faux client pour tester l'adaptateur ; format valide ≠ exact.
</details>

**Pratique** : [tests offline](../../../tests/), [lab Developer](../../../labs/developer_foundations/README.md).
