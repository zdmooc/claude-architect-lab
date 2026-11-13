# M6 · Synthèse et quiz

## Synthèse
- Agent SDK = boucle + outils + MCP + sous-agents + hooks, hébergé par toi.
- **Prompt guide, hook impose** : étapes obligatoires → `PreToolUse` `deny` (ou contrôle dans l'outil).
- Outils maison via serveur MCP in-process (`mcp__serveur__outil`) ; `allowed_tools` minimal ; `max_turns` = garde-fou.
- Sous-agents : contexte **explicite**, périmètres complémentaires, format de retour commun, parallélisme pour l'indépendant.
- Pipeline séquentiel si le processus est connu ; décomposition adaptative si la tâche est ouverte.
- Reprise de session : revalider les faits critiques.

## Quiz (questions originales)
**Q1.** Un agent bancaire effectue parfois des virements sans double authentification malgré une consigne en majuscules. Correction ?
A. Répéter la consigne · B. Hook `PreToolUse` qui refuse le virement tant que la double authentification n'est pas validée · C. Exemple few-shot · D. Modèle plus gros

**Q2.** Un sous-agent produit une analyse hors sujet. Sa mission était « continue l'analyse ». Cause la plus probable ?
A. Modèle trop petit · B. Il n'a pas reçu explicitement le contexte · C. Trop d'outils · D. `max_turns` trop bas

**Q3.** (2 réponses) Bonnes pratiques de décomposition :
A. Périmètres complémentaires · B. Plusieurs sous-agents sur la même question pour « être sûr » · C. Format de retour commun · D. Laisser chaque sous-agent choisir son format

**Q4.** Traitement mensuel stable : extraire → valider → produire le rapport. Structure ?
A. Décomposition adaptative · B. Pipeline séquentiel · C. Un seul agent sans outils · D. Batch de sous-agents aléatoires

**Q5.** Rôle de `max_turns` ?
A. Condition d'arrêt normale · B. Garde-fou contre les boucles · C. Limite de coût exacte · D. Nombre de sous-agents

## Corrigé
<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | Règle critique → hook déterministe ; A et C restent du prompt. |
| Q2 | **B** | Le sous-agent ne connaît que ce qu'on lui passe. |
| Q3 | **A, C** | Couverture complète sans doublon, synthèse facile. B gaspille ; D complique l'agrégation. |
| Q4 | **B** | Étapes stables et connues → pipeline. |
| Q5 | **B** | Garde-fou ; l'arrêt normal est la fin de la tâche. |

</details>
