"""Tests locaux outils métier, sans requêtes Claude."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "labs" / "m3"))
import outils_contrats as o


def test_recherche_vide_est_un_succes(monkeypatch):
    monkeypatch.setattr(o, "TAUX_PANNE", 0.0)
    r = o.executer("rechercher_client", {"nom": "INCONNU"})
    assert r["is_error"] is False
    assert json.loads(r["content"])["nombre"] == 0


def test_contrat_inexistant_erreur_metier(monkeypatch):
    monkeypatch.setattr(o, "TAUX_PANNE", 0.0)
    r = o.executer("consulter_contrat", {"numero": "AUTO-9999"})
    assert r["is_error"] is True
    err = json.loads(r["content"])
    assert err["categorie"] == "introuvable" and err["reessayable"] is False


def test_erreur_temporaire_reessayable(monkeypatch):
    monkeypatch.setattr(o, "TAUX_PANNE", 1.0)
    r = o.executer("consulter_contrat", {"numero": "AUTO-4471"})
    assert r["is_error"] is True
    err = json.loads(r["content"])
    assert err["categorie"] == "transitoire" and err["reessayable"] is True


def test_contrat_sans_sinistre_nest_pas_une_panne(monkeypatch):
    monkeypatch.setattr(o, "TAUX_PANNE", 0.0)
    r = o.executer("lister_sinistres", {"numero": "HAB-2210"})
    assert r["is_error"] is False
    assert json.loads(r["content"])["sinistres"] == []
