# A2 — Workflow Integration and Solution Design (16 %)

> **Source des objectifs** : guide officiel CCAO-F v1.0 (juillet 2026), §6, Domain 4. Cours, exemples et questions **originaux**. Fil rouge : [cas ConseilNova](../cas-conseilnova.md) (fictif).

## Objectifs officiels
- analyser besoins et cas d'usage ;
- utiliser Claude pour la recherche, la planification et l'optimisation de processus ;
- soutenir la conception de solution et l'itération ;
- intégrer Claude dans les flux de travail ;
- communiquer valeur et limites aux parties prenantes.

**Prérequis** : aucun prérequis de programmation.

**Compétence** : intégrer Claude à un **processus métier**, avec des étapes humaines et des contrôles, plutôt que multiplier des conversations isolées.

## Méthode

1. Cartographier **AS-IS** : déclencheur, acteurs, entrées, règles, livrables, systèmes, exceptions.
2. Identifier les tâches utiles à confier à Claude : résumé, rédaction, classement, exploration d'options, extraction ; laisser les **décisions réglementées** et les validations aux personnes/systèmes autorisés.
3. Concevoir le **TO-BE** : qui déclenche, données autorisées, prompts standard, sources, format, approbation, archivage, incidents et reprise manuelle.
4. Définir un KPI avec baseline (minutes par dossier, taux de retouche, erreurs, satisfaction) ; un « gain » supposé n'est pas un gain démontré.
5. Rédiger un mode opératoire compréhensible par une personne qui n'a pas participé au pilote.

### Trois options courantes

| Option | Convient à | Attention |
|---|---|---|
| Chat ponctuel | tâche individuelle, faible risque | historique et vérification manuelle |
| Project avec connaissances | répétition par équipe avec sources stables | droits, actualisation et version |
| Workflow intégré / automatisation | volume et contrôles stables | responsabilités, erreurs et escalades |

## Exercice guidé

Une équipe copie-colle 100 mails clients chaque jour dans un chat personnel. Dessiner un futur parcours où les informations sensibles sont préalablement filtrées, les demandes classées, les réponses **proposées** puis validées par un gestionnaire. **Corrigé** : conserver traçabilité et approbation, mesurer corrections, prévoir un canal de traitement manuel quand Claude est indisponible.

**À produire** : carte de processus avec décision, responsable, système source et chemin d'erreur par étape. Voir [cas ConseilNova](../cas-conseilnova.md).

## Exercice à toi
- **E1.** Cartographie AS-IS → TO-BE en 5 étapes pour « répondre aux demandes de devis entrantes ». Indique où intervient Claude et où intervient l'humain.
- **E2.** Le sponsor annonce « 30 % de gain de temps ». Comment le transformes-tu en engagement mesurable ?
- **E3.** Rédige 3 phrases pour expliquer à un directeur ce que Claude **ne fera pas** dans ce projet.

## Correction
<details><summary>Voir la correction</summary>

- **E1.** 1. Réception (formulaire) → 2. Classement et extraction des besoins (**Claude**) → 3. Vérification des prix dans le catalogue (**système de référence**) → 4. Brouillon de devis (**Claude**) → 5. Validation et envoi (**commercial**). Chemin d'erreur : demande incomplète → question au client.
- **E2.** Mesurer une **baseline** (minutes par devis sur 2 semaines), définir la méthode de mesure après pilote, comparer à périmètre égal, inclure le temps de relecture ; annoncer un objectif, pas un résultat.
- **E3.** « Claude ne fixera aucun prix : les prix viennent du catalogue. Claude n'enverra rien à un client sans validation d'un commercial. Claude n'aura pas accès aux données d'autres clients. »
</details>

## Questions d'entraînement (originales)
**Q1.** Avant d'intégrer Claude dans un processus, première étape ?
A. Choisir le modèle · B. Cartographier le processus actuel et la baseline · C. Écrire le prompt · D. Acheter des licences

**Q2.** (2 réponses) Bonnes façons de présenter la valeur :
A. Gain mesuré contre une baseline · B. « Claude ne se trompe jamais » · C. Limites et contrôles explicités · D. Promesse de 100 % d'automatisation

<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | Comprendre avant d'outiller. |
| Q2 | **A, C** | Honnêteté et mesure. |
</details>

## À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- AS-IS → TO-BE ; Claude pour lire, rédiger, classer ; humains et systèmes pour décider.
- KPI avec baseline ; un gain supposé n'est pas démontré.
- Mode opératoire, chemin d'erreur, repli manuel.
- Communiquer valeur **et** limites.
</details>
