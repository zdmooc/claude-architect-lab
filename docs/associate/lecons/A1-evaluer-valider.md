# A1 — Output Evaluation and Validation (21 %)

> **Source des objectifs** : guide officiel CCAO-F v1.0 (juillet 2026), §6, Domain 2. Cours, exemples et questions **originaux**. Fil rouge : [cas ConseilNova](../cas-conseilnova.md) (fictif).

## Objectifs officiels
- évaluer l'exactitude et la complétude des réponses ;
- repérer hallucinations, incohérences et biais ;
- vérifier les faits et valider ;
- décider quand une revue humaine est nécessaire ;
- éditer, affiner et comparer les sorties selon le public ;
- organiser l'information et choisir le format (artifact, réponse dans le fil, données structurées).

**Prérequis** : aucun prérequis de programmation.

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

## Exercice guidé

Livrable : une proposition contenant 3 chiffres, 2 citations et 1 échéance. Établir une grille avec colonnes **assertion / source / vérification / verdict / correctif**. Exemple : « 27 % d'économie » / aucune mesure / non vérifiable / **échec** / demander le calcul. **Correction** : une proposition peut être retournée pour révision même si le style est bon.

## Pièges d'examen

- « Claude l'a dit avec assurance » n'est pas une preuve.
- Le format JSON valide n'implique pas que la valeur soit vraie.
- Faire réécrire un chiffre sans source n'est pas une validation.
- L'accord humain doit être réel, informé et enregistré.

**À produire** : [grille de validation](../grille-validation.md) renseignée sur le [cas ConseilNova](../cas-conseilnova.md).

## Exercice à toi
- **E1.** Une synthèse de Claude cite « selon l'étude Gartner 2025, 62 % des PME… » sans lien. Que fais-tu avant diffusion ?
- **E2.** Pour chacun, revue humaine obligatoire ou non : (a) brouillon de note interne de brainstorming ; (b) courrier de refus envoyé à un client ; (c) tableau de chiffres pour un comité financier.
- **E3.** Quel format de sortie choisis-tu pour : (a) un tableau comparatif à réutiliser dans Excel ; (b) un document de 5 pages à itérer ; (c) une réponse rapide à une question ?

## Correction
<details><summary>Voir la correction</summary>

- **E1.** Retrouver la source primaire ; si elle est introuvable ou différente, **retirer** le chiffre ou le marquer « non vérifié » ; ne jamais diffuser une statistique sans source vérifiée.
- **E2.** (a) Non (faible impact, usage interne). (b) **Oui** (impact client et juridique). (c) **Oui** (décision financière ; chiffres rapprochés de la source de vérité).
- **E3.** (a) **Données structurées** (CSV/tableau). (b) **Artifact** (document éditable à part). (c) **Réponse dans le fil**.
</details>

## Questions d'entraînement (originales)
**Q1.** Une réponse est bien rédigée, assurée, mais un chiffre ne figure dans aucune source fournie. C'est :
A. Acceptable si le style est bon · B. Une hallucination probable : vérifier ou retirer · C. Une preuve de qualité · D. Un problème de format

**Q2.** (2 réponses) Situations qui exigent une revue humaine :
A. Communication externe engageante · B. Liste d'idées pour un atelier interne · C. Chiffres pour une décision financière · D. Reformulation d'un mail personnel

<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | Plausible ≠ vrai. |
| Q2 | **A, C** | Impact externe ou financier. |
</details>

## À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Cinq vérifications : exactitude, complétude, pertinence, conformité, traçabilité.
- Hallucination, incohérence, biais : vérifier contre la source, pas contre l'assurance du texte.
- Revue humaine proportionnée à l'impact.
- Format adapté : artifact, dans le fil, données structurées.
</details>
