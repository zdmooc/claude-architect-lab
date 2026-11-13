# M5 · Leçon 3 — Plan mode, itération par les tests et Claude Code en CI (D3)

> **Statut** : options CLI **vérifiées** dans l'aide de Claude Code 2.1.323 (`-p/--print`, `--output-format text|json|stream-json`, `--json-schema` « only works with --print », `--allowedTools`, `--permission-mode` incluant `plan`). `ci/revue_ci.sh` **non exécuté**.

## 1. Objectif et utilité
Choisir le bon mode de travail, et faire tourner Claude Code **sans humain** dans une chaîne CI avec une sortie exploitable.

## 2. Prérequis
M5·L1, M2·L2 (schémas JSON).

## 3. Cours
### a) Plan mode ou exécution directe ?
| Tâche | Mode |
|---|---|
| Corriger une faute, renommer une variable | exécution directe |
| Refonte multi-fichiers, choix d'architecture, impact incertain | **plan mode** : Claude analyse et propose un plan **sans modifier**, tu valides, puis il exécute |
👉 Comme un `oc diff` / `terraform plan` avant `apply`.

### b) Itérer avec des exemples et des tests
Donner des **exemples d'entrée/sortie** et un **test qui échoue** : Claude a une cible vérifiable, il itère jusqu'au vert.

### c) Mode non interactif
```bash
claude -p "consigne" --output-format json --json-schema "$SCHEMA" --allowedTools "Read,Grep,Glob"
```
- `-p` / `--print` : pas d'interaction, sortie sur stdout.
- `--output-format json` : résultat structuré.
- `--json-schema` : la sortie doit respecter ton schéma (comme M2).
- `--allowedTools` : moindre privilège en CI.

### d) Génération ≠ revue
La session qui a **écrit** le code est mal placée pour le **relire** : elle partage ses propres angles morts. Bonne pratique (dossier §3.4) : une **instance indépendante**, avec un contexte neuf, fait la revue.
👉 Le principe des quatre yeux.

### e) Faux positifs en CI
Une revue automatique trop bavarde est ignorée. Dans la consigne : « liste uniquement les problèmes réels », gravité obligatoire, et on ne bloque la PR que sur `bloquant`.

## 4. Exemple commenté : `ci/revue_ci.sh`
- Schéma : `problemes[]` avec `fichier`, `gravite` (`bloquant|majeur|mineur`), `description`.
- `--allowedTools "Read,Grep,Glob"` : la revue ne peut rien modifier.
- La suite du pipeline lit `revue.json` et échoue seulement s'il y a un `bloquant`.

## 5. Exercice guidé
« En CI, Claude Code reste bloqué. » Cause probable : lancé **sans** `-p`, il attend une interaction. Correction : `-p` + outils autorisés explicitement.

## 6. Exercice à toi
- **E1.** Plan mode ou exécution directe : (a) passer de `unittest` à `pytest` sur 40 fichiers ; (b) corriger un arrondi dans `devis.py` couvert par un test qui échoue.
- **E2.** Pourquoi la revue doit-elle être faite par une **autre** instance que celle qui a généré le code ?
- **E3.** (avec Claude Code — consomme ton abonnement/crédits) Dans `labs/labo2_claude_code`, lance `bash ci/revue_ci.sh` et colle-moi `revue.json`.

## 7. Correction
*Après ta réponse.*
## 8. À retenir pour l'examen
*Avec la correction.*
