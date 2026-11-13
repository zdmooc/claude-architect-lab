# D6 — Stakeholder Communication & Lifecycle Management (14 %)

**But** : obtenir une décision d'investissement explicite et un passage en exploitation qui ne dépend pas de l'architecte initial.

## 1. Discovery et gouvernance

Rencontrer sponsor, gestionnaires, sécurité, DPO, exploitation, architecture d'entreprise et responsables des systèmes sources. Séparer « désirable », « permis », « faisable » et « mesurable ». Identifier les désaccords plutôt que choisir silencieusement.

Formaliser : problème, KPI métier, parcours inclus/exclus, critères de succès et d'arrêt, hypothèses à confirmer, obligations, dépendances, budget et calendrier de décision. Maintenir un registre de risques et décisions ADR (qui a validé, à quelle date, sous quelles conditions).

## 2. Argumentaire pour comité

Une fiche de décision doit comparer 2 à 3 options en termes de coût complet, délai, qualité, risques, réversibilité, charge des gestionnaires et impact client. Les scores estimatifs ne sont **pas** des faits ; afficher la source et l'incertitude. Répondre à la question du comité : « Quelle décision devons-nous prendre aujourd'hui et quelle preuve manque-t-il pour la suivante ? »

## 3. Phases de cycle de vie

Discovery → POC instrumenté → pilote restreint → homologation sécurité/DPO → canary → production supervisée → suivi qualité → décommissionnement. Chaque phase possède des **critères de sortie**, son décideur et un plan de retour arrière.

RACI minimal : sponsor responsable des bénéfices, métier propriétaire des règles, sécurité des contrôles, DPO du traitement, plateforme de la résilience, product owner des priorités, run manager de l'exploitation. Documenter les SLA/SLO réellement négociés, pas des valeurs choisies arbitrairement.

## 4. Exercice

Un sponsor veut « 90 % d'automatisation dès lundi ». Rédiger la réponse : démarrer par une baseline fiable, distinguer automatisation documentaire et paiement, proposer un pilote limité, définir un gate, préciser un risque et une date de revue. Ne pas opposer un « non » purement technique.

**Livrable** : note pour comité, registre des décisions et risques, RACI, critères de mise en production, plan d'adoption.

Voir [dossier de décision](../cas-assurnova/06-dossier-decision.md).
