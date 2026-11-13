# P2 — Claude Models, Prompting & Context Engineering (D2, 13 %)

> **Source des objectifs** : guide officiel CCAR-P v1.0, §6, Domain 2. Cours et questions **originaux**.
> Les identifiants et prix de modèles changent : **vérifie-les sur la documentation officielle** au moment de l'examen.

## 1. Objectif
Objectifs officiels :
- choisir le modèle Claude selon les compromis ;
- concevoir prompts système, gabarits et garde-fous ;
- appliquer zero-shot, few-shot, chain-of-thought ;
- optimiser la fenêtre de contexte et l'usage des tokens ;
- mettre en place la réutilisation de prompts (**caching**, prompts modulaires, **Skills**).

## 2. Prérequis
Foundations M2 (prompts explicites, few-shot, sorties structurées) et M7 (contexte).

## 3. Cours

### a) Choisir le modèle : un compromis mesuré
Familles Claude : un modèle **le plus capable** (raisonnement complexe, agents longs), un modèle **équilibré**, un modèle **rapide et économique** (classification, extraction simple, volume). Critères :
- **qualité requise** sur *ta* tâche, mesurée sur *ton* jeu d'évaluation (D4) ;
- **latence** (temps jusqu'au premier token, durée totale) ;
- **coût** par requête × volume ;
- capacités nécessaires (fenêtre de contexte, raisonnement étendu, vision, outils).
Démarche : prototyper avec le plus capable pour connaître le plafond de qualité, puis **descendre** tant que l'évaluation tient. On peut **router** : petit modèle pour le tri, grand modèle pour les cas difficiles.

### b) Prompt système, gabarits, garde-fous
- **Prompt système** : rôle, périmètre, règles, format de sortie, conduite en cas de doute (« si l'information manque, dis-le »).
- **Gabarits** : parties fixes + variables balisées (`<facture>…</facture>`) ; versionnés comme du code.
- **Garde-fous** : dans le prompt (refus hors périmètre) **et** hors prompt (validation de sortie, contrôles dans les outils, hooks). Rappel Foundations : le prompt **guide**, le code **garantit**.

### c) Techniques
- **Zero-shot** : consignes claires suffisent pour une tâche simple.
- **Few-shot** : 2–5 exemples **variés et difficiles**, dont un cas « absent / ambigu ».
- **Chain-of-thought** : faire raisonner avant de conclure (balises de réflexion, ou **raisonnement étendu** du modèle) pour les tâches multi-étapes ; coûte des tokens et de la latence, à réserver aux tâches qui en profitent.

### d) Fenêtre de contexte et tokens
- Envoyer **ce qui sert à la question**, pas tout le dossier.
- Résultats d'outils **filtrés à la source**.
- **Bloc de faits** en tête pour les longues conversations ; résumés guidés.
- Mesurer `usage` (entrée, sortie, cache) par type de requête.

### e) Réutilisation : caching, modularité, Skills
- **Prompt caching** : le préfixe **identique** d'une requête à l'autre (outils, prompt système, documents de référence) est mis en cache ; les requêtes suivantes le relisent plus vite et moins cher. **Condition** : mettre le **statique avant le dynamique** et ne pas modifier ce préfixe (une date ou un identifiant au début casse le cache).
- **Prompts modulaires** : blocs réutilisables (politique, format, ton) assemblés par le code, versionnés.
- **Skills** : paquets d'instructions (et éventuellement de scripts) chargés **à la demande** : seule la description est visible en permanence, le contenu est chargé quand la tâche le demande. On garde le contexte léger et on partage des savoir-faire entre équipes (lien D3 « progressive discovery » et D7).

## 4. Exemple — AssurNova
- Lecture de facture : modèle **économique** + schéma structuré ; l'évaluation montre 97 % d'exactitude, comme le modèle supérieur → on garde l'économique.
- Cas « garantie ambiguë » : routés vers le modèle **le plus capable** avec raisonnement.
- Prompt système de 6 000 tokens (règles + barème) identique pour tous → placé **en premier** avec prompt caching ; le message du client vient après.

## 5. Exercice guidé
Une équipe ajoute au début du prompt système « Nous sommes le {date_heure} ». Les coûts n'ont pas baissé malgré le caching.
→ Le préfixe change à chaque requête : le cache n'est jamais réutilisé. Correction : déplacer la date **après** le contenu statique (ou dans le message utilisateur).

## 6. Exercice à toi
- **E1.** Classification de 200 000 courriels par jour en 5 catégories, pas d'urgence. Quel modèle et quel mode d'appel proposes-tu, et comment le justifies-tu ?
- **E2.** Écris le squelette d'un prompt système pour l'assistant AssurNova (6 rubriques maximum).
- **E3.** Trois équipes copient-collent les mêmes 2 pages de « règles de rédaction des courriers ». Que proposes-tu ?

## 7. Correction
<details><summary>Voir la correction</summary>

- **E1.** Modèle **rapide et économique**, validé sur un jeu annoté (exactitude par catégorie) ; mode **Message Batches** (asynchrone, moins cher) ; prompt système stable en cache ; escalade des cas peu sûrs vers un modèle supérieur ou un humain. Justification par la mesure, pas par l'intuition.
- **E2.** 1. Rôle et périmètre (bris de glace, lecture seule, pas de paiement). 2. Sources autorisées et obligation de citer. 3. Règles (identité avant tout, seuil 800 € → humain, demande d'humain). 4. Conduite en cas de doute (null, question, escalade). 5. Format de sortie (schéma). 6. Ton et langue.
- **E3.** Une **Skill** partagée (ou un module de prompt versionné) « rédaction des courriers », chargée à la demande ; un seul propriétaire, revue des changements, et évaluation après modification.
</details>

## 8. Questions d'entraînement (originales)
**Q1.** Le modèle le plus capable et le modèle équilibré obtiennent la même exactitude sur ton jeu d'évaluation ; le second coûte nettement moins cher. Que fais-tu ?
A. Garder le plus capable par prudence · B. Choisir l'équilibré, avec surveillance de la qualité en production · C. Prendre le plus petit sans tester · D. Alterner au hasard

**Q2.** Pourquoi placer les instructions et documents fixes **avant** la question variable ?
A. Le modèle lit mieux la fin · B. Pour que le préfixe soit réutilisable par le prompt caching · C. C'est obligatoire dans l'API · D. Pour réduire `max_tokens`

**Q3.** (2 réponses) Quand le chain-of-thought / raisonnement étendu est-il justifié ?
A. Analyse multi-étapes d'une garantie avec exclusions · B. Classement d'un courriel en 3 catégories évidentes · C. Diagnostic d'un incident à causes multiples · D. Traduction d'un mot

<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | Décision par la mesure ; la surveillance couvre la dérive. |
| Q2 | **B** | Le cache porte sur un préfixe identique. |
| Q3 | **A, C** | Raisonnement utile pour le multi-étapes ; coût inutile sinon. |
</details>

## 9. À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Modèle choisi **par l'évaluation** sur ta tâche : qualité, latence, coût ; routage possible.
- Prompt système = rôle, périmètre, règles, doute, format ; garde-fous aussi **hors prompt**.
- Few-shot varié ; chain-of-thought quand la tâche est multi-étapes.
- **Statique avant dynamique** + prompt caching ; ne pas casser le préfixe.
- Réutilisation : modules versionnés, **Skills** chargées à la demande.
</details>
