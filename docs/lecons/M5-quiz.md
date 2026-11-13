# M5 · Synthèse et quiz

## Synthèse
- `CLAUDE.md` : utilisateur (`~/.claude/`), projet (versionné), local (non versionné), sous-répertoires.
- `@import` pour modulariser ; `.claude/rules/` + `paths:` pour des règles par type de fichier.
- Commandes : `.claude/commands/` (équipe) vs `~/.claude/commands/` (perso).
- Skills : `SKILL.md`, `description`, `allowed-tools`, `context: fork`, `argument-hint`.
- Plan mode pour l'incertain et le multi-fichiers ; exécution directe pour le simple.
- CI : `-p`, `--output-format json`, `--json-schema`, `--allowedTools`. Revue par une instance indépendante.

## Quiz (questions originales)
**Q1.** Un développeur a mis les conventions de nommage de l'équipe dans `~/.claude/CLAUDE.md`. Ses collègues ne les voient pas. Correction ?
A. Les dupliquer dans le prompt de chaque session · B. Les mettre dans le `CLAUDE.md` du projet · C. Les mettre dans `CLAUDE.local.md` · D. Créer une Skill

**Q2.** Les fichiers de test sont dispersés dans 15 dossiers. Meilleure façon d'appliquer des règles de test ?
A. Un `CLAUDE.md` par dossier · B. Une règle dans `.claude/rules/` avec `paths: "**/test_*.py"` · C. Les mettre dans le `CLAUDE.md` racine · D. Une commande `/tests`

**Q3.** Une Skill d'analyse produit beaucoup d'intermédiaires qui encombrent la conversation. Quel champ ?
A. `allowed-tools` · B. `argument-hint` · C. `context: fork` · D. `description`

**Q4.** En CI, il faut un résultat exploitable par le pipeline. (2 réponses)
A. `-p` · B. Mode interactif · C. `--output-format json` · D. `--permission-mode plan`

**Q5.** Refonte de l'architecture de 30 fichiers aux dépendances mal connues. Mode recommandé ?
A. Exécution directe · B. Plan mode · C. CI non interactive · D. Une commande personnelle

**Q6.** Pourquoi une instance indépendante pour la revue ?
A. Elle coûte moins cher · B. Elle n'hérite pas du contexte et des angles morts de la session de génération · C. C'est obligatoire techniquement · D. Elle est plus rapide

### Questions supplémentaires (banque d'entraînement)

**Q7.** Claude Code ne doit jamais lire le fichier `.env` du projet. Quelle solution est la plus fiable ?
A. Une phrase claire dans le CLAUDE.md du projet, versionné et partagé : « Ne jamais lire ni afficher le fichier .env » · B. Une règle de permission `deny` (par exemple `Read(./.env)`) dans les settings partagés du projet · C. Renommer le fichier · D. Le rappeler oralement à chaque session

## Corrigé
<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | Partagé = `CLAUDE.md` projet versionné. C est personnel et ignoré par Git. |
| Q2 | **B** | Règle ciblée par motif, un seul endroit à maintenir. |
| Q3 | **C** | `context: fork` isole les intermédiaires. |
| Q4 | **A, C** | Non interactif + sortie JSON exploitable. D ne produit pas de modifications, ce n'est pas la question. |
| Q5 | **B** | Changement large et flou : planifier, valider, puis exécuter. |
| Q6 | **B** | Indépendance = pas d'angles morts hérités. |
| Q7 | **B** | A : CLAUDE.md guide le comportement mais n'est pas un contrôle d'accès · B : la règle est appliquée par l'outil, pas laissée au jugement du modèle (exemple `Read(./.env)` vérifié dans la doc des settings Claude Code) · C : contournement fragile, d'autres fichiers sensibles resteront exposés · D : repose sur la mémoire humaine et le modèle. À retenir : Interdiction critique : une règle de permission, pas une consigne. |

</details>
