# Labo M4 — Serveur MCP « référentiel contrats » (fictif)

| Fichier | Rôle |
|---|---|
| `serveur_contrats.py` | 2 outils + 1 ressource, erreurs via `ToolError` |
| `test_serveur.py` | tests **sans Claude** (liste outils/ressources, vide ≠ erreur, ToolError) |
| `mcp.json.exemple` | config projet pour Claude Code, secret par variable d'environnement |

```bash
pip install -r labs/m4/requirements.txt
cd labs/m4 && python test_serveur.py
```
Statut : `test_serveur.py` **exécuté** par le formateur avec `mcp` 2.3.0 (OK). Branchement dans Claude Code : **non testé** (à faire en M5).
⚠️ `mcp` 2.x : `FastMCP` est devenu `MCPServer`. Les tutoriels v1 ne fonctionnent pas tels quels.
