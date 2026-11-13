"""M7 · L1 — Préserver les faits critiques et réduire les sorties d'outils (hors API, exécutable)."""
import json

# 1) Bloc de FAITS STRUCTURÉS, renvoyé à chaque tour au lieu de compter sur de vieux messages.
FAITS = {
    "client_id": "C-1001",
    "contrat": "AUTO-4471",
    "sinistre": {"date": "2026-11-03", "nature": "bris de glace", "montant_estime": 420.0},
    "attente_client": "réparation avant le 20/11",
}


def bloc_faits(faits: dict) -> str:
    """Rendu stable, placé EN TÊTE du message pour qu'il ne soit pas noyé."""
    return "<faits_dossier>\n" + json.dumps(faits, ensure_ascii=False, indent=2) + "\n</faits_dossier>"


# 2) RÉDUIRE la sortie d'un outil aux champs utiles avant de la donner au modèle.
REPONSE_BRUTE_REFERENTIEL = {
    "contrat": "AUTO-4471", "statut": "actif", "franchise": 300,
    "historique_technique": ["...200 lignes de journaux..."], "metadonnees_internes": {"shard": 7, "etag": "x9"},
    "iban": "FR76 3000 1007 9412 3456 7890 185",
}
CHAMPS_UTILES = ("contrat", "statut", "franchise")


def reduire(sortie: dict, champs=CHAMPS_UTILES) -> dict:
    return {k: sortie[k] for k in champs if k in sortie}


if __name__ == "__main__":
    print(bloc_faits(FAITS))
    avant, apres = len(json.dumps(REPONSE_BRUTE_REFERENTIEL)), len(json.dumps(reduire(REPONSE_BRUTE_REFERENTIEL)))
    print(f"Sortie d'outil : {avant} -> {apres} caractères ; IBAN retiré : {'iban' not in reduire(REPONSE_BRUTE_REFERENTIEL)}")
