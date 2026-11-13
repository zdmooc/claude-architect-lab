"""M3 — Outils métier FICTIFS d'un assureur (données synthétiques).

Ce module ne dépend PAS de l'API : on peut le tester sans clé.
Il illustre trois notions D2 :
- descriptions qui DISTINGUENT des outils proches ;
- erreurs STRUCTURÉES (catégorie, retry possible ou non) ;
- « aucun résultat » ≠ « échec d'accès ».
"""
import json
import random

CLIENTS = {
    "C-1001": {"nom": "Durand", "prenom": "Alice", "ville": "Lyon"},
    "C-1002": {"nom": "Martin", "prenom": "Karim", "ville": "Nantes"},
}
CONTRATS = {
    "AUTO-4471": {"client": "C-1001", "type": "auto", "franchise": 300, "statut": "actif"},
    "HAB-2210": {"client": "C-1002", "type": "habitation", "franchise": 150, "statut": "résilié"},
}
SINISTRES = {
    "AUTO-4471": [{"id": "S-88", "date": "2026-11-03", "nature": "bris de glace", "statut": "expertise"}],
    "HAB-2210": [],
}

# Probabilité d'une panne simulée du référentiel (pour tester la gestion d'erreur).
TAUX_PANNE = 0.0

TOOLS = [
    {
        "name": "rechercher_client",
        "description": (
            "Recherche des CLIENTS par nom de famille (recherche exacte, insensible à la casse). "
            "Utilise cet outil quand tu as un nom mais pas d'identifiant client. "
            "Renvoie une liste (éventuellement vide) de clients {id, nom, prenom, ville}. "
            "Ne renvoie PAS de contrats : pour un contrat, utilise consulter_contrat."
        ),
        "input_schema": {
            "type": "object",
            "properties": {"nom": {"type": "string", "description": "Nom de famille, ex. 'Durand'"}},
            "required": ["nom"],
            "additionalProperties": False,
        },
    },
    {
        "name": "consulter_contrat",
        "description": (
            "Lit le détail d'UN contrat à partir de son numéro exact (ex. 'AUTO-4471'). "
            "Renvoie type, franchise, statut et identifiant client. "
            "Ne liste pas les sinistres : pour cela, utilise lister_sinistres."
        ),
        "input_schema": {
            "type": "object",
            "properties": {"numero": {"type": "string", "description": "Numéro de contrat, ex. 'AUTO-4471'"}},
            "required": ["numero"],
            "additionalProperties": False,
        },
    },
    {
        "name": "lister_sinistres",
        "description": (
            "Liste les sinistres déclarés sur UN contrat (numéro exact). "
            "Une liste vide signifie qu'aucun sinistre n'est déclaré sur ce contrat."
        ),
        "input_schema": {
            "type": "object",
            "properties": {"numero": {"type": "string"}},
            "required": ["numero"],
            "additionalProperties": False,
        },
    },
]


def _erreur(categorie: str, message: str, reessayable: bool) -> dict:
    """Erreur STRUCTURÉE : le modèle (et le code) savent quoi faire ensuite."""
    return {"is_error": True, "content": json.dumps(
        {"categorie": categorie, "message": message, "reessayable": reessayable}, ensure_ascii=False)}


def _ok(donnees) -> dict:
    return {"is_error": False, "content": json.dumps(donnees, ensure_ascii=False)}


def executer(nom: str, entree: dict) -> dict:
    """Exécute un outil et renvoie {'is_error': bool, 'content': str}."""
    if random.random() < TAUX_PANNE:
        return _erreur("transitoire", "Référentiel indisponible (timeout).", reessayable=True)

    if nom == "rechercher_client":
        trouves = [{"id": k, **v} for k, v in CLIENTS.items() if v["nom"].lower() == entree["nom"].lower()]
        return _ok({"clients": trouves, "nombre": len(trouves)})   # liste vide = SUCCÈS, pas une erreur

    if nom == "consulter_contrat":
        contrat = CONTRATS.get(entree["numero"])
        if contrat is None:
            return _erreur("introuvable", f"Aucun contrat {entree['numero']}. Vérifie le numéro.", reessayable=False)
        return _ok({"numero": entree["numero"], **contrat})

    if nom == "lister_sinistres":
        if entree["numero"] not in CONTRATS:
            return _erreur("introuvable", f"Aucun contrat {entree['numero']}.", reessayable=False)
        return _ok({"sinistres": SINISTRES.get(entree["numero"], [])})

    return _erreur("validation", f"Outil inconnu : {nom}", reessayable=False)
