# M4 · Leçon 2 — Construire un serveur MCP en Python

> **Statut** : `labs/m4/serveur_contrats.py` vérifié contre `mcp` 2.3.0 ; `test_serveur.py` **exécuté** par le formateur (résultat observé : 2 outils, 1 ressource, liste vide renvoyée sans erreur, `ToolError` levée pour un contrat inconnu).

## 1. Objectif et utilité
Écrire un serveur MCP minimal, **testable sans Claude**, avec des erreurs propres. C'est le livrable que ton dossier propose pour D2 : « un serveur MCP fictif avec plusieurs outils bien décrits, des erreurs testables et une ressource documentaire ».

## 2. Prérequis
M4·L1, M3·L2.

## 3. Cours
### a) Le squelette (SDK `mcp` 2.x)
```python
from mcp.server.mcpserver import MCPServer
from mcp.server.mcpserver.exceptions import ToolError
serveur = MCPServer("referentiel-contrats")

@serveur.tool()
def consulter_contrat(numero: str) -> str:
    """Docstring = description vue par le modèle."""
    ...

@serveur.resource("doc://procedures/franchise", mime_type="text/markdown")
def procedure_franchise() -> str: ...

serveur.run()   # stdio par défaut
```
⚠️ **Fait observé** : en 2.x, `FastMCP` s'appelle `MCPServer`. Beaucoup de tutoriels montrent encore `from mcp.server.fastmcp import FastMCP` (v1) : ce code échoue avec la v2. Réflexe d'architecte : **noter la version** de chaque SDK.

### b) Erreurs : anticipées vs crash
| Ce que tu fais | Ce que reçoit le client |
|---|---|
| `raise ToolError("message clair")` | résultat `is_error=True` **avec ton message** → le modèle peut réagir |
| Une autre exception (bug) | `is_error=True` avec un message **générique** « Error executing tool … » → le modèle ne sait pas quoi faire |

Donc : on **anticipe** les échecs métier et on lève `ToolError` avec un contenu structuré (catégorie, réessayable, message).

### c) Tester sans Claude
`test_serveur.py` appelle directement `serveur.list_tools()`, `serveur.list_resources()` et `serveur.call_tool(...)`. En appel direct, l'erreur anticipée remonte sous forme d'exception `ToolError` ; via le protocole, elle devient un résultat `is_error=True`.
👉 Comme tester un EJB en local avant de le déployer.

## 4. Exemple commenté
- `lister_sinistres("HAB-2210")` → `{"sinistres": []}`, `is_error=False` (observé). Vide = succès.
- `consulter_contrat("AUTO-9999")` → `ToolError` avec `{"categorie": "introuvable", "reessayable": false, ...}` (observé).
- `JETON_REFERENTIEL = os.environ.get(...)` : un secret arrive par l'environnement, jamais en dur.

## 5. Exercice guidé
On ajoute `rembourser(numero, montant)` au serveur. Contrôles à prévoir **dans le code de l'outil** :
1. contrat inexistant → `ToolError` introuvable ;
2. contrat résilié → `ToolError` règle métier, non réessayable ;
3. montant > 1 000 € → `ToolError` « validation humaine requise » (et création d'un ticket) ;
4. sinon → exécution.
Aucun de ces contrôles ne dépend du prompt.

## 6. Exercice à toi
- **E1.** Lance `python test_serveur.py`. Puis remplace `raise ToolError(...)` par `raise ValueError(...)` dans `consulter_contrat`. Que change-t-il pour le **modèle** (cf. tableau 3b) ?
- **E2.** Ajoute un outil `rechercher_client(nom)` au serveur (sur le modèle de M3). Ajoute un test « nom inconnu → liste vide, pas d'erreur ».
- **E3.** Pourquoi la procédure franchise est-elle une ressource et pas un outil ?

## 7. Correction
*Après ta réponse.*
## 8. À retenir pour l'examen
*Avec la correction.*
