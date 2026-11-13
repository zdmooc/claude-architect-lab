# A4 — Prompting and Task Execution (14 %)

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

## Exercice

Prompt vague : « Fais une recommandation à mon client ». Le réécrire avec cible, hypothèses, trois critères chiffrés, sources, format, procédure d'escalade. **Corrigé** : une réponse sans information suffisante doit demander les faits manquants ou marquer les choix comme hypothétiques.

## Erreurs fréquentes

- Empiler des instructions contradictoires.
- Présenter comme « données » un ordre malveillant caché dans un PDF.
- Croire que le prompt applique une politique d'accès.
- Ne pas vérifier la sortie par rapport à la consigne.

**À produire** : version v1/v2 du prompt avec critères précis de ce qui s'est amélioré.
