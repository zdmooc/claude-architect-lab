# Labo 4 — Recherche multi-agent avec provenance (M6, D1/D5)

- Un **coordinateur**, deux **sous-agents** aux périmètres complémentaires (replatform / refactor).
- Contexte passé **explicitement** (les sous-agents n'héritent pas de la conversation).
- Format de preuve : `{affirmation, extrait, source, date_source}` + `lacunes`.

Statut : compilé avec `claude-agent-sdk` 0.2.181, **non exécuté** (coût, nécessite Claude Code installé).
Exercices de robustesse (M7) : simuler un timeout, introduire deux sources contradictoires.
