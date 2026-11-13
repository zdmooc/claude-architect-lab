"""M7 · L3 — Mesurer l'exactitude PAR CHAMP et PAR TYPE de document, et conserver les contradictions."""
from collections import defaultdict

# Jeu ANNOTÉ (vérité terrain) vs extractions du modèle (fictives).
VERITE = {
    "F001": {"type": "facture", "montant_ttc": 2880.0, "date": "2026-10-15"},
    "F002": {"type": "facture", "montant_ttc": 360.0, "date": "2026-11-02"},
    "D001": {"type": "declaration", "montant_ttc": 1200.0, "date": "2026-09-30"},
    "D002": {"type": "declaration", "montant_ttc": 640.0, "date": "2026-10-01"},
}
EXTRAIT = {
    "F001": {"montant_ttc": 2880.0, "date": "2026-10-15"},
    "F002": {"montant_ttc": 360.0, "date": "2026-11-02"},
    "D001": {"montant_ttc": 1200.0, "date": "2026-03-09"},   # erreur de date
    "D002": {"montant_ttc": 460.0, "date": "2026-10-01"},    # erreur de montant
}


def exactitude():
    stats = defaultdict(lambda: [0, 0])                     # (type, champ) -> [justes, total]
    for doc, v in VERITE.items():
        for champ in ("montant_ttc", "date"):
            cle = (v["type"], champ)
            stats[cle][1] += 1
            stats[cle][0] += EXTRAIT[doc][champ] == v[champ]
    return {f"{t}/{c}": f"{j}/{n}" for (t, c), (j, n) in sorted(stats.items())}


# Provenance : on CONSERVE les deux valeurs contradictoires, attribuées.
# ATTENTION : valeurs et sources FICTIVES, pour l exercice (pas des dates de support réelles).
AFFIRMATIONS = [
    {"affirmation": "Fin du support WebSphere 8.5", "valeur": "2030", "source": "note fournisseur A", "date_source": "2025-06"},
    {"affirmation": "Fin du support WebSphere 8.5", "valeur": "2028", "source": "article B", "date_source": "2024-02"},
]


def contradictions(affs):
    par_sujet = defaultdict(list)
    for a in affs:
        par_sujet[a["affirmation"]].append(a)
    return {s: l for s, l in par_sujet.items() if len({a["valeur"] for a in l}) > 1}


if __name__ == "__main__":
    print("Exactitude par type/champ :", exactitude())
    print("Global :", sum(e[c] == v[c] for d, v in VERITE.items() for e in [EXTRAIT[d]] for c in ("montant_ttc", "date")), "/ 8")
    for sujet, l in contradictions(AFFIRMATIONS).items():
        print("CONTRADICTION :", sujet, [(a["valeur"], a["source"], a["date_source"]) for a in l])
