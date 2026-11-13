# Labo M3 — Tool use

| Fichier | Leçon | Contenu |
|---|---|---|
| `outils_contrats.py` | L2 | 3 outils fictifs, descriptions distinctives, erreurs structurées |
| `boucle_manuelle.py` | L1 | boucle `tool_use` → `end_turn`, garde-fou d'itérations |
| `tool_runner.py` | L3 | même chose avec le Tool Runner du SDK (beta) |
| `test_outils.py` | L2 | tests **sans API** : vide ≠ erreur, introuvable, panne transitoire |

```bash
cd labs/m3
python test_outils.py                 # sans clé
python boucle_manuelle.py "Quels sinistres sur le contrat de Mme Durand ?"   # avec clé
```
Statut : `test_outils.py` **exécuté** par le formateur (4 tests OK) ; scripts API compilés, **non exécutés**.
