# M5 · Leçon 2 — Commandes et Skills (D3)

> **Statut** : `revue.md` et `SKILL.md` proposés selon les champs listés dans ton dossier (`context: fork`, `allowed-tools`, `argument-hint`) ; comportement **non exécuté** par le formateur.

## 1. Objectif et utilité
Rendre des procédures **réutilisables et partagées** : une commande `/revue` pour toute l'équipe, une Skill « revue d'architecture » isolée et limitée en outils.

## 2. Prérequis
M5·L1.

## 3. Cours
### a) Commandes
Un fichier Markdown dans `.claude/commands/` → une commande `/nom`.
- **Projet** : `.claude/commands/` (versionné) → partagée avec l'équipe.
- **Personnelle** : `~/.claude/commands/` → pour toi seul.

### b) Skills
Un dossier `.claude/skills/<nom>/SKILL.md` : instructions + éventuels fichiers de ressources. Champs d'en-tête à connaître (dossier §3.4) :
| Champ | Effet |
|---|---|
| `description` | quand Claude doit l'utiliser (il la lit pour décider) |
| `allowed-tools` | outils autorisés pendant la Skill (ex. lecture seule) |
| `context: fork` | s'exécute dans un **contexte séparé** : le détail ne pollue pas la conversation principale |
| `argument-hint` | indique l'argument attendu |

### c) Commande ou Skill ?
- **Commande** : un raccourci que **l'utilisateur** déclenche.
- **Skill** : une compétence que **Claude** peut choisir d'utiliser selon la description, avec éventuellement isolation et restrictions.

### d) Moindre privilège, encore
Une revue n'a pas besoin d'écrire : `allowed-tools: Read, Grep, Glob`. Même logique qu'en M3·L2.

## 4. Exemple commenté
- `.claude/commands/revue.md` → `/revue` : revue du `git diff` selon les règles du projet.
- `.claude/skills/revue-architecture/SKILL.md` : lecture seule, `context: fork`, rendu en tableau.

## 5. Exercice guidé
« La Skill d'analyse de logs remplit la conversation de milliers de lignes. » → `context: fork` : l'analyse se fait à part, seule la conclusion revient.

## 6. Exercice à toi
- **E1.** Écris l'en-tête d'une Skill `generer-tests` qui peut lire **et** écrire uniquement des fichiers (pas de Bash). Justifie `context`.
- **E2.** Une commande `/deployer-prod` est dans `~/.claude/commands/` d'un développeur. Problème ? Où devrait-elle être, et faut-il seulement la partager ?
- **E3.** Commande ou Skill pour : (a) « génère le changelog de la release » lancé par le responsable de release ; (b) « vérifie la conformité RGPD d'un module » que Claude devrait appliquer de lui-même quand on touche aux données personnelles ?

## 7. Correction
<details><summary>Voir la correction</summary>

- **E1.**
```yaml
---
name: generer-tests
description: Génère des tests pytest pour un module Python. À utiliser quand on demande d'ajouter ou compléter des tests.
allowed-tools: Read, Glob, Grep, Write, Edit
context: fork
---
```
`context: fork` : la génération produit beaucoup de lectures intermédiaires ; on les isole et on ne garde que le résultat.
- **E2.** Une commande de **prod** personnelle : non versionnée, non relue, propre à une personne. La mettre dans `.claude/commands/` du **projet**, revue en PR. Et surtout la **protéger** : un déploiement prod passe par la CI/CD avec validation, pas par une commande libre.
- **E3.** (a) **Commande** (déclenchée explicitement par quelqu'un). (b) **Skill** (Claude l'invoque de lui-même grâce à sa `description`).

</details>
## 8. À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Commande = lancée par l'utilisateur (`/nom`). Skill = choisie par Claude via sa `description`.
- `allowed-tools` limite les outils ; `context: fork` isole les intermédiaires ; `argument-hint` documente les arguments.
- Commandes d'équipe dans le projet, versionnées.

</details>
