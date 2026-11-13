# 04 — Matrice de contrôles, risques et RACI

## Contrôles obligatoires — concept à faire auditer

| ID | Menace / exigence | Contrôle exécuté hors modèle | Owner | Preuve attendue |
|---|---|---|---|---|
| C-01 | Accès au contrat d'autrui | OIDC + contrôle titulaire/mandat côté API à chaque appel | IAM | test BOLA/IDOR négatif |
| C-02 | Identité non vérifiée | refus de création de proposition, **fail closed** | métier + backend | test sans identité |
| C-03 | Indemnisation >800 € | blocage déterministe et routage humain | métier | tests 800,00 / 800,01 |
| C-04 | Paiement par l'agent | aucun outil ni scope de paiement exposé | RSSI | revue permissions |
| C-05 | Prompt injection facture | traiter les pièces comme données, validation de sortie, allowlist outils | AI engineering | suite adversariale |
| C-06 | Montant erroné | validation HT+TVA=TTC, provenance obligatoire | QA métier | test facture incohérente |
| C-07 | Doublon après retry | clé d'idempotence + stockage état durable | intégration | test de rejeu |
| C-08 | Données personnelles dans traces | minimisation, rétention, contrôle accès logs | DPO/SRE | inspection traces |
| C-09 | Panne Claude ou MCP | circuit breaker, timeout, file de revue humaine | SRE | exercice dégradé |
| C-10 | Changement modèle dégrade qualité | évaluation segmentée + canary + rollback | MLOps/QA | rapport de release |

**Principe** : les prompts et hooks peuvent **ajouter** un contrôle, jamais remplacer une vérification d'autorisation dans le service métier ; la sortie du modèle est une **proposition non fiable jusqu'à validation**.

## RACI simplifié

R = réalise, A = approuve/est comptable, C = consulté, I = informé.

| Activité | Sponsor | Métier | Archi | RSSI | DPO | SRE |
|---|---|---|---|---|---|---|
| Règles d'indemnisation | I | A/R | C | C | I | I |
| HLD / ADR | I | C | A/R | C | C | C |
| Homologation sécurité | I | C | R | A | C | C |
| Traitement données personnelles | I | C | C | C | A/R | I |
| Critères qualité fonctionnelle | I | A/R | C | C | C | C |
| Mise en production technique | I | C | C | C | C | A/R |
| Acceptation risque résiduel métier | A | R | C | C | C | I |

## Décision humaine

Toute ambiguïté de montant, contrat inactif, demande de contestation, soupçon de fraude ou montant >800 € produit un ticket de reprise. Le ticket porte : dossier_id, provenance, étapes déjà effectuées, incertitude et cause de transfert ; **jamais** une recommandation opaque présentée comme décision définitive.

## Points ouverts pour une entreprise réelle

Base légale RGPD et DPA, zone de traitement, durée de conservation, DPIA si nécessaire, localisation des journaux, sous-traitants, gestion des demandes d'effacement, séparation entre contrôle antifraude et service aux assurés. Le dossier fictif ne vaut pas avis juridique.
