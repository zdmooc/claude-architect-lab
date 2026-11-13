# 06 — Dossier de décision pour l'Architecture Board

**AssurNova — proposition d'architecture Claude pour l'assistance bris de glace**

## Décision sollicitée

**Autoriser uniquement la préparation d'un pilote supervisé**, sous réserve des gates ci-dessous. **Ne pas autoriser la mise en production ni une opération de paiement automatisée** sur la base du présent dossier conceptuel.

## Résumé métier

10 000 dossiers/mois est une hypothèse de travail. La valeur recherchée est la réduction de ressaisie et des retours incomplets, sans transfert d'autorité financière au LLM. Les données sont synthétiques ; ni coût, ni temps de réponse, ni taux d'exactitude n'ont été mesurés.

## Option retenue et alternatives

| Option | Atout | Risque | Avis |
|---|---|---|---|
| A. Workflow + Claude ciblé | gouvernance et tests déterministes | orchestration applicative supplémentaire | **à instruire** |
| B. Agent avec outils d'écriture | souplesse | actions imprévues, sécurité accrue à démontrer | non retenu V1 |
| C. Multi-agent | parallélisme de recherches ouvertes | coordination, coût, preuves | non justifié V1 |

Voir [ADR-001 à ADR-004](02-adr.md). Aucune « solution finale » n'est décidée sans tests comparatifs.

## Conditions d'autorisation du pilote

1. Métier approuve les règles, seuil d'escalade et responsabilités.
2. IAM/RSSI démontrent interdiction d'accès inter-contrats et d'action non autorisée **dans l'API**.
3. DPO valide base légale, rétention, hébergement et circulation des données.
4. QA produit rapport d'evals segmenté et cas adversariaux, avec couverture du périmètre critique.
5. SRE valide dégradé manuel, quotas, alertes, backups/reprise et rollback.
6. FinOps valide une baseline coût complet par dossier et budget de pilote.

## Risques résiduels / arbitrages ouverts

Qualité OCR sur factures atypiques ; coût et latence en pics saisonniers ; version et disponibilité API Claude ; comportement face aux documents adversariaux ; impact des escalades sur capacité gestionnaires. Chaque risque requiert un owner, une date de revue et une preuve de clôture.

## Délibération (à compléter en séance)

- Décision : **EN ATTENTE**.
- Sponsor décisionnaire : **à nommer**.
- Architecte responsable : **à nommer**.
- Références preuve / date de test : **aucune campagne exécutée à ce stade**.
- Date de comité, réserves et signatures : **à renseigner**.

**Sortie attendue** : « GO pilote », « GO avec réserves listées » ou « NO-GO », et non une validation générale sans critères.
