"""M3 · L1 — Boucle agentique MANUELLE.

Code PROPOSÉ, suit la documentation du SDK `anthropic` (boucle manuelle, is_error),
compilé, NON EXÉCUTÉ contre l'API par le formateur.
Usage : python boucle_manuelle.py "Quels sinistres sur le contrat de Mme Durand ?"
"""
import sys

import anthropic

from outils_contrats import TOOLS, executer

MODEL = "claude-opus-5-5"   # ou "claude-haiku-5-5" (ton choix, moins cher)
MAX_TOURS = 10              # GARDE-FOU, pas condition d'arrêt normale

client = anthropic.Anthropic()
SYSTEM = ("Tu es un assistant de gestionnaire sinistres. Utilise les outils pour répondre. "
          "Si un outil renvoie une erreur non réessayable, explique-la au lieu d'inventer.")


def repondre(question: str) -> str:
    messages = [{"role": "user", "content": question}]

    for tour in range(MAX_TOURS):
        response = client.messages.create(
            model=MODEL, max_tokens=4000, system=SYSTEM, tools=TOOLS, messages=messages,
        )
        # 1) La condition d'arrêt NORMALE, c'est le stop_reason.
        if response.stop_reason == "end_turn":
            return "".join(b.text for b in response.content if b.type == "text")
        if response.stop_reason != "tool_use":
            return f"[arrêt inattendu : {response.stop_reason}]"

        # 2) On garde la réponse COMPLÈTE (avec ses blocs tool_use) dans l'historique.
        messages.append({"role": "assistant", "content": response.content})

        # 3) On exécute TOUS les appels demandés et on renvoie TOUS les résultats
        #    dans UN SEUL message user.
        resultats = []
        for bloc in response.content:
            if bloc.type != "tool_use":
                continue
            r = executer(bloc.name, bloc.input)
            print(f"  [outil] {bloc.name}({bloc.input}) -> erreur={r['is_error']}")
            resultats.append({
                "type": "tool_result",
                "tool_use_id": bloc.id,      # doit correspondre à l'id du tool_use
                "content": r["content"],
                "is_error": r["is_error"],
            })
        messages.append({"role": "user", "content": resultats})

    # 4) Le garde-fou s'est déclenché : c'est une anomalie à signaler, pas une fin normale.
    return "[garde-fou : trop d'itérations, escalade vers un humain]"


if __name__ == "__main__":
    print(repondre(sys.argv[1] if len(sys.argv) > 1 else "Quels sinistres sur le contrat de Mme Durand ?"))
