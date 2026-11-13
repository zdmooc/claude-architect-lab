# 01 — High Level Design (HLD) — AssurNova

**Statut : proposition à valider**, sans environnement de production démontré.

## Vue d'ensemble

~~~mermaid
flowchart LR
 A[Assuré / Gestionnaire] --> B[API Gateway + OIDC]
 B --> C[Orchestrateur dossier]
 C --> D[Service autorisation]
 C --> E[Outils contrat / sinistre]
 C --> F[Préparation documents]
 F --> G[Claude API]
 G --> H[Validation schéma + provenance]
 H --> I[Moteur de politiques]
 D --> E
 E --> I
 I --> J[Proposition versionnée]
 I --> K[File revue humaine]
 J --> K
 K --> L[Gestionnaire habilité]
 C --> M[Audit + observabilité]
 I --> M
 K --> M
~~~

L'outil de **paiement n'est accessible ni à Claude ni à l'orchestrateur**. Une éventuelle chaîne de règlement distincte est hors périmètre et exige approbation / contrôles de sa propre responsabilité.

## Parcours nominal

1. Le portail authentifie le demandeur ; l'API transmet un subject_id et un dossier_id non sensibles.
2. L'autorisation vérifie que le demandeur peut consulter ce dossier et les pièces liées.
3. L'orchestrateur lit contrat, garanties et procédure **dans leur version applicable à la date du sinistre**.
4. Le préparateur extrait du PDF des textes contrôlés ; les pièces sont considérées non fiables (risque de prompt injection).
5. Claude propose une extraction JSON et un résumé ; validation du schéma, cohérence des montants et citations côté application.
6. Le moteur de politiques décide **éligibilité à proposer / escalade**, de façon déterministe ; montant > 800 €, anomalie ou demande humaine → revue.
7. Une proposition est enregistrée avec une **clé d'idempotence**, sa version, ses preuves et statut « à valider » ; décision finale par gestionnaire habilité.

## Contrats de données minimaux

~~~json
{
  "dossier_id": "SYN-SIN-0001",
  "contrat_id": "SYN-AUTO-4471",
  "facture": {
    "numero": "F-001",
    "montant_ht": 625.0,
    "montant_tva": 125.0,
    "montant_ttc": 750.0,
    "devise": "EUR",
    "ambiguites": []
  },
  "source_refs": [{"document_id": "SYN-DOC-01", "version": "v1", "page": 1}],
  "statut": "PROPOSITION_A_VALIDER"
}
~~~

**Erreurs typées** : `not_found` (non réessayable), `forbidden` (non réessayable + audit), `unavailable` (réessayable borné), `ambiguous_data` (revue humaine). Ne pas confondre liste vide et panne.

## NFR et budget initial à **mesurer**

| Critère | Cible de conception (non mesurée) | Vérification |
|---|---|---|
| Disponibilité portail | 99,9 % mensuel, à négocier | test de dégradé et mesure SLI |
| Réponse d'assistance | P95 < 8 s sur segment simple, à confirmer | tests sous charge représentative |
| Intégrité métier | 0 proposition non autorisée dans jeu de tests négatifs | tests auth + seuil + rejeu |
| Récupération | traitement manuel lorsque Claude indisponible | exercice de bascule |
| Coûts | budget par dossier fixé après POC | dashboard tokens+outils+revu humain |

Ces seuils sont **des hypothèses de projet**, pas des résultats certifiés.

## Frontières de confiance et résilience

Répartir les identités entre utilisateur, workload et outil ; secrets dans un coffre ; chiffrement en transit ; contrôle d'ACL sur les données et le retrieval. Les traces enregistrent uniquement IDs pseudonymes, version des politiques, outil, décision, latence et coût agrégé. Prévoir timeout par outil, circuit breaker, retry avec backoff sur lectures idempotentes et DLQ sur traitements asynchrones. Aucun rejeu d'écriture sans clé d'idempotence.

**Décisions à approfondir** : [ADR](02-adr.md), [mesure](03-evaluations.md), [contrôles](04-controles-raci.md).
