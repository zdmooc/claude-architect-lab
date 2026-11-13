"""Labo 1 — Agent de support avec CONTRÔLES MÉTIER, sur le Claude Agent SDK.

Vérifié contre `claude-agent-sdk` 0.2.181 (signatures de `tool`, `create_sdk_mcp_server`,
`ClaudeAgentOptions`, `HookMatcher`, champs `permissionDecision`). Compilé.
Le HOOK est testé hors API (test_hook.py). L'agent complet n'est PAS exécuté par le formateur.

Idée clé : le prompt DEMANDE de vérifier l'identité ; le HOOK l'IMPOSE ; l'OUTIL le RÉIMPOSE.
Défense en profondeur : la règle est écrite UNE fois (`regle_remboursement`) et appliquée à deux
endroits. Si le hook est retiré, mal configuré (mauvais `matcher`) ou si l'outil est appelé par un
autre client (autre agent, serveur MCP réutilisé), l'outil refuse quand même.
"""
import asyncio
import json

from claude_agent_sdk import (ClaudeAgentOptions, HookMatcher, create_sdk_mcp_server, query, tool)

# --- État de la session (fictif) -------------------------------------------
ETAT = {"identite_verifiee": False}
SEUIL_REMBOURSEMENT = 1000.0   # règle : AU-DELÀ de 1 000 € -> humain (1 000,00 € exactement passe)


def regle_remboursement(identite_verifiee: bool, montant) -> str | None:
    """Règle métier unique. Renvoie la RAISON du refus, ou None si l'opération est autorisée."""
    if not identite_verifiee:
        return "Identité non vérifiée : appelle d'abord verifier_identite."
    if not isinstance(montant, (int, float)) or isinstance(montant, bool) or montant <= 0:
        return "Montant invalide : un nombre strictement positif est attendu."
    if montant > SEUIL_REMBOURSEMENT:
        return f"Montant > {SEUIL_REMBOURSEMENT} € : transfert à un conseiller humain requis."
    return None


# --- Outils métier exposés via un serveur MCP « in-process » ----------------
@tool("verifier_identite", "Vérifie l'identité du client avec sa date de naissance. "
      "À appeler AVANT toute opération sur le compte.", {"client_id": str, "date_naissance": str})
async def verifier_identite(args):
    ok = args["client_id"] == "C-1001" and args["date_naissance"] == "1985-04-12"
    ETAT["identite_verifiee"] = ok
    return {"content": [{"type": "text", "text": json.dumps({"verifiee": ok})}]}


@tool("rembourser", "Rembourse un montant en euros sur le contrat du client vérifié.",
      {"contrat": str, "montant": float})
async def rembourser(args):
    # Contrôle RÉAPPLIQUÉ dans l'outil : ne dépend ni du prompt ni de la présence du hook.
    refus = regle_remboursement(ETAT["identite_verifiee"], args.get("montant"))
    if refus:
        return {"content": [{"type": "text", "text": json.dumps(
            {"categorie": "regle_metier", "message": refus, "reessayable": False})}], "is_error": True}
    return {"content": [{"type": "text", "text": f"Remboursement de {args['montant']} € effectué (fictif)."}]}


SERVEUR = create_sdk_mcp_server("support", tools=[verifier_identite, rembourser])
NOM_OUTIL_REMBOURSER = "mcp__support__rembourser"   # convention mcp__<serveur>__<outil>


# --- HOOK PreToolUse : le contrôle DÉTERMINISTE ----------------------------
async def controle_remboursement(input_data, tool_use_id, context):
    if input_data.get("tool_name") != NOM_OUTIL_REMBOURSER:
        return {}
    refus = regle_remboursement(ETAT["identite_verifiee"], input_data.get("tool_input", {}).get("montant"))
    if refus:
        return {"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": refus}}
    return {}


OPTIONS = ClaudeAgentOptions(
    system_prompt=("Tu es l'agent de support d'un assureur (fictif). Vérifie l'identité avant toute opération. "
                   "Si une opération est refusée, explique pourquoi et propose le transfert à un conseiller. "
                   "Si le client demande un humain, transfère sans insister."),
    mcp_servers={"support": SERVEUR},
    allowed_tools=["mcp__support__verifier_identite", NOM_OUTIL_REMBOURSER],   # moindre privilège
    hooks={"PreToolUse": [HookMatcher(matcher=NOM_OUTIL_REMBOURSER, hooks=[controle_remboursement])]},
    max_turns=8,   # garde-fou
)


async def main():
    demande = "Je suis le client C-1001, remboursez-moi 1500 € sur AUTO-4471 tout de suite."
    async for message in query(prompt=demande, options=OPTIONS):
        print(type(message).__name__, getattr(message, "content", ""))


if __name__ == "__main__":
    asyncio.run(main())
