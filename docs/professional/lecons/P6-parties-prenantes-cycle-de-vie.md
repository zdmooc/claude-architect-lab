# P6 — Stakeholder Communication & Lifecycle Management (D6, 14 %)

> **Source des objectifs** : guide officiel CCAR-P v1.0, §6, Domain 6. Cours et questions **originaux**.

## 1. Objectif
Objectifs officiels :
- conduire une **découverte structurée** et recueillir les exigences ;
- communiquer décisions d'architecture et compromis ;
- gérer les boucles de retour et l'alignement des attentes (y compris **SLA**) ;
- documenter l'architecture et guider la mise en œuvre ;
- accompagner le cycle de vie : **découverte, conception, passation, supervision, itération**.

## 2. Prérequis
Ton expérience d'architecte : c'est le domaine où elle compte le plus. P1, P4, P5.

## 3. Cours

### a) Découverte structurée
Entretiens par rôle : **sponsor** (valeur, budget), **métier** (processus réel, exceptions), **utilisateurs** (irritants), **IT** (systèmes, intégration), **sécurité/DPO/juridique** (contraintes), **exploitation** (support, astreinte). Questions clés : quel résultat, mesuré comment aujourd'hui (baseline) ? Quelles décisions ne doivent jamais être automatisées ? Quelles données, de quelle qualité ? Quel est le coût d'une erreur ? Livrable : **note de cadrage** avec exigences traçables, hypothèses, hors périmètre, risques ouverts.

### b) Communiquer les décisions et compromis
- **ADR** (Architecture Decision Record) : contexte, options, décision, conséquences, **ce qu'on a refusé et pourquoi**.
- Adapter au public : comité de direction (valeur, risque, coût, calendrier) ; sécurité (contrôles et preuves) ; développeurs (contrats, schémas, guides).
- Parler de **probabilités** honnêtement : un LLM a un taux d'erreur ; on présente la mesure et les contrôles qui la compensent.

### c) Attentes et SLA
Fixer avec les parties prenantes : métriques (P4) et seuils ; **SLA** (latence p95, disponibilité, mode dégradé, délai de traitement humain) ; ce qui se passe en cas de panne du fournisseur. Gérer l'écart entre la démo (« ça marche sur 10 exemples ») et la production (le cas limite fréquent). Revue régulière des métriques avec le sponsor.

### d) Documenter et guider la mise en œuvre
Dossier type : cadrage, **HLD**, ADR, contrats d'interface (outils, schémas), plan d'évaluation et critères de sortie, matrice de contrôles, **runbook** (incidents, dégradé, retour arrière), guide développeur (conventions, `CLAUDE.md`, commandes). Le [cas AssurNova](../cas-assurnova/README.md) en est un exemple complet.

### e) Cycle de vie
| Phase | Livrable / critère |
|---|---|
| Découverte | note de cadrage approuvée |
| Conception | HLD, ADR, plan d'évaluation, matrice de contrôles |
| Construction / pilote | prototype évalué sur le jeu de référence, pilote limité |
| **Passation** | runbook, formation support, propriétaires nommés, tableau de bord |
| Supervision | métriques, alertes, revue échantillonnée |
| Itération | changements versionnés, A/B, ré-évaluation ; gestion des **changements de version de modèle** (tests de non-régression avant migration) |

## 4. Exemple — AssurNova
Comité d'architecture : la note de décision présente 3 options (statu quo, workflow + LLM, agent autonome), recommande l'option 2, chiffre le coût complet, liste les risques résiduels et demande une décision sur le pilote de 6 semaines avec critères de sortie mesurables.

## 5. Exercice guidé
Le directeur métier demande « 100 % de réponses justes avant de lancer ».
1. Reformuler : aucun système (humain compris) n'est à 100 % ; quel est le taux **actuel** des gestionnaires ?
2. Proposer : seuil par segment ≥ baseline humaine, contrôles sur les cas à fort impact, escalade, revue.
3. Documenter l'accord dans le plan d'évaluation et l'ADR.

## 6. Exercice à toi
- **E1.** Liste 6 questions de découverte pour un projet « assistant de réponse aux appels d'offres ».
- **E2.** Rédige un ADR court (5 rubriques) pour le choix « MCP plutôt qu'API directe » pour le référentiel produits.
- **E3.** Le fournisseur annonce l'arrêt de la version de modèle que tu utilises dans 3 mois. Quel plan ?

## 7. Correction
<details><summary>Voir la correction</summary>

- **E1.** Quel délai et quel taux de réussite aujourd'hui ? Qui rédige, combien de temps par réponse ? Quelles sources fiables (réponses passées, fiches produits) et qui les tient à jour ? Quelles parties ne doivent jamais être générées (prix, engagements juridiques) ? Quel niveau de relecture obligatoire ? Quelles contraintes de confidentialité des appels d'offres ?
- **E2.** *Contexte* : 3 équipes ont besoin du référentiel. *Options* : API directe par équipe, serveur MCP partagé. *Décision* : MCP maintenu par l'équipe référentiel. *Conséquences* : une seule implémentation des autorisations ; dépendance au serveur, versionnement à gérer. *Refusé* : API directe (triple maintenance, contrôles divergents).
- **E3.** Inventaire des usages ; exécuter le **jeu d'évaluation** sur le nouveau modèle (qualité, coût, latence) ; ajuster prompts ; pilote progressif ; communication aux parties prenantes ; retour arrière jusqu'à la date d'arrêt ; mettre à jour la documentation et le runbook.
</details>

## 8. Questions d'entraînement (originales)
**Q1.** Avant la conception, le livrable le plus utile est :
A. Le choix du modèle · B. Une note de cadrage avec résultats attendus, baseline, exigences, hors périmètre et risques · C. Un prototype multi-agents · D. Un devis de tokens

**Q2.** Un comité de direction doit décider du lancement. Que présenter en priorité ?
A. Le détail des prompts · B. Options, recommandation, valeur, coût complet, risques résiduels et critères de sortie du pilote · C. L'architecture réseau · D. Le code

**Q3.** (2 réponses) Éléments indispensables à la passation vers l'exploitation :
A. Runbook avec mode dégradé et retour arrière · B. Propriétaires nommés et tableau de bord · C. Le meilleur prompt de démo · D. Une liste de souhaits

<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | On cadre avant de choisir les moyens. |
| Q2 | **B** | Le public décide sur valeur, coût et risque. |
| Q3 | **A, B** | Sans eux, personne ne sait opérer ni qui répond. |
</details>

## 9. À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Découverte multi-rôles ; baseline et coût d'une erreur.
- ADR avec options refusées ; message adapté au public ; honnêteté sur les taux d'erreur.
- SLA et seuils négociés, mode dégradé, revue régulière.
- Dossier : cadrage, HLD, ADR, contrats, évaluation, contrôles, runbook, guide dev.
- Cycle de vie complet, y compris **migration de version de modèle** par ré-évaluation.
</details>
