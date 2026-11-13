# Labo 1 — Agent de support avec contrôles métier (M6, D1/D5)

- `agent_support.py` : Agent SDK, 2 outils via serveur MCP in-process, **hook PreToolUse** qui bloque le remboursement sans identité vérifiée ou au-delà de 1 000 €.
- `test_hook.py` : tests du hook **sans API**.

```bash
pip install claude-agent-sdk
cd labs/labo1_support && python test_hook.py      # sans clé
python agent_support.py                            # nécessite Claude Code installé + accès (coût)
```
Statut : `test_hook.py` **exécuté** par le formateur (4 OK) avec `claude-agent-sdk` 0.2.181 ; agent complet **non exécuté**.
