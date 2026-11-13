# Labo 1 — Agent de support avec contrôles métier (M6, D1/D5)

- `agent_support.py` : Agent SDK, 2 outils via serveur MCP in-process, **hook PreToolUse** qui bloque le remboursement sans identité vérifiée ou au-delà de 1 000 €.
- **Défense en profondeur** : la règle est écrite une fois (`regle_remboursement`) et appliquée deux fois, par le hook **et** dans l'outil `rembourser`. Si le hook est retiré, mal ciblé, ou si l'outil est appelé par un autre client, l'outil refuse quand même (erreur structurée, non réessayable).
- `test_hook.py` : 10 tests **sans API** : hook, outil appelé sans hook, limite à 1 000,00 €, montants invalides.

```bash
pip install claude-agent-sdk
cd labs/labo1_support && python test_hook.py      # sans clé
python agent_support.py                            # nécessite Claude Code installé + accès (coût)
```
Statut : `test_hook.py` **exécuté** par le formateur (10 OK) et en CI avec `claude-agent-sdk` 0.2.181 ; agent complet **non exécuté**.
