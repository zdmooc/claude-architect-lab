# A3 — Governance, Risk, and Responsible Use (15 %)

> **Source des objectifs** : guide officiel CCAO-F v1.0 (juillet 2026), §6, Domain 6. Cours, exemples et questions **originaux**. Fil rouge : [cas ConseilNova](../cas-conseilnova.md) (fictif).

## Objectifs officiels
- identifier les usages appropriés et inappropriés ;
- appliquer les considérations de sensibilité des données, réglementaires et de confidentialité ;
- suivre la politique IA de l'organisation ;
- comprendre les implications éthiques.

**Prérequis** : aucun prérequis de programmation.

**Compétence** : reconnaître quand Claude est inapproprié, protéger les données et organiser une validation humaine proportionnée au risque.

## Cours

Avant d'envoyer un document : **ai-je le droit de l'utiliser ?** Vérifier classification interne, données personnelles, contrats de sous-traitance, conservation, politique d'entreprise et contrôle d'accès. Ne pas supposer qu'un abonnement grand public permet l'envoi d'un dossier confidentiel.

Risques à examiner : réponses inventées, **prompt injection** via documents externes, biais, erreurs sur montants, données datées, confidentialité, dépendance à une réponse automatisée, surconfiance. Une personne vérifie les décisions à impact élevé, avec possibilité effective de refuser ou corriger. **Le modèle ne doit jamais être la source de l'autorisation**.

| Risque | Contrôle | Preuve |
|---|---|---|
| Fuite de données | classification et accès restreints | revue des droits |
| Chiffres faux | vérification contre système de référence | grille signée |
| Procédure obsolète | propriétaire, date/version de mise à jour | journal de révision |
| Message malveillant dans un document | document traité comme données non fiables | cas de test d'injection |
| Décision critique automatisée | approbation par responsable habilité | décision et historique |

## Exercice guidé

Un manager souhaite charger dans un Project partagé des CV avec données personnelles. **Corrigé** : suspendre le chargement, vérifier base légale, droits, outil autorisé et minimisation ; utiliser des profils synthétiques pour la démonstration.

## Piège

« Claude chiffre les données » ne répond pas seul aux questions : **qui peut les lire ? où sont-elles traitées ? combien de temps sont-elles conservées ? qui a approuvé ?**

**À produire** : registre simple **risque, gravité, responsable, contrôle, preuve**.

## Exercice à toi
- **E1.** Approprié ou non (et pourquoi) : (a) résumer un rapport public ; (b) décider seul de licencier un salarié à partir d'évaluations ; (c) rédiger un premier jet de politique interne relu par le juridique.
- **E2.** Un collègue colle un fichier clients complet dans un outil grand public pour « gagner du temps ». Que fais-tu ?
- **E3.** Cite deux risques de biais dans un usage de tri de candidatures et une mesure pour chacun.

## Correction
<details><summary>Voir la correction</summary>

- **E1.** (a) Approprié (données publiques, faible risque). (b) **Inapproprié** : décision à fort impact sur une personne, doit rester humaine, encadrée. (c) Approprié avec relecture experte.
- **E2.** Arrêter, signaler selon la politique (incident de données possible), vérifier quel outil est autorisé, minimiser les données, utiliser des données synthétiques pour les essais.
- **E3.** Biais d'historique (reproduire les choix passés) → critères explicites et revue humaine ; biais de formulation (pénaliser certains profils/langues) → tests par segment et anonymisation des champs non pertinents.
</details>

## Questions d'entraînement (originales)
**Q1.** Avant de charger des documents dans un Project partagé, la première question est :
A. Quel modèle utiliser ? · B. Ai-je le droit de partager ces données dans cet outil ? · C. Quel format de fichier ? · D. Combien de pages ?

**Q2.** (2 réponses) Usages qui demandent une décision humaine finale :
A. Refus d'un crédit · B. Résumé d'un article public · C. Sanction disciplinaire · D. Mise en forme d'un tableau

<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | Gouvernance avant outil. |
| Q2 | **A, C** | Impact fort sur des personnes. |
</details>

## À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Droit d'utiliser les données **avant** l'outil ; minimisation ; outils autorisés.
- Décisions à fort impact : humaines, avec pouvoir réel de refuser.
- Documents externes = données non fiables (injection).
- Biais : tester par segment ; transparence.
</details>
