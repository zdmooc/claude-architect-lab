# A4 — Prompting and Task Execution (14 %)

> **Source des objectifs** : guide officiel CCAO-F v1.0 (juillet 2026), §6, Domain 1. Cours, exemples et questions **originaux**. Fil rouge : [cas ConseilNova](../cas-conseilnova.md) (fictif).

## Objectifs officiels
- créer des prompts efficaces pour des tâches métier et techniques ;
- décomposer les demandes complexes ;
- itérer sur les prompts ;
- adapter la stratégie au type de tâche (analyse, recherche, rédaction, brainstorming).

**Prérequis** : aucun prérequis de programmation.

**Compétence** : formuler une demande reproductible, guider une tâche en plusieurs étapes et vérifier que les consignes sont respectées.

## Gabarit pratique

> **Rôle** : tu prépares une synthèse pour un comité.
>
> **Objectif** : comparer les trois options du document fourni, sans ajouter de chiffres.
>
> **Contexte** : décideurs non techniques ; réunion demain ; source datée du 12 novembre.
>
> **Contraintes** : ne déduis ni prix, ni délai absents ; signale les hypothèses.
>
> **Format** : tableau option / bénéfice / coût prouvé / risque / question ouverte.
>
> **Vérification** : cite le titre et l'emplacement de chaque chiffre.

Techniques : zéro exemple pour tâche simple, **few-shot** (un ou deux exemples contrastés) pour un format répétitif ; décomposer tâche complexe (extraire → vérifier → synthétiser) ; contraindre longueur/ton ; demander la **liste des inconnues** au lieu de forcer une réponse.

Une phrase comme « fais mieux » est un feedback inutilisable : indiquer l'erreur, la source et le critère d'acceptation.

## Exercice guidé

Prompt vague : « Fais une recommandation à mon client ». Le réécrire avec cible, hypothèses, trois critères chiffrés, sources, format, procédure d'escalade. **Corrigé** : une réponse sans information suffisante doit demander les faits manquants ou marquer les choix comme hypothétiques.

## Erreurs fréquentes

- Empiler des instructions contradictoires.
- Présenter comme « données » un ordre malveillant caché dans un PDF.
- Croire que le prompt applique une politique d'accès.
- Ne pas vérifier la sortie par rapport à la consigne.

**À produire** : version v1/v2 du prompt avec critères précis de ce qui s'est amélioré.

## Exercice à toi
- **E1.** Réécris avec le gabarit (rôle, objectif, contexte, contraintes, format, vérification) : « Résume ce rapport. »
- **E2.** Décompose en étapes : « Prépare la réponse à l'appel d'offres à partir des 3 documents joints. »
- **E3.** Quelle différence de consigne entre une tâche de **brainstorming** et une tâche d'**analyse** ?

## Correction
<details><summary>Voir la correction</summary>

- **E1.** « Rôle : analyste pour un comité de direction. Objectif : résumer le rapport joint en 10 lignes. Contexte : lecteurs non techniques, décision la semaine prochaine. Contraintes : aucune information absente du rapport ; signaler les incertitudes. Format : 3 points clés, 2 risques, 1 recommandation. Vérification : indiquer la page de chaque chiffre. »
- **E2.** 1. Extraire les exigences de l'appel d'offres. 2. Associer chaque exigence aux éléments des documents. 3. Lister les manques. 4. Rédiger section par section. 5. Vérifier la couverture exigence par exigence.
- **E3.** Brainstorming : quantité, variété, pas de filtre précoce, ton ouvert. Analyse : critères explicites, sources citées, hypothèses signalées, conclusion argumentée.
</details>

## Questions d'entraînement (originales)
**Q1.** Claude ignore le format demandé. Premier geste ?
A. Répéter « respecte le format ! » · B. Donner un gabarit de sortie précis et un exemple · C. Changer d'outil · D. Abandonner

**Q2.** (2 réponses) Bonnes pratiques de prompt :
A. Préciser public et objectif · B. Empiler des consignes contradictoires · C. Demander de signaler ce qui manque · D. Dire seulement « fais mieux »

<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | Format explicite + exemple. |
| Q2 | **A, C** | B et D dégradent. |
</details>

## À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Gabarit : rôle, objectif, contexte, contraintes, format, vérification.
- Décomposer : extraire → vérifier → rédiger.
- Itérer avec un retour précis (erreur, source, critère).
- Adapter au type de tâche.
</details>
