# M5 · Leçon 1 — Mémoire de projet : `CLAUDE.md`, imports et règles conditionnelles (D3)

> **Statut** : configuration proposée dans `labs/labo2_claude_code/`. Comportement de Claude Code avec ces fichiers **non exécuté** par le formateur : à observer toi-même. Version de référence : Claude Code 2.1.323.

## 1. Objectif et utilité
Donner à Claude Code le **contexte d'équipe** (commandes, conventions, règles) sans le répéter à chaque session, et savoir **qui** voit **quoi**.
D3 (20 %, selon le dossier) commence par : hiérarchie `CLAUDE.md`, `@import`, `.claude/rules/`, règles par chemins.

## 2. Prérequis
M0·L2 (ce qu'est Claude Code). **Installation** (le moment est venu) :
1. Node.js 18+ ou l'installeur natif décrit sur la doc officielle de Claude Code.
2. `claude` dans un terminal, puis connexion.
⚠️ **Dépense** : Claude Code fonctionne avec un abonnement Claude (Pro/Max…) **ou** des crédits API. **Ne souscris rien sans m'en parler** ; on choisira l'option la moins chère.

## 3. Cours
### a) La hiérarchie
| Niveau | Fichier | Portée | Versionné |
|---|---|---|---|
| Utilisateur | `~/.claude/CLAUDE.md` | tous tes projets | non |
| Projet | `CLAUDE.md` à la racine | toute l'équipe | **oui** |
| Local | `CLAUDE.local.md` | toi, ce projet | non (`.gitignore`) |
| Sous-répertoire | `sous-dossier/CLAUDE.md` | quand on travaille dans ce dossier | oui |
👉 Analogie : configuration WebSphere cellule → nœud → serveur : du général au particulier.

### b) Garder `CLAUDE.md` court : `@import`
`@docs-equipe.md` dans `CLAUDE.md` importe un autre fichier. On modularise au lieu d'un pavé de 500 lignes.

### c) Règles conditionnelles : `.claude/rules/`
Un fichier de règles avec un en-tête `paths:` ne s'applique qu'aux fichiers concernés :
```yaml
---
paths:
  - "**/test_*.py"
---
```
→ les règles de test s'appliquent **où que soient** les fichiers de test. C'est mieux qu'un `CLAUDE.md` par dossier quand les fichiers concernés sont dispersés.

### d) Que mettre dedans ?
Ce que Claude **ne peut pas deviner** : commandes de build/test, conventions, pièges du projet. Pas ce qu'il lit déjà dans le code.

## 4. Exemple commenté : `labs/labo2_claude_code/`
- `CLAUDE.md` : contexte, commandes, 3 règles d'équipe, import `@docs-equipe.md`.
- `.claude/rules/tarification.md` → `paths: src/**/*.py`.
- `.claude/rules/tests.md` → `paths: **/test_*.py`.

## 5. Exercice guidé
« Mes collègues ne voient pas mes consignes de style. » Diagnostic :
1. Où sont-elles ? Dans `~/.claude/CLAUDE.md` → **portée utilisateur**, donc invisibles pour l'équipe.
2. Correction : les déplacer dans le `CLAUDE.md` **projet** (versionné) si elles sont communes.
Ce diagnostic de portée est un scénario typique du guide (dossier §7.2 : « explication des différences utilisateur/projet »).

## 6. Exercice à toi
- **E1.** Où mets-tu : (a) la commande de test du projet, (b) ta préférence « réponds-moi en français », (c) ton chemin local vers un jeu de données de test ?
- **E2.** Les tests sont dans `tests/`, `src/api/tests/` et `modules/*/test_*.py`. Pourquoi une règle `paths` est-elle meilleure qu'un `CLAUDE.md` dans chaque dossier ?
- **E3.** (avec Claude Code) Ouvre `labs/labo2_claude_code`, demande « quelles règles s'appliquent quand tu modifies tests/test_devis.py ? ». Note ce qu'il répond.

## 7. Correction
<details><summary>Voir la correction</summary>

- **E1.** (a) `CLAUDE.md` du **projet** (partagé). (b) `~/.claude/CLAUDE.md` (**utilisateur**). (c) `CLAUDE.local.md` (personnel à ce projet, ignoré par Git).
- **E2.** Une règle `paths: "**/test_*.py"` s'applique **partout où le motif correspond**, se maintient à **un seul endroit** et suit les nouveaux dossiers ; plusieurs `CLAUDE.md` se dupliquent et divergent.
- **E3.** Résultat observé à toi. Attendu : `CLAUDE.md` + `docs-equipe.md` importé, plus `.claude/rules/tests.md` ; **pas** `tarification.md` (motif `src/**/*.py`).

</details>
## 8. À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Hiérarchie : utilisateur (`~/.claude/CLAUDE.md`) · projet (`CLAUDE.md`, versionné) · local (`CLAUDE.local.md`).
- `@import` pour factoriser ; `.claude/rules/` + `paths:` pour cibler.
- Conventions d'équipe dans la config utilisateur = invisibles pour les autres.

</details>
