"""Labo 3 — Schéma d'extraction de factures fournisseurs (données SYNTHÉTIQUES).

Choix de conception (D4) :
- champs NULLABLES quand l'information peut manquer dans la source
  -> le modèle peut répondre `null` au lieu d'inventer ;
- catégorie fermée + valeur "autre" + champ de précision -> catégorie extensible ;
- champ `ambiguites` pour signaler ce qui est incertain plutôt que de trancher en silence.
"""
from typing import List, Literal, Optional

from pydantic import BaseModel


class Facture(BaseModel):
    numero_facture: Optional[str]
    fournisseur: str
    date_facture: Optional[str]          # format AAAA-MM-JJ, null si absente
    categorie: Literal["informatique", "telecom", "locaux", "conseil", "autre"]
    categorie_precision: Optional[str]   # rempli seulement si categorie == "autre"
    montant_ht: Optional[float]
    montant_tva: Optional[float]
    montant_ttc: Optional[float]
    devise: Optional[str]                # code ISO, ex. "EUR"
    ambiguites: List[str]                # ce qui est incertain dans la source
