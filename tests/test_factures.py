"""Validation métier des factures, sans LLM ni réseau."""
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "labs" / "labo3_extraction"))
from schema import Facture
from validation import valider


def facture(**changes):
    donnees = dict(numero_facture="F-001", fournisseur="Garage fictif",
                   date_facture="2026-10-12", categorie="locaux",
                   categorie_precision=None, montant_ht=100.0,
                   montant_tva=20.0, montant_ttc=120.0,
                   devise="EUR", ambiguites=[])
    donnees.update(changes)
    return Facture(**donnees)


def test_facture_coherente():
    assert valider(facture()) == []


def test_ecart_ttc_signale():
    assert any("Incohérence" in x for x in valider(facture(montant_ttc=999)))


def test_champ_absent_reste_nullable():
    assert valider(facture(montant_ttc=None)) == []


def test_date_future_signalee():
    avenir = (date.today() + timedelta(days=1)).isoformat()
    assert any("futur" in x for x in valider(facture(date_facture=avenir)))


def test_date_invalide_signalee():
    assert any("format" in x for x in valider(facture(date_facture="demain")))


def test_categorie_autre_exige_precision():
    assert any("renseigne categorie_precision" in x
               for x in valider(facture(categorie="autre")))


def test_precision_interdite_si_categorie_standard():
    assert any("categorie_precision" in x
               for x in valider(facture(categorie="locaux", categorie_precision="n/a")))
