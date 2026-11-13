# D3 — Integration (19 %)

**But** : intégrer Claude au SI d'entreprise avec identité, autorisation, résilience, contrats d'interface et audit de bout en bout.

## 1. Architecture d'intégration

Chemin recommandé : portail → API Gateway/OIDC → orchestration → moteur d'autorisation → outils métier lecture seule → API Claude pour les tâches cognitives → validation métier → proposition → humain si nécessaire. Porter un identifiant de corrélation non sensible et une identité explicite dans chaque service.

### API directe ou MCP ?

- **API métier directe** : une application et quelques outils ; surface minimale.
- **Serveur MCP** : mutualisation d'outils/ressources entre plusieurs clients compatibles ; standardisation des descriptions et découverte.
- Dans les deux cas : permissions **dans le serveur métier**, scopes, propriétaire de la donnée, secrets hors Git, versionnement, timeouts, quotas et protocole d'erreurs. Un accès technique au serveur MCP ne vaut pas autorisation à consulter tous les contrats.

## 2. Outils métiers

| Outil | Contrat | Contrôle impératif |
|---|---|---|
| consulter_contrat | entrée contrat_id ; sortie garanties/statut/version | vérifier titulaire et scope |
| rechercher_procedure | recherche + date ; passages sourcés | ACL documentaire et validité |
| soumettre_proposition | sinistre_id, montant, clé idempotence | autorisation, seuil, journal, statut |
| escalader | cause + résumé structuré | routage gestionnaire habilité |

Distinguer liste vide, refus d'accès, introuvable, panne temporaire et résultat ambigu. Les résultats d'outils sont des **données non fiables** tant que leur origine et forme ne sont pas validées.

## 3. RAG et événements

RAG : filtre d'accès avant retrieval, source/version/date, évaluation recall@k et exactitude de la réponse ; éviter la citation d'un extrait que l'utilisateur n'est pas autorisé à voir.

Asynchrone : message avec event_id, outbox, clé d'idempotence, DLQ, rejouabilité et suivi d'état. Un retry d'écriture sans clé d'idempotence peut créer deux propositions. Prévoir circuit breaker, bornes de retry et repli humain.

## 4. Sécurité et exploitation

Traces : correlation_id, acteur/périmètre, outil, résultat, version de politique, latence ; **pas de secret ni de facture brute** dans le journal de diagnostic. Tester BOLA/IDOR, permissions inter-contrats, replay, timeouts, retry, tool injection, secrets et invalidation de procédure.

**Livrable** : carte d'interfaces, matrice d'identité, contrat d'outils, séquence nominale et dégradée, tests de refus et critères d'acceptation.

Voir [HLD](../cas-assurnova/01-hld.md) et [contrôles/RACI](../cas-assurnova/04-controles-raci.md).
