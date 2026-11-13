"""M4 — Serveur MCP FICTIF « référentiel contrats » (données synthétiques).

Code vérifié contre le SDK Python MCP `mcp` 2.3.0 (13/11/2026) :
- en 2.x, `FastMCP` a été renommé `MCPServer` (`from mcp.server.mcpserver import MCPServer`) ;
- lever `ToolError` renvoie au client un résultat `is_error=True` avec ton message ;
  toute autre exception est traitée comme un crash (message générique).
Si tu trouves un tutoriel avec `from mcp.server.fastmcp import FastMCP`, c'est la v1.

Lancement (transport stdio, utilisé par Claude Code) : python serveur_contrats.py
"""
import json
import os

from mcp.server.mcpserver import MCPServer
from mcp.server.mcpserver.exceptions import ToolError

serveur = MCPServer("referentiel-contrats")

CONTRATS = {
    "AUTO-4471": {"client": "C-1001", "type": "auto", "franchise": 300, "statut": "actif"},
    "HAB-2210": {"client": "C-1002", "type": "habitation", "franchise": 150, "statut": "résilié"},
}
SINISTRES = {"AUTO-4471": [{"id": "S-88", "nature": "bris de glace", "statut": "expertise"}], "HAB-2210": []}

# Exemple de configuration par variable d'environnement (jamais de secret en dur).
# Le jeton n'est pas utilisé ici ; il montre où il arriverait.
JETON_REFERENTIEL = os.environ.get("REFERENTIEL_TOKEN")


@serveur.tool()
def consulter_contrat(numero: str) -> str:
    """Lit le détail d'UN contrat d'assurance à partir de son numéro exact (ex. 'AUTO-4471').
    Renvoie type, franchise, statut, identifiant client. Ne liste pas les sinistres :
    utilise lister_sinistres pour cela."""
    contrat = CONTRATS.get(numero)
    if contrat is None:
        # Échec ANTICIPÉ -> ToolError -> is_error=True, message lisible par le modèle.
        raise ToolError(json.dumps({"categorie": "introuvable", "reessayable": False,
                                    "message": f"Aucun contrat {numero}. Vérifie le numéro."}, ensure_ascii=False))
    return json.dumps({"numero": numero, **contrat}, ensure_ascii=False)


@serveur.tool()
def lister_sinistres(numero: str) -> str:
    """Liste les sinistres d'UN contrat (numéro exact). Une liste vide signifie
    qu'aucun sinistre n'est déclaré : ce n'est pas une erreur."""
    if numero not in CONTRATS:
        raise ToolError(json.dumps({"categorie": "introuvable", "reessayable": False,
                                    "message": f"Aucun contrat {numero}."}, ensure_ascii=False))
    return json.dumps({"sinistres": SINISTRES[numero]}, ensure_ascii=False)


@serveur.resource("doc://procedures/franchise", mime_type="text/markdown")
def procedure_franchise() -> str:
    """Procédure interne (fictive) d'application de la franchise. Ressource en LECTURE seule."""
    return (
        "# Application de la franchise (fictif)\n"
        "1. Vérifier le statut du contrat (actif).\n"
        "2. Déduire la franchise du montant indemnisable.\n"
        "3. Bris de glace : franchise réduite de 50 % si réparation (pas de remplacement).\n"
    )


if __name__ == "__main__":
    serveur.run()  # transport stdio par défaut
