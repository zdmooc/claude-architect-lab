"""Labo 3 — Extraction SYNCHRONE avec validation métier et relance ciblée.

Code PROPOSÉ, vérifié contre le SDK `anthropic` 2.8.0 (signature de messages.parse),
compilé, NON EXÉCUTÉ contre l'API par le formateur.

Usage : python extraire.py corpus/F001.txt
"""
import sys
from pathlib import Path

import anthropic

from prompt import SYSTEM
from schema import Facture
from validation import valider

MODEL = "claude-opus-5-5"   # ou "claude-haiku-5-5" pour réduire les coûts (ton choix)
MAX_RELANCES = 1            # on ne réessaie pas indéfiniment

client = anthropic.Anthropic()


def extraire(texte: str) -> Facture:
    messages = [{"role": "user", "content": f"<document>\n{texte}\n</document>"}]

    for tentative in range(MAX_RELANCES + 1):
        response = client.messages.parse(
            model=MODEL,
            max_tokens=2000,
            system=SYSTEM,
            messages=messages,
            output_format=Facture,       # STRUCTURE garantie par le schéma
        )
        if response.stop_reason != "end_turn":
            raise RuntimeError(f"Arrêt inattendu : {response.stop_reason}")

        facture = response.parsed_output
        erreurs = valider(facture)       # SENS vérifié par le code métier
        if not erreurs:
            return facture

        print(f"[tentative {tentative + 1}] erreurs métier : {erreurs}")
        # Relance CIBLÉE : on renvoie la réponse précédente + les erreurs précises.
        messages.append({"role": "assistant", "content": response.content})
        messages.append({
            "role": "user",
            "content": "Ta réponse contient ces erreurs :\n- " + "\n- ".join(erreurs)
            + "\nCorrige uniquement ce qui est en erreur. Si l'information est absente "
              "du document, mets null et note-le dans ambiguites.",
        })

    # Échec persistant : on ne force pas, on envoie en revue humaine.
    facture.ambiguites.append("VALIDATION_ECHOUEE: " + " | ".join(erreurs))
    return facture


if __name__ == "__main__":
    chemin = Path(sys.argv[1])
    print(extraire(chemin.read_text(encoding="utf-8")).model_dump_json(indent=2))
