# Labo 2 — Claude Code partagé dans une équipe (M5, D3)

Mini-projet fictif pour s'exercer à **configurer** Claude Code. Ouvre Claude Code **dans ce dossier** (`cd labs/labo2_claude_code && claude`).

| Élément | Fichier | Notion |
|---|---|---|
| Mémoire projet | `CLAUDE.md` (+ import `@docs-equipe.md`) | hiérarchie, `@import` |
| Règles conditionnelles | `.claude/rules/*.md` avec `paths:` | règles par chemin |
| Commande partagée | `.claude/commands/revue.md` → `/revue` | commandes d'équipe |
| Skill | `.claude/skills/revue-architecture/SKILL.md` | `allowed-tools`, `context: fork`, `argument-hint` |
| CI | `ci/revue_ci.sh` | `-p`, `--output-format json`, `--json-schema` |
| Config perso (non versionnée) | `CLAUDE.local.md`, `.claude/settings.local.json` | exclus par `.gitignore` |

Statut :
- tests `pytest` **exécutés** par le formateur (4 OK) ;
- options CLI vérifiées dans l'aide de Claude Code 2.1.323 ;
- comportement de Claude Code avec cette configuration (règles, skill, CI) **non exécuté** : à observer toi-même.
