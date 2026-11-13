"""Tests HORS API du contrôle de remboursement (hook ET outil) : python test_hook.py"""
import asyncio
import json

import agent_support as a


def refus_hook(r):
    return r.get("hookSpecificOutput", {}).get("permissionDecision") == "deny"


async def appeler_outil(montant):
    """Appelle directement le handler de l'outil, SANS passer par le hook."""
    return await a.rembourser.handler({"contrat": "AUTO-4471", "montant": montant})


async def main():
    entree = {"tool_name": a.NOM_OUTIL_REMBOURSER, "tool_input": {"contrat": "AUTO-4471", "montant": 200.0}}
    n = 0

    # --- Hook ---------------------------------------------------------------
    a.ETAT["identite_verifiee"] = False
    assert refus_hook(await a.controle_remboursement(entree, "t1", None)), "identité non vérifiée -> refus"; n += 1

    a.ETAT["identite_verifiee"] = True
    assert await a.controle_remboursement(entree, "t2", None) == {}, "vérifié + petit montant -> autorisé"; n += 1

    gros = {**entree, "tool_input": {"contrat": "AUTO-4471", "montant": 1500.0}}
    r = await a.controle_remboursement(gros, "t3", None)
    assert "conseiller" in r["hookSpecificOutput"]["permissionDecisionReason"], "seuil -> humain"; n += 1

    autre = {"tool_name": "mcp__support__verifier_identite", "tool_input": {}}
    assert await a.controle_remboursement(autre, "t4", None) == {}, "autres outils non concernés"; n += 1

    limite = {**entree, "tool_input": {"contrat": "AUTO-4471", "montant": 1000.0}}
    assert await a.controle_remboursement(limite, "t5", None) == {}, "1 000,00 € exactement -> autorisé"; n += 1

    sans_montant = {**entree, "tool_input": {"contrat": "AUTO-4471"}}
    assert refus_hook(await a.controle_remboursement(sans_montant, "t6", None)), "montant absent -> refus"; n += 1

    # --- Outil appelé SANS le hook (défense en profondeur) -------------------
    a.ETAT["identite_verifiee"] = False
    r = await appeler_outil(200.0)
    assert r.get("is_error") is True, "outil : identité non vérifiée -> refus même sans hook"; n += 1

    a.ETAT["identite_verifiee"] = True
    r = await appeler_outil(1500.0)
    assert r.get("is_error") is True and json.loads(r["content"][0]["text"])["reessayable"] is False, \
        "outil : au-delà du seuil -> refus non réessayable"; n += 1

    for invalide in (-50.0, 0, "1500"):
        assert (await appeler_outil(invalide)).get("is_error") is True, f"outil : montant invalide {invalide!r}"
    n += 1

    r = await appeler_outil(200.0)
    assert not r.get("is_error") and "effectué" in r["content"][0]["text"], "outil : cas nominal"; n += 1

    print(f"OK : {n} tests passés (hook + outil)")


asyncio.run(main())
