"""Test HORS API du hook de contrôle : python test_hook.py"""
import asyncio

import agent_support as a


async def main():
    entree = {"tool_name": a.NOM_OUTIL_REMBOURSER, "tool_input": {"contrat": "AUTO-4471", "montant": 200.0}}

    a.ETAT["identite_verifiee"] = False
    r = await a.controle_remboursement(entree, "t1", None)
    assert r["hookSpecificOutput"]["permissionDecision"] == "deny", "identité non vérifiée -> refus"

    a.ETAT["identite_verifiee"] = True
    assert await a.controle_remboursement(entree, "t2", None) == {}, "vérifié + petit montant -> autorisé"

    gros = {**entree, "tool_input": {"contrat": "AUTO-4471", "montant": 1500.0}}
    r = await a.controle_remboursement(gros, "t3", None)
    assert "conseiller" in r["hookSpecificOutput"]["permissionDecisionReason"], "seuil -> humain"

    autre = {"tool_name": "mcp__support__verifier_identite", "tool_input": {}}
    assert await a.controle_remboursement(autre, "t4", None) == {}, "autres outils non concernés"
    print("OK : 4 tests du hook passés")


asyncio.run(main())
