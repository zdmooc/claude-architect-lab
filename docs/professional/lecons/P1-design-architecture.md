# P1 — Solution Design & Architecture (D1, 17 %)

> **Source des objectifs** : guide officiel CCAR-P v1.0 (juillet 2026), §6, Domain 1. Le cours, les exemples et les questions sont **originaux**.
> Fil rouge : le [cas AssurNova](../cas-assurnova/README.md) (assistant bris de glace, données synthétiques).

## 1. Objectif
Objectifs officiels du domaine :
- traduire un problème métier en solution Claude ;
- concevoir une architecture de bout en bout (entrée → traitement → sortie → **boucle de retour**) ;
- choisir le motif : **workflow**, **agentique** ou **augmented LLM** ;
- concevoir des systèmes multi-agents et leur orchestration ;
- appliquer des techniques de décomposition ;
- aligner la solution sur les piliers de valeur (efficacité, transformation, productivité, coût, SLA de performance).

À la fin, tu sais défendre devant un comité **pourquoi** tu as choisi tel motif, et ce que tu as refusé.

## 2. Prérequis
Foundations M3 (boucle tool use), M6 (sous-agents), M7 (escalade). Ton expérience d'architecte (HLD, ADR) est un atout direct.

## 3. Cours

### a) Du problème à la solution : ne pas commencer par le modèle
Ordre de cadrage :
1. **Résultat métier** mesurable (ex. « délai de traitement d'un sinistre bris de glace »), avec sa **baseline**.
2. **Décisions** dans le processus : lesquelles sont automatisables, lesquelles restent humaines (argent, droit, santé).
3. **Données** : sources, qualité, propriétaire, sensibilité.
4. **Contraintes** : SLA, coût cible, réglementation, systèmes existants.
5. **Seulement ensuite** : où un LLM apporte de la valeur (lire, extraire, résumer, classer, rédiger, raisonner sur des cas ouverts).
Une partie du problème se résout souvent **sans LLM** (règle, formulaire, API). C'est une bonne réponse d'architecte.

### b) Trois motifs, du plus simple au plus autonome
| Motif | Principe | Quand | Risque principal |
|---|---|---|---|
| **Augmented LLM** | un appel enrichi (récupération, outils, mémoire) | tâche bornée : résumer, extraire, répondre avec sources | qualité du contexte fourni |
| **Workflow** | étapes **définies par le code** (chaîne, routage, parallélisation, évaluateur-optimiseur) | processus connu et répétable | rigidité ; mais testable et prévisible |
| **Agentique** | le **modèle choisit** les étapes et les outils en boucle | chemin non prévisible, exploration, diagnostic | coût, latence, dérive, surface d'action |

Règle : **le motif le plus simple qui atteint l'objectif**. On monte en autonomie quand on peut prouver que le gain dépasse le surcoût de contrôle. Un processus réglementé à 5 règles connues = workflow + extraction LLM ciblée, pas un agent libre.

### c) Architecture de bout en bout et boucle de retour
`Entrée` (canal, identité, validation) → `Traitement` (contexte, modèle, outils, règles déterministes) → `Sortie` (format structuré, validation, humain si besoin) → **`Retour`** (corrections des gestionnaires, incidents, métriques → jeu d'évaluation → amélioration). Sans boucle de retour, la qualité se dégrade sans qu'on le voie : c'est le lien avec D4.

### d) Multi-agents : seulement si la décomposition le justifie
Bon cas : sous-tâches **indépendantes** et parallélisables, ou contextes qui se gêneraient (ex. analyser 40 documents). Mauvais cas : tâche séquentielle courte, ou « un agent par service » par principe.
Points de conception : contexte **explicite** passé à chaque sous-agent, périmètres **complémentaires**, format de retour **commun**, budget (tours, tokens) par sous-agent, provenance conservée à la synthèse, coordinateur responsable de la **couverture**.

### e) Techniques de décomposition
- **Fonctionnelle** : par capacité (lire facture, vérifier garantie, proposer).
- **Par données** : un lot ou un document par sous-tâche (map → reduce).
- **Par risque** : isoler ce qui touche l'argent ou les données sensibles derrière des contrôles.
- **Planifier puis exécuter** : un plan validé (humain ou règle) avant les actions.

### f) Piliers de valeur et SLA
Relier chaque choix à un pilier : **efficacité** (temps gagné), **productivité** (volume par gestionnaire), **transformation** (nouveau service), **coût** (complet : tokens, revues humaines, exploitation), **SLA de performance** (latence p95, disponibilité, mode dégradé). Un « taux d'automatisation » seul n'est pas un KPI : il faut qualité et coût en face.

## 4. Exemple — AssurNova
Problème : « réduire le délai de traitement des sinistres bris de glace ».
- Motif retenu : **workflow** (identité → contrat → facture → règles → proposition) avec **augmented LLM** pour lire la facture et rédiger le résumé.
- Refusé : agent autonome avec outil de paiement (surface d'action, conformité). Multi-agents : inutile en V1 (processus séquentiel court).
- Boucle de retour : chaque correction du gestionnaire alimente le jeu d'évaluation mensuel.
- Pilier : efficacité + coût, SLA « proposition en < 30 s p95, repli manuel si l'API est indisponible ».

## 5. Exercice guidé
Demande du sponsor : « un agent qui gère tout le sinistre auto, de la déclaration au paiement ».
1. Découper : déclaration (formulaire), qualification (LLM + règles), expertise (humain), chiffrage (règles), paiement (système existant).
2. Placer le LLM : qualification et synthèse du dossier ; jamais le paiement.
3. Motif : workflow ; un agent seulement pour la **recherche d'informations manquantes** (chemin imprévisible), en lecture seule.
4. Valeur : délai de qualification, taux de dossiers complets du premier coup.

## 6. Exercice à toi
- **E1.** Une banque veut « un chatbot qui répond à toutes les questions des clients sur leurs comptes ». Choisis le motif, justifie, et cite ce que tu exclus de la V1.
- **E2.** Un cabinet d'audit doit analyser 300 contrats fournisseurs pour repérer des clauses de résiliation à risque. Propose une décomposition et dis si des sous-agents sont justifiés.
- **E3.** Le sponsor veut mesurer le succès par « 80 % des dossiers automatisés ». Propose trois indicateurs qui complètent ou remplacent celui-là.

## 7. Correction
<details><summary>Voir la correction</summary>

- **E1.** **Augmented LLM** (récupération de la FAQ et des données du compte via outils **en lecture seule**, avec l'identité du client). Workflow autour : authentification, puis routage (information / opération / réclamation). Exclus de la V1 : virements, modification de coordonnées, conseil en investissement, litiges → transfert humain. Raison : risque financier et réglementaire, et le gain vient surtout de l'information.
- **E2.** Décomposition **par données** : un sous-agent (ou simplement un appel, voire un batch) par contrat, avec le **même schéma de sortie** (clause, extrait, niveau de risque, justification), puis une synthèse. Des sous-agents se justifient si chaque contrat demande une exploration (annexes, renvois) ; sinon un **workflow map → reduce** en Message Batches suffit et coûte moins cher. Contrôle : échantillon relu par un juriste.
- **E3.** Délai de bout en bout (p50/p95) ; **taux d'erreur** détecté en revue ou après coup ; **coût complet par dossier** (tokens + temps humain) ; satisfaction des gestionnaires ; taux d'escalades justifiées. Automatiser 80 % des dossiers avec 5 % d'erreurs coûteuses peut détruire de la valeur.
</details>

## 8. Questions d'entraînement (originales)
**Q1.** Un processus de remboursement suit 6 règles écrites et stables. Une seule étape demande de lire des factures hétérogènes. Motif ?
A. Agent autonome avec tous les outils · B. Workflow codé avec un appel LLM d'extraction · C. Trois sous-agents spécialisés · D. Fine-tuning d'un modèle

**Q2.** (2 réponses) Signaux qui justifient une architecture multi-agents :
A. Sous-tâches indépendantes et parallélisables · B. Volonté d'avoir « un agent par équipe » · C. Contextes volumineux qui se gêneraient dans un seul agent · D. Tâche séquentielle de trois étapes

**Q3.** Six mois après la mise en production, la qualité baisse sans alerte. Quel élément d'architecture manquait le plus probablement ?
A. Un modèle plus grand · B. Une boucle de retour alimentant l'évaluation · C. Un deuxième agent · D. Un prompt plus long

<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | Le plus simple qui suffit ; le LLM seulement là où il apporte. |
| Q2 | **A, C** | B et D ne sont pas des raisons techniques. |
| Q3 | **B** | Sans retour ni évaluation continue, la dérive est invisible. |
</details>

## 9. À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Partir du **résultat métier** et des décisions, pas du modèle.
- **Augmented LLM < workflow < agentique** : choisir le plus simple qui suffit ; justifier chaque montée en autonomie.
- Toujours une **boucle de retour** vers l'évaluation.
- Multi-agents si sous-tâches indépendantes ou contextes lourds ; contexte explicite, format commun, couverture vérifiée.
- Valeur = qualité **et** coût complet **et** SLA, pas un taux d'automatisation seul.
</details>
