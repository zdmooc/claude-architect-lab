# Étude de cas AssurNova — architecture Claude en entreprise

**Client fictif** : AssurNova, assureur IARD. **Aucun contenu client réel.** Ce dossier constitue un exercice d'architecture complet, pas la preuve qu'un système a été déployé.

## Périmètre

Assistance aux sinistres auto **bris de glace** : réception, vérification du contrat, extraction des factures, proposition d'indemnisation et escalade. L'IA ne déclenche **jamais le paiement** ; les droits d'accès et règles financières sont contrôlés par des services déterministes. Seuil pédagogique : **800 €**, montant strictement supérieur → gestionnaire.

## Pièces du dossier

| Pièce | Destinataire | Objectif |
|---|---|---|
| [00 — Cadrage](00-cadrage.md) | métier / sponsor | cadrer valeur, périmètre, non-objectifs et exigences |
| [01 — HLD](01-hld.md) | architecture / intégration | blocs, flux, sécurité, SLO et dépendances |
| [02 — ADR](02-adr.md) | Architecture Board | arbitrer workflow, MCP, modèle, stockage |
| [03 — Évaluations](03-evaluations.md) | QA / métier / MLOps | mesurer et décider go/no-go |
| [04 — Contrôles et RACI](04-controles-raci.md) | RSSI / DPO / métier | contrôles, responsables, preuves |
| [05 — Runbook](05-runbook.md) | SRE / exploitation | diagnostiquer, contenir, restaurer |
| [06 — Décision](06-dossier-decision.md) | comité d'investissement | arbitrage et conditions d'entrée en pilote |

## Épreuve intégratrice

Sans consulter les ADR : proposer une autre architecture (agent autonome), calculer ses nouveaux points de défaillance, établir un test comparatif de coût/qualité, rédiger une objection sécurité, puis soutenir oralement l'option retenue en 5 minutes.

**Statut** : dossier conceptuel rédigé. À faire : tests réels, revue contradictoire, coûts mesurés, homologation sécurité et métier.
