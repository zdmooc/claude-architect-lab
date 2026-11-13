"""Tests HORS API du serveur MCP (sans Claude, sans réseau) : python test_serveur.py"""
import asyncio

from mcp.server.mcpserver.exceptions import ToolError

from serveur_contrats import serveur


async def main():
    outils = await serveur.list_tools()
    noms = sorted(t.name for t in outils)
    assert noms == ["consulter_contrat", "lister_sinistres"], noms

    ressources = await serveur.list_resources()
    assert any(str(r.uri) == "doc://procedures/franchise" for r in ressources)

    ok = await serveur.call_tool("lister_sinistres", {"numero": "HAB-2210"})
    print("lister_sinistres(HAB-2210) ->", ok)

    try:
        await serveur.call_tool("consulter_contrat", {"numero": "AUTO-9999"})
        raise AssertionError("une ToolError était attendue")
    except ToolError as e:
        print("consulter_contrat(AUTO-9999) -> ToolError :", e)

    print("OK : tests serveur MCP passés")


asyncio.run(main())
