# Labo M1 — API Messages

| Script | Leçon | Ce qu'il montre |
|---|---|---|
| `premier_appel.py` | M1·L1 | requête, blocs de contenu, `stop_reason`, `usage` |
| `conversation.py` | M1·L2 | historique côté application, coût cumulatif |

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r labs/m1/requirements.txt
export ANTHROPIC_API_KEY="..."   # jamais dans le code ni dans Git
python labs/m1/premier_appel.py
```

Statut : code proposé et compilé, **non exécuté** contre l'API par le formateur.
