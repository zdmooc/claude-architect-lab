# A2 — Workflow Integration and Solution Design (16 %)

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

## Exercice

Une équipe copie-colle 100 mails clients chaque jour dans un chat personnel. Dessiner un futur parcours où les informations sensibles sont préalablement filtrées, les demandes classées, les réponses **proposées** puis validées par un gestionnaire. **Corrigé** : conserver traçabilité et approbation, mesurer corrections, prévoir un canal de traitement manuel quand Claude est indisponible.

**À produire** : carte de processus avec décision, responsable, système source et chemin d'erreur par étape. Voir [cas ConseilNova](../cas-conseilnova.md).
