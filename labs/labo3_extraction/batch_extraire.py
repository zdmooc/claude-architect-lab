"""Labo 3 — Extraction en BATCH (Message Batches) avec custom_id et reprise sélective.

Code PROPOSÉ, imports vérifiés contre le SDK `anthropic` 2.8.0, compilé,
NON EXÉCUTÉ contre l'API par le formateur.

Batch = asynchrone (souvent < 1 h, jusqu'à 24 h), environ 50 % moins cher.
-> adapté au traitement de nuit, PAS à un contrôle bloquant.
"""
import json
import time
from pathlib import Path

import anthropic
from anthropic import transform_schema
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request

from prompt import SYSTEM
from schema import Facture
from validation import valider

MODEL = "claude-opus-5-5"
client = anthropic.Anthropic()

# transform_schema adapte le schéma Pydantic aux exigences de l'API
# (ex. additionalProperties: false). Vérifié sur anthropic 2.8.0.
SCHEMA = transform_schema(Facture)


def requete(custom_id: str, texte: str) -> Request:
    return Request(
        custom_id=custom_id,            # clé de corrélation : nom du fichier
        params=MessageCreateParamsNonStreaming(
            model=MODEL,
            max_tokens=2000,
            system=SYSTEM,
            messages=[{"role": "user", "content": f"<document>\n{texte}\n</document>"}],
            output_config={"format": {"type": "json_schema", "schema": SCHEMA}},
        ),
    )


def lancer(fichiers):
    batch = client.messages.batches.create(
        requests=[requete(f.stem, f.read_text(encoding="utf-8")) for f in fichiers]
    )
    print("Batch :", batch.id)
    while client.messages.batches.retrieve(batch.id).processing_status != "ended":
        time.sleep(60)
    return batch.id


def collecter(batch_id):
    ok, a_reprendre, revue_humaine = {}, [], []
    # Les résultats arrivent dans N'IMPORTE QUEL ordre : on indexe par custom_id.
    for r in client.messages.batches.results(batch_id):
        if r.result.type != "succeeded":
            a_reprendre.append(r.custom_id)           # erreur / expiration -> reprise
            continue
        texte = next(b.text for b in r.result.message.content if b.type == "text")
        facture = Facture.model_validate(json.loads(texte))
        erreurs = valider(facture)
        if erreurs:
            revue_humaine.append((r.custom_id, erreurs))
        else:
            ok[r.custom_id] = facture
    return ok, a_reprendre, revue_humaine


if __name__ == "__main__":
    fichiers = sorted(Path("corpus").glob("*.txt"))
    ok, a_reprendre, revue = collecter(lancer(fichiers))
    print(f"OK : {len(ok)} | à reprendre : {a_reprendre} | revue humaine : {revue}")
    # Reprise SÉLECTIVE : on ne relance QUE les documents en échec technique.
    if a_reprendre:
        print("Relance de :", a_reprendre)
        lancer([f for f in fichiers if f.stem in a_reprendre])
