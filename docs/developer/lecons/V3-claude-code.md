# V3 — Claude Code (3,1 %)

## Compétence

Connaître les **composants et niveaux de configuration** de Claude Code, leurs effets sur l'autorisation et le travail d'équipe. Le faible poids à l'examen ne réduit pas l'importance en ingénierie réelle.

- `CLAUDE.md` : instructions persistantes, commandes build/test, conventions, règles de sûreté, chemin d'escalade. Garder la configuration d'équipe **dans le dépôt**.
- `.claude/rules/` : règles ciblées ; `.claude/skills/` : workflows réutilisables ; permissions/hooks dans la configuration selon la version installée.
- **Plan mode** pour arbitrer une refonte ; passage par PR, tests et revue avant fusion.
- **Hooks** utiles pour renforcer un contrôle de workflow, mais ne constituent pas l'unique barrière d'une opération métier.
- Serveur MCP : droits et secrets côté infrastructure, **jamais dans une description d'outil commitée**.

## Exercice et corrigé

Une règle interdisant les paiements automatiques est stockée exclusivement dans `~/.claude/CLAUDE.md` d'un développeur. **Corrigé** : répliquer le principe dans la documentation versionnée d'équipe, et surtout mettre le vrai contrôle dans le backend/permission métier ; un fichier d'instructions ne suffit pas.

## Preuves

[Lab Claude Code](../../../labs/labo2_claude_code/README.md). Vérifier les conventions exactes dans la documentation Claude Code de la version utilisée.
