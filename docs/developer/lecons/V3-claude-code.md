# V3 — Claude Code (3,1 %)

> **Source des objectifs** : guide officiel CCDV-F v1.0, §6, Domain 3. Cours et questions **originaux**. Petit poids à l'examen, gros impact au quotidien. Détails complets : Architect Foundations M5.

## 1. Objectif
Compétence officielle **Claude Code Operation (3,1 %)** : Rules, Skills, Commands, Agents, Agent Memory ; sessions, commandes slash, modes **headless** et streaming, **auto-mode**, hiérarchie `CLAUDE.md`, initialisation d'un dépôt, `settings.json`.

## 2. Prérequis
Architect Foundations M5 (labo 2).

## 3. Cours
| Élément | Rôle | Où |
|---|---|---|
| `CLAUDE.md` | instructions persistantes (build, tests, conventions, interdits) | projet (partagé), `~/.claude/` (perso), `CLAUDE.local.md` (perso, ignoré par Git) |
| Rules | règles ciblées par chemin (`paths:`) | `.claude/rules/` |
| Commands | `/nom` déclenché par l'utilisateur | `.claude/commands/` |
| Skills | savoir-faire chargé à la demande via sa `description` | `.claude/skills/<nom>/SKILL.md` |
| Agents (sous-agents) | spécialistes avec prompt, outils, contexte isolé | `.claude/agents/` |
| Agent memory | mémoire persistante d'un agent entre sessions | selon la version : vérifier la doc |
| `settings.json` | permissions (allow/deny), hooks, variables | `.claude/settings.json` (équipe), `settings.local.json` (perso) |
- **Initialiser un dépôt** : `/init` génère un `CLAUDE.md` de départ, à relire et compléter.
- **Sessions** : reprendre ou repartir à neuf ; compacter quand le contexte s'alourdit.
- **Headless** : `claude -p "…"` non interactif ; `--output-format json` ou `stream-json` pour le streaming ; `--json-schema` pour une sortie structurée ; `--allowedTools` pour restreindre.
- **Modes de permission** : demande de confirmation (défaut), plan, acceptation des modifications, **auto-mode** (Claude décide de plus d'actions seul, avec des garde-fous) : à réserver à des environnements maîtrisés, avec permissions `deny` et hooks.

## 4. Exemple — DevBank
`CLAUDE.md` : `pytest -q`, « jamais de données réelles », « aucun outil de paiement ». Règle `paths: "src/api/**"` : validation de schéma obligatoire. `settings.json` : `deny` sur `Bash(curl:*)` vers la prod. CI : `claude -p` en JSON pour la revue.

## 5. Exercice guidé
Les conventions sont dans le `~/.claude/CLAUDE.md` d'un seul développeur → invisibles pour l'équipe. Les déplacer dans le `CLAUDE.md` du projet, revu en PR.

## 6. Exercice à toi
- **E1.** Commande, Skill ou sous-agent : (a) « génère le changelog » lancé par le release manager ; (b) savoir-faire « écrire une migration SQL sûre » à appliquer quand c'est pertinent ; (c) revue de sécurité isolée avec ses propres outils en lecture seule.
- **E2.** Écris la commande headless qui produit un JSON de revue, sans outil d'écriture.
- **E3.** Un développeur veut activer l'auto-mode sur son poste qui a des identifiants de production. Ta réponse ?

## 7. Correction
<details><summary>Voir la correction</summary>

- **E1.** (a) **Commande**. (b) **Skill**. (c) **Sous-agent**.
- **E2.** `claude -p "Revois le diff de cette PR" --output-format json --json-schema "$(cat schema.json)" --allowedTools "Read,Grep,Glob"`
- **E3.** Non sur un poste avec accès production : retirer ces identifiants, ou utiliser un environnement isolé (conteneur, préprod), règles `deny` et hooks bloquant les commandes destructrices.
</details>

## 8. Questions d'entraînement (originales)
**Q1.** Où mettre la commande de test pour toute l'équipe ?
A. `CLAUDE.local.md` · B. `CLAUDE.md` du projet · C. `~/.claude/CLAUDE.md` · D. Un message Slack

**Q2.** Pour un pipeline CI qui lit la sortie de Claude Code :
A. Mode interactif · B. `claude -p` avec `--output-format json` · C. Auto-mode · D. Plan mode seul

<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | Partagé et versionné. |
| Q2 | **B** | Non interactif, sortie lisible par machine. |
</details>

## 9. À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Hiérarchie : projet (partagé) / utilisateur / local.
- Rules (par chemin), Commands (utilisateur), Skills (à la demande), Agents (isolés), `settings.json` (permissions, hooks).
- Headless `-p` + JSON/stream-json + schéma + outils restreints.
- Auto-mode seulement dans un environnement maîtrisé.
</details>

**Pratique** : [labo 2 Claude Code](../../../labs/labo2_claude_code/README.md). Vérifier les options exactes dans la documentation de ta version.
