# 02 — Architecture Decision Records (ADR)

Chaque décision est une **proposition pour exercice**, à confirmer par Architecture Board ; sa date et son sponsor doivent être enregistrés avant adoption réelle.

## ADR-001 — Workflow orchestré plutôt qu'agent autonome

**Contexte** : enchaînement connu, données financières, traitement de pièces non fiables. **Options** : (A) workflow + Claude sur extraction ; (B) agent autonome avec outils ; (C) multi-agent.

**Décision proposée : A**. Les transitions et limites sont vérifiables, les autorisations et politiques exécutées hors du modèle, les retries sont maîtrisables. **Alternatives** : B plus flexible mais plus de chemins imprévus ; C introduit coordination/coût sans besoin métier démontré. **Conséquences** : plus de code d'orchestration, moins de liberté pour cas atypiques. **Réexamen** si évaluation comparative démontre un gain qualité/coût suffisant et sécurité équivalente.

## ADR-002 — Exposition limitée des outils

**Contexte** : contrats et sinistres sont des données à accès restreint. **Options** : (A) API métier directe avec authentification et scopes ; (B) serveur MCP partagé ; (C) accès base de données par l'agent.

**Décision proposée : A en V1**, adaptateur MCP possible si plusieurs clients validés. C rejeté (surfaces excessives). Contrôles côté service : ownership, scopes, journal d'audit, limite débit. **Réexamen** si une mutualisation multi-client apporte un bénéfice justifié et que la sécurité de bout en bout est testée.

## ADR-003 — Autorisation et montant déterministes

**Contexte** : une instruction LLM ne garantit pas l'application d'une règle. **Décision** : valider identité, titre contractuel, seuil 800 € et idempotence dans le service métier avant création de proposition. Claude ne dispose jamais d'un outil de règlement.

**Alternatives rejetées** : prompt seul, hook d'agent seul. Le hook sert de défense additionnelle mais n'est pas le **point d'autorité métier**. **Preuve requise** : tests 800/800,01, identité absente, accès inter-contrats, rejeu et service de droits indisponible.

## ADR-004 — Révision contrôlée des modèles et prompts

**Contexte** : version et tarifs évoluent ; un modèle performant sur un segment peut régresser sur un autre. **Décision** : schéma strict, prompt et modèle versionnés, dataset annoté, comparaison segmentée, canary et rollback. **Réexamen** à chaque changement majeur de guide/API, de données ou de résultat de sécurité.

## Registre d'arbitrage

| ADR | Décideur à solliciter | Preuve avant GO | Statut |
|---|---|---|---|
| 001 | Architecture Board + métier | benchmark motifs, HLD | proposé |
| 002 | RSSI + intégration | tests ACL/BOLA et contrats | proposé |
| 003 | métier + sécurité | tests de refus et idempotence | proposé |
| 004 | qualité + exploitation | rapport d'evals et canary | proposé |
