# P4 — Evaluation, Testing & Optimization (D4, 16 %)

> **Source des objectifs** : guide officiel CCAR-P v1.0, §6, Domain 4. Cours et questions **originaux**.

## 1. Objectif
Objectifs officiels :
- définir les métriques (exactitude, latence, coût, sûreté, sécurité) ;
- concevoir jeux d'évaluation et cadres de test par **méthodes mixtes** ;
- conduire des **tests A/B** et des améliorations itératives ;
- diagnostiquer (échec de prompt, hallucination, mauvais choix de modèle) ;
- optimiser tokens, latence et rapport coût/performance ;
- superviser avec journalisation et outils d'observabilité.

## 2. Prérequis
Foundations M2 (validation), M7·L3 (mesure par segment). P2, P3.

## 3. Cours

### a) Les cinq familles de métriques
| Famille | Exemples |
|---|---|
| Exactitude | exactitude par champ, précision/rappel d'une classification, fidélité aux sources (pas d'affirmation non sourcée) |
| Latence | temps jusqu'au premier token, durée totale p50/p95, nombre d'allers-retours d'outils |
| Coût | tokens entrée/sortie/cache par parcours, coût complet avec revue humaine |
| Sûreté | refus appropriés, absence de contenu interdit, escalades déclenchées quand il le faut |
| Sécurité | résistance à l'injection, absence de fuite de données, respect des autorisations |
Chaque métrique a un **seuil d'acceptation** décidé **avant** la mise en production (critère de sortie).

### b) Jeux d'évaluation et méthodes mixtes
- Jeu **représentatif** (cas fréquents) + **cas limites** (ambigus, absents, hors périmètre) + **cas adverses** (injection, tentative d'accès à un autre contrat) + **régressions** (incidents passés).
- Vérité terrain annotée par des experts métier ; segmentation (type de document, canal, langue).
- Méthodes : **vérifications par code** (format, montants, règles), **évaluation par modèle** (« LLM juge » avec grille précise, calibré sur des notes humaines), **revue humaine** sur échantillon. On combine : le code là où c'est possible, le juge pour le qualitatif, l'humain pour calibrer et trancher.

### c) A/B et itération
Changer **une variable** à la fois (prompt, modèle, récupération). D'abord **hors ligne** sur le jeu d'évaluation, puis en ligne sur une fraction du trafic, avec métriques et garde-fous (retour arrière automatique si un seuil se dégrade). Versionner prompts et configurations pour savoir ce qui tourne.

### d) Diagnostiquer
| Symptôme | Cause probable | Où regarder |
|---|---|---|
| Ignore une consigne | prompt ambigu, consigne noyée, conflit de règles | prompt, ordre, exemples |
| Affirmation fausse avec assurance | **hallucination** ou mauvais contexte | sources récupérées, obligation de citer, possibilité de répondre « je ne sais pas » |
| Bon sur le simple, mauvais sur le complexe | **modèle inadapté** | essai avec un modèle supérieur ou raisonnement |
| Régression soudaine sans changement de modèle | données ou index modifiés | récupération, données d'entrée |
| Mauvais outil appelé | descriptions confuses, trop d'outils | P3 a) |

### e) Optimiser coût et latence
Prompt caching (préfixe stable), modèle plus petit si l'évaluation tient, routage, Message Batches pour le non urgent, réduction du contexte (filtrer les résultats d'outils, moins de documents), sorties plus courtes et structurées, moins d'allers-retours (outils plus complets). Toujours **re-mesurer la qualité** après optimisation.

### f) Superviser en production
Tableau de bord : qualité échantillonnée (juge + humain), taux d'escalade, erreurs d'outils, latence p95, coût par parcours, `stop_reason` anormaux. Alertes sur seuils. Les cas corrigés par les humains rejoignent le jeu d'évaluation (boucle de retour de P1).

## 4. Exemple — AssurNova
Critères de sortie V1 : exactitude du montant TTC ≥ 98 % **par type de facture**, 0 proposition > 800 € non escaladée, 0 accès inter-contrat sur 200 tentatives adverses, latence p95 < 30 s, coût par dossier ≤ budget. Évaluation : code pour montants/seuils, juge pour la qualité du résumé (calibré sur 100 notes de gestionnaires), revue humaine de 2 % des dossiers.

## 5. Exercice guidé
« Le nouveau prompt est meilleur, je l'ai essayé sur 5 exemples. »
1. 5 exemples ne prouvent rien : passer le **jeu complet** (ancien vs nouveau prompt).
2. Comparer **par segment** : le gain global peut cacher une régression sur un type de document.
3. Si mieux hors ligne : déploiement progressif (10 % du trafic), surveillance, retour arrière prêt.

## 6. Exercice à toi
- **E1.** Définis 5 métriques (une par famille) avec un seuil pour un assistant RH qui répond aux questions sur les congés.
- **E2.** Ton LLM juge note la qualité à 4,6/5 alors que les gestionnaires se plaignent. Que vérifies-tu ?
- **E3.** Le coût mensuel a doublé, le trafic est stable. Trois hypothèses à vérifier.

## 7. Correction
<details><summary>Voir la correction</summary>

- **E1.** Exactitude : ≥ 95 % de réponses conformes à la politique sur le jeu annoté. Latence : p95 < 5 s. Coût : ≤ X centimes par question. Sûreté : 100 % des questions médicales/disciplinaires escaladées. Sécurité : 0 divulgation du solde d'un autre salarié sur les tests adverses.
- **E2.** **Calibration** du juge : comparer ses notes à des notes humaines sur un échantillon ; grille trop vague ; juge qui voit la réponse sans la source ; biais (préférence pour les réponses longues). Corriger la grille, ajouter des exemples notés, ou utiliser des vérifications par code pour les critères objectifs.
- **E3.** Cache cassé (préfixe modifié, ex. date en tête) ; contexte qui a grossi (plus de documents récupérés, résultats d'outils non filtrés, historique non résumé) ; changement de modèle ou de routage vers le plus cher ; boucles d'agents plus longues (plus de tours). Vérifier via `usage` par parcours.
</details>

## 8. Questions d'entraînement (originales)
**Q1.** Pour valider un changement de prompt, la meilleure démarche est :
A. Essayer sur quelques exemples · B. Comparer ancien et nouveau sur le jeu d'évaluation complet, par segment, puis déploiement progressif · C. Déployer et attendre les plaintes · D. Demander au modèle s'il préfère le nouveau

**Q2.** Un assistant invente des numéros d'articles de loi. Les sources récupérées ne les contiennent pas. Correctif prioritaire ?
A. Modèle plus grand · B. Exiger la citation des sources fournies, autoriser « je ne sais pas », et vérifier par code que l'article cité existe · C. Augmenter la température · D. Ajouter des exemples few-shot quelconques

**Q3.** (2 réponses) Bonnes pratiques pour un LLM juge :
A. Grille précise par critère · B. Calibration sur des notes humaines · C. Même prompt que le système évalué · D. Aucune revue humaine nécessaire

<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | Mesure complète, segmentée, puis prudence en production. |
| Q2 | **B** | Ancrage dans les sources + contrôle déterministe. |
| Q3 | **A, B** | Un juge non calibré n'est pas une mesure. |
</details>

## 9. À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Cinq familles : exactitude, latence, coût, sûreté, sécurité ; **seuils décidés avant** la production.
- Jeu d'évaluation : représentatif + limites + adverses + régressions ; vérité terrain ; segments.
- Méthodes mixtes : code, LLM juge **calibré**, humain.
- A/B : une variable à la fois, hors ligne puis progressif, retour arrière.
- Diagnostic par symptôme ; régression après changement de données → récupération.
- Optimiser puis **re-mesurer** la qualité.
</details>
