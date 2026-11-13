# Labo 3 — Extraction documentaire structurée (D4, D5)

Données **100 % synthétiques**.

| Fichier | Rôle |
|---|---|
| `schema.py` | Schéma Pydantic : champs nullables, catégorie extensible, `ambiguites` |
| `validation.py` | Règles **métier** (cohérence HT+TVA=TTC, dates, catégorie) |
| `prompt.py` | Consignes + exemples few-shot de cas difficiles |
| `extraire.py` | Extraction synchrone + relance ciblée (1 max) + revue humaine |
| `batch_extraire.py` | Message Batches, `custom_id`, reprise sélective |
| `corpus/` | 5 factures fictives, dont des cas pièges |

Cas pièges volontaires : F002 (HT absent), F003 (TTC incohérent), F004 (catégorie « autre », pas de HT/TVA), F005 (illisible).

```bash
cd labs/labo3_extraction
pip install anthropic pydantic
python extraire.py corpus/F003.txt
```

Statut : code proposé, compilé, **non exécuté** contre l'API par le formateur.
