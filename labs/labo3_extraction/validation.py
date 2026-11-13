"""Validation MÉTIER — distincte de la validation de STRUCTURE.

Le schéma garantit un JSON bien formé. Il ne garantit pas que les chiffres sont cohérents.
Chaque règle renvoie un message PRÉCIS, réutilisable pour une relance ciblée.
"""
from datetime import date
from typing import List

from schema import Facture


def valider(f: Facture) -> List[str]:
    erreurs: List[str] = []

    if None not in (f.montant_ht, f.montant_tva, f.montant_ttc):
        if abs(f.montant_ht + f.montant_tva - f.montant_ttc) > 0.02:
            erreurs.append(
                f"Incohérence : montant_ht ({f.montant_ht}) + montant_tva ({f.montant_tva}) "
                f"≠ montant_ttc ({f.montant_ttc}). Relis les montants dans la facture."
            )

    if f.date_facture:
        try:
            if date.fromisoformat(f.date_facture) > date.today():
                erreurs.append(f"date_facture {f.date_facture} est dans le futur.")
        except ValueError:
            erreurs.append(f"date_facture '{f.date_facture}' n'est pas au format AAAA-MM-JJ.")

    if f.categorie == "autre" and not f.categorie_precision:
        erreurs.append("categorie vaut 'autre' : renseigne categorie_precision.")
    if f.categorie != "autre" and f.categorie_precision:
        erreurs.append("categorie_precision ne doit être rempli que si categorie vaut 'autre'.")

    return erreurs
