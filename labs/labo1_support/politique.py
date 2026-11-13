"""Règles métier déterministes, indépendantes du modèle et du SDK.

Exemple SYNTHÉTIQUE. À placer dans un vrai service avec identité liée à la requête,
contrôles d'autorisation côté serveur, audit, persistance et tests d'intégration.
"""
from dataclasses import dataclass
from math import isfinite


SEUIL_EUROS = 800.0


@dataclass(frozen=True)
class Decision:
    autorise: bool
    code: str
    motif: str


def autoriser_operation(*, identite_verifiee: bool, contrat: str,
                        contrats_autorises: set[str], montant: float,
                        seuil: float = SEUIL_EUROS) -> Decision:
    """Vérifie identité, accès au contrat, montant et escalade.

    800,00 € accepté si toutes les autres conditions sont réunies,
    800,01 € refusé. La fonction n'effectue aucun mouvement d'argent.
    """
    if not identite_verifiee:
        return Decision(False, "IDENTITE", "Identité non vérifiée : conseiller requis.")
    if not contrat or contrat not in contrats_autorises:
        return Decision(False, "AUTORISATION", "Contrat non autorisé : conseiller requis.")
    if (isinstance(montant, bool) or not isinstance(montant, (int, float))
            or not isfinite(float(montant)) or montant <= 0):
        return Decision(False, "MONTANT_INVALIDE", "Montant absent ou invalide.")
    if montant > seuil:
        return Decision(False, "SEUIL", "Montant supérieur au seuil : transfert au conseiller.")
    return Decision(True, "OK", "Proposition autorisée pour ce contrat.")
