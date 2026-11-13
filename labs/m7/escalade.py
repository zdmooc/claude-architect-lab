"""M7 · L2 — Déclencheurs d'escalade EXPLICITES et transfert structuré (hors API, exécutable)."""
from dataclasses import asdict, dataclass, field
from typing import List

MOTS_HUMAIN = ("conseiller", "humain", "quelqu'un", "parler à une personne")


@dataclass
class Transfert:
    client_id: str
    faits: dict
    cause: str
    action_proposee: str
    tentatives: List[str] = field(default_factory=list)
    points_non_resolus: List[str] = field(default_factory=list)


def doit_escalader(message_client: str, montant: float, echecs_outil: int) -> str | None:
    """Renvoie la CAUSE d'escalade, ou None. Règles explicites, testables, pas un 'score de confiance'."""
    if any(m in message_client.lower() for m in MOTS_HUMAIN):
        return "demande explicite d'un humain"          # on respecte la demande, sans insister
    if montant > 1000:
        return "montant au-delà du seuil d'autonomie"
    if echecs_outil >= 2:
        return "échecs répétés d'un outil"
    return None


if __name__ == "__main__":
    cas = [("Je veux parler à un conseiller.", 50, 0), ("Remboursez 1500 €", 1500, 0),
           ("Où en est mon dossier ?", 0, 2), ("Où en est mon dossier ?", 0, 0)]
    for msg, m, e in cas:
        print(f"{msg!r:40} -> {doit_escalader(msg, m, e)}")
    t = Transfert("C-1001", {"contrat": "AUTO-4471"}, "montant au-delà du seuil d'autonomie",
                  "valider le remboursement de 1500 €", ["vérification identité OK"], ["justificatif non reçu"])
    print(asdict(t))
