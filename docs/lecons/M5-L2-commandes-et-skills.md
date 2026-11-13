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
*Après ta réponse.*
## 8. À retenir pour l'examen
*Avec la correction.*
