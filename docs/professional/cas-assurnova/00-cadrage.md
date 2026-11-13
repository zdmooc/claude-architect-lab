# 00 — Note de cadrage métier et valeur

**Projet** : AssurNova / Assistance bris de glace — **v0.1, simulation**.

## Problème et hypothèses

Le parcours de déclaration impose une lecture de factures et de garanties dispersées. Le sponsor souhaite réduire la ressaisie et accélérer les propositions sans déléguer une décision financière au modèle.

**Hypothèses non vérifiées** : 10 000 dossiers/mois ; trois canaux (portail, courrier numérisé, back-office) ; langage principal français ; authentification OIDC ; référentiels contrat et sinistre existants. Ces valeurs guident la simulation, pas un dimensionnement de production.

## Résultats attendus et bornes

- Produire un **résumé vérifiable** et une **proposition** d'indemnisation lorsque les sources sont disponibles et cohérentes.
- Déclencher un **transfert humain** lorsque demande explicite, identité non vérifiée, garantie manquante, facture ambiguë, alerte fraude ou montant > 800 €.
- **Exclure** du périmètre : exécution de paiement, décision de fraude automatisée, résiliation, conseil juridique et communication autonome avec des tiers.
- Conserver le parcours manuel actuel comme solution de repli.

## Exigences traçables

| ID | Exigence | Critère d'acceptation | Responsable |
|---|---|---|---|
| REQ-01 | Contrat consultable uniquement par son titulaire ou gestionnaire habilité | tests inter-contrats refusés (403) | IAM |
| REQ-02 | Aucun versement par Claude | aucun outil de paiement exposé | produit |
| REQ-03 | Montant > 800 € ou demande client → humain | test 800 / 800,01 et demande directe | métier |
| REQ-04 | Toute proposition justifie ses sources | contrat, procédure, facture et version référencés | métier |
| REQ-05 | Facture ambiguë → pas d'invention | null + motif + file revue | QA |
| REQ-06 | Pas d'action d'écriture sans clé d'idempotence | rejeu n'ajoute pas de proposition | intégration |
| REQ-07 | Dégradé opérationnel en panne API Claude | dossiers routés en traitement manuel | exploitation |
| REQ-08 | Journal d'audit sans documents ni secrets bruts | contrôle des événements et de la rétention | RSSI/DPO |

## Mesures de valeur à établir en baseline

Durée de traitement par dossier, taux de ressaisie, erreurs de facture corrigées en revue, proportion d'escalades justifiées, délai de notification, qualité perçue par les gestionnaires et coût complet (outils, LLM, revues). Comparer avant/après avec saisonnalité ; un taux d'automatisation seul n'est pas un KPI suffisant.

## Décisions ouvertes

Validation par DPO de l'hébergement/traitement ; autorisations du référentiel ; délai cible à négocier ; jeu d'évaluation annoté ; coût des revues ; seuil de 800 € présenté **comme règle de simulation, non comme règle réelle d'assurance**.

**Critère de sortie du cadrage** : sponsor, métier, architecture et sécurité approuvent explicitement les hypothèses et les risques ouverts.
