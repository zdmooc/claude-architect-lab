# A6 — Configuration and Knowledge Management (12 %)

> **Source des objectifs** : guide officiel CCAO-F v1.0 (juillet 2026), §6, Domain 5. Cours, exemples et questions **originaux**. Fil rouge : [cas ConseilNova](../cas-conseilnova.md) (fictif).

## Objectifs officiels
- configurer des Projects avec instructions et sources de connaissance ;
- gérer les téléversements et les **connecteurs** (ex. Google Drive, Gmail) ;
- créer des instructions de niveau système ;
- maintenir les configurations dans le temps.

**Prérequis** : aucun prérequis de programmation.

**Compétence** : préparer un environnement Claude réutilisable et maintenir une connaissance fiable.

## Cours

Un Project utile comporte : **instructions partagées**, documents approuvés, taxonomie de fichiers, propriétaires, dates/version, règles de diffusion et méthode d'actualisation. Une base de connaissance périmée peut produire une réponse apparemment parfaite mais **fausse au jour de la demande**.

Distinguer :
- **Instructions** : rôle, format, limites, escalades ; ne sont pas des faits.
- **Connaissance** : sources vérifiables et horodatées, avec droits.
- **Contexte de session** : besoin et documents du dossier courant.
- **Mémoire / historique** : informations accumulées, qui peuvent être anciennes ou inadaptées ; ne pas les prendre comme source de vérité.

Planifier ajout, modification, retrait et purge des documents ; tester qu'une correction de procédure se retrouve dans les réponses. Réduire les données confidentielles partagées.

## Exercice guidé

La procédure SAV « retour sous 14 jours » est remplacée par « retour sous 30 jours ». Un Project continue à répondre 14 jours. **Corrigé** : identifier le document historique, retirer/remplacer, mettre à jour instructions si nécessaire, retester sur 3 cas, consigner la version et communiquer le changement aux utilisateurs.

**À produire** : registre document, owner, version, date de validité, restriction et date de prochaine revue.

## Exercice à toi
- **E1.** Rédige les instructions d'un Project « Support SAV ConseilNova » (5 lignes).
- **E2.** Connecteur Google Drive ou téléversement de fichiers : lequel pour (a) une procédure qui change chaque semaine ; (b) un PDF de référence stable ?
- **E3.** Propose un rythme et une méthode de maintenance du Project.

## Correction
<details><summary>Voir la correction</summary>

- **E1.** « Tu aides l'équipe SAV à rédiger des réponses. Utilise uniquement les procédures du Project (version indiquée). Si une information manque, dis-le et propose de transférer au superviseur. Ne copie aucune donnée identifiante. Format : réponse courte + procédure citée. »
- **E2.** (a) **Connecteur** (toujours la version à jour, sous réserve des droits). (b) **Téléversement** (stable, maîtrisé).
- **E3.** Propriétaire nommé ; revue mensuelle des documents (version, date de validité) ; retrait des obsolètes ; 3 cas de test rejoués après chaque modification ; journal des changements.
</details>

## Questions d'entraînement (originales)
**Q1.** Le Project répond avec une ancienne procédure. Cause la plus probable ?
A. Le modèle est trop petit · B. Document obsolète encore présent dans les connaissances · C. Prompt trop court · D. Panne

**Q2.** (2 réponses) Contenu des instructions d'un Project :
A. Rôle, format, limites, escalade · B. Données clients identifiantes · C. Sources à utiliser en priorité · D. Mots de passe

<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | Connaissance périmée. |
| Q2 | **A, C** | Jamais de données sensibles ni de secrets. |
</details>

## À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Instructions (règles) ≠ connaissances (faits sourcés) ≠ session ≠ mémoire.
- Connecteurs pour le vivant (avec droits), téléversement pour le stable.
- Propriétaire, versions, revue, tests après changement.
</details>
