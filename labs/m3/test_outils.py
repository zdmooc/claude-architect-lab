"""Tests HORS API des outils (exécutables sans clé) : python test_outils.py"""
import json

import outils_contrats as o

r = o.executer("rechercher_client", {"nom": "Inconnu"})
assert r["is_error"] is False and json.loads(r["content"])["nombre"] == 0, "vide = succès"

r = o.executer("consulter_contrat", {"numero": "AUTO-9999"})
assert r["is_error"] is True and json.loads(r["content"])["reessayable"] is False, "introuvable"

r = o.executer("lister_sinistres", {"numero": "HAB-2210"})
assert r["is_error"] is False and json.loads(r["content"])["sinistres"] == [], "contrat sans sinistre"

o.TAUX_PANNE = 1.0
r = o.executer("consulter_contrat", {"numero": "AUTO-4471"})
assert r["is_error"] is True and json.loads(r["content"])["categorie"] == "transitoire"

print("OK : 4 tests passés")
