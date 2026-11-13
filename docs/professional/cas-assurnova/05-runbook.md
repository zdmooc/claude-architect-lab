# 05 — Runbook d'exploitation, incidents et repli

**Service fictif** : Assistance sinistres. **Responsable opérationnel** : Run Manager à nommer ; astreinte et contacts à renseigner dans le référentiel d'exploitation (pas de PII dans Git).

## Indicateurs et alertes

| Signal | Diagnostic | Action initiale |
|---|---|---|
| P95 au-delà du SLO négocié | séparer API Claude, MCP, OCR, backend et queue | limiter débit, repli manuel |
| Hausse refus / JSON invalides | modèle/prompt, changement schéma, OCR | revenir version précédente |
| 403 anormaux / accès transversal | identité, mandats, ACL | suspendre outil concerné ; incident sécurité |
| Propositions en double | idempotence, retries, outbox | suspendre écriture ; réconcilier |
| Coût par dossier anormal | boucle outil, tokens, volumétrie | réduire quota, isoler flux |
| Escalades non prises | queue/ticketing, assignation | activer gestionnaire de secours |

## Procédure incident P1 — action non autorisée

1. **Contenir** : désactiver l'outil ou endpoint d'écriture via feature flag ; ne pas simplement modifier le prompt.
2. **Préserver** : garder trace d'audit minimisée et versions policy/code, sécuriser les clés, tracer les dossiers concernés.
3. **Qualifier** avec RSSI + métier + DPO selon la nature des données ; engager la procédure interne d'incident.
4. **Réparer** : corriger autorisation dans service métier, ajouter régression négative (identité, seuil, BOLA, replay).
5. **Restaurer** après double validation sécurité/métier ; observer un canary. Documenter RCA et actions préventives.

## Procédure P2 — Claude ou MCP indisponible

- Ouvrir circuit breaker / arrêter les retries non bornés.
- Conserver dossier et état de file, afficher une information neutre au client ; envoyer à un gestionnaire.
- Ne **jamais** extrapoler une garantie ou un montant depuis un cache non autorisé.
- Reprendre uniquement les actions de lecture idempotentes et les écritures munies d'une clé durable.
- Mesurer temps de dégradé, backlog et délai de rétablissement.

## Déploiement / retour arrière

Pipeline : tests + evals signées → environnement pilote → canary faible pourcentage → vérification métriques par segment → extension progressive. Si une action interdite, hausse critique des erreurs ou P95 hors budget persiste : retour modèle/prompt/app version précédente, conservation des preuves, passage en mode manuel.

## Checklist de transfert aux opérations

- [ ] Dépendances, cartes de flux et propriétaires connus
- [ ] Dashboards latence/coût/erreurs et seuils d'alerte validés
- [ ] Procédures P1/P2 exercées et datées
- [ ] Plan restauration état de dossier et DLQ testé
- [ ] Rotation des secrets, droits et certificats attribuée
- [ ] Plan d'évaluation continue et changements modèle documentés
- [ ] Critères de fermeture d'incident et contacts d'escalade connus
