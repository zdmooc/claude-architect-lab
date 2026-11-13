"""Tests hors API des règles de remboursement synthétiques."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "labs" / "labo1_support"))
from politique import autoriser_operation


def decision(**changes):
    valeurs = {
        "identite_verifiee": True,
        "contrat": "AUTO-4471",
        "contrats_autorises": {"AUTO-4471"},
        "montant": 800.0,
    }
    valeurs.update(changes)
    return autoriser_operation(**valeurs)


def test_limite_exacte_autorisee():
    assert decision().autorise


def test_limite_depassee_refusee():
    r = decision(montant=800.01)
    assert not r.autorise and r.code == "SEUIL"


def test_identite_absente_fail_closed():
    assert decision(identite_verifiee=False).code == "IDENTITE"


def test_contrat_autre_client_interdit():
    assert decision(contrat="AUTO-9999").code == "AUTORISATION"


def test_aucun_contrat_autorise():
    assert decision(contrats_autorises=set()).code == "AUTORISATION"


def test_montants_invalides_rejetes():
    for montant in [-1, 0, float("nan"), float("inf"), True, None, "800"]:
        r = decision(montant=montant)
        assert not r.autorise and r.code == "MONTANT_INVALIDE"
