"""Tests HORS API de la validation métier (labo 3) : python -m pytest labs/labo3_extraction"""
from schema import Facture
from validation import valider

BASE = dict(numero_facture="F-1", fournisseur="Fournisseur fictif", date_facture="2026-10-15",
            categorie="informatique", categorie_precision=None, montant_ht=2400.0,
            montant_tva=480.0, montant_ttc=2880.0, devise="EUR", ambiguites=[])


def f(**kw):
    return Facture(**{**BASE, **kw})


def test_facture_coherente():
    assert valider(f()) == []


def test_ht_plus_tva_different_du_ttc():
    erreurs = valider(f(montant_ttc=2900.0))
    assert len(erreurs) == 1 and "Incohérence" in erreurs[0]


def test_tolerance_arrondi():
    assert valider(f(montant_ttc=2880.02)) == []


def test_montant_absent_pas_de_controle_de_somme():
    assert valider(f(montant_ht=None)) == []


def test_date_future_et_format():
    assert "futur" in valider(f(date_facture="2999-01-01"))[0]
    assert "format" in valider(f(date_facture="15/10/2026"))[0]


def test_regle_categorie_autre():
    assert valider(f(categorie="autre")) != []
    assert valider(f(categorie="autre", categorie_precision="espaces verts")) == []
    assert valider(f(categorie_precision="inutile")) != []
