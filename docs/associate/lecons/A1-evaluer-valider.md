# A1 — Output Evaluation and Validation (21 %)

**Compétence** : décider si une réponse Claude est **réutilisable**, pas seulement « plausible » ou élégante. Domaine le plus important d'Associate.

## Cours

Une sortie peut être **correctement rédigée et factuellement fausse**. Séparer cinq vérifications :
1. **Exactitude** : chiffres, dates et citations contre documents de référence, vérifiables indépendamment.
2. **Complétude** : chaque demande est couverte ; signaler ce qui manque.
3. **Pertinence** : la réponse résout le besoin du bon destinataire ; pas de digressions.
4. **Conformité** : format, confidentialité, politique, droit d'auteur et ton adapté.
5. **Traçabilité** : source, version, date de consultation, auteur responsable et modifications humaines.

Créer une **rubrique de validation** avant d'exécuter un prompt. Une auto-évaluation par Claude peut aider à repérer une erreur, mais elle n'est pas une source indépendante et ne remplace jamais une vérification des informations sensibles. Différencier hallucination (fait inventé), omission, erreur arithmétique et donnée obsolète.

## Scénario ConseilNova

Un compte rendu d'appel affirme « économie client : 27 % », mais l'étude ne donne qu'un objectif de 15 %. **Ne pas diffuser** : trouver la source, remplacer la valeur ou signaler « non mesuré », inscrire une anomalie et refaire vérifier par la personne métier.

## Exercice guidé et corrigé

Livrable : une proposition contenant 3 chiffres, 2 citations et 1 échéance. Établir une grille avec colonnes **assertion / source / vérification / verdict / correctif**. Exemple : « 27 % d'économie » / aucune mesure / non vérifiable / **échec** / demander le calcul. **Correction** : une proposition peut être retournée pour révision même si le style est bon.

## Pièges d'examen

- « Claude l'a dit avec assurance » n'est pas une preuve.
- Le format JSON valide n'implique pas que la valeur soit vraie.
- Faire réécrire un chiffre sans source n'est pas une validation.
- L'accord humain doit être réel, informé et enregistré.

**À produire** : [grille de validation](../grille-validation.md) renseignée sur le [cas ConseilNova](../cas-conseilnova.md).
