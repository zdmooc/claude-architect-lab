---
name: revue-architecture
description: Revue d'architecture d'un module Python du projet devis (couplage, testabilité, configuration). À utiliser quand on demande une revue d'architecture ou de conception.
argument-hint: "[chemin du module]"
allowed-tools: Read, Grep, Glob
context: fork
---
# Revue d'architecture

Analyse le module indiqué en argument (par défaut `src/`) **en lecture seule**.

Points à vérifier :
1. Séparation calcul / barème / entrée-sortie.
2. Testabilité : les fonctions pures sont-elles isolées ?
3. Configuration : aucun secret ni taux en dur.

Rends : un tableau `point | constat | recommandation`, puis 3 actions priorisées.
