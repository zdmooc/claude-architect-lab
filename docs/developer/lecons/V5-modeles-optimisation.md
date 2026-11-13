# V5 — Model Selection and Optimization (16,8 %)

> **Source des objectifs** : guide officiel CCDV-F v1.0, §6, Domain 5. Cours et questions **originaux**. Avec V2, ce domaine pèse près de **50 %** de l'examen.
> Identifiants, fenêtres de contexte et tarifs **changent** : les vérifier dans la documentation officielle avant tout calcul réel.

## 1. Objectif
Compétences officielles :
- **LLM Fundamentals (5,2 %)** : tokens, fenêtres de contexte, échantillonnage, non-déterminisme ; **fast mode**, raisonnement **étendu/adaptatif**, niveaux d'**effort** ; prompting zero-, single-, multi-shot ;
- **Technical Fundamentals (6,1 %)** : SDK qui encapsulent des API REST, websockets ;
- **Model Selection and Tradeoffs (2,7 %)** : Opus vs Sonnet vs Haiku, compromis qualité/latence/coût, changements cassants entre versions ;
- **Cost and Token Management (2,8 %)** : budget de tokens, modélisation des coûts, prompt caching et points de cache.

## 2. Prérequis
V2. Architect Foundations M0, M1.

## 3. Cours

### a) Fondamentaux des LLM
- **Token** : unité de découpage (ni caractère ni mot) ; facture, limite et `max_tokens` s'expriment en tokens.
- **Fenêtre de contexte** : plafond pour système + historique + outils + documents + sortie.
- **Échantillonnage et non-déterminisme** : deux exécutions peuvent différer ; tester sur plusieurs passages et valider par code.
- **Raisonnement** : étendu (budget de réflexion) ou adaptatif (le modèle décide quand et combien réfléchir) ; le paramètre d'**effort** règle le compromis profondeur/coût/latence ; un **fast mode** existe sur certains modèles pour une sortie plus rapide (prix et disponibilité à vérifier).
- **Zero / single / multi-shot** : 0, 1 ou plusieurs exemples dans le prompt.

### b) Fondamentaux techniques
Les SDK officiels encapsulent l'API REST (types, retries, streaming, pagination). Le streaming utilise des événements serveur (SSE) ; certaines intégrations temps réel utilisent des **websockets** (connexion bidirectionnelle persistante) : gérer reconnexion, ordre et fermeture. Connaître la requête HTTP sous-jacente aide au débogage.

### c) Choisir le modèle
| Famille | Profil | Exemples d'usage |
|---|---|---|
| **Opus** | le plus capable, plus cher, plus lent | raisonnement complexe, agents longs, code difficile |
| **Sonnet** | équilibre | la plupart des applications, agents |
| **Haiku** | rapide, économique | classification, extraction simple, volume, sous-agents |
Démarche : mesurer sur **ton** jeu d'évaluation, choisir le moins coûteux qui atteint le seuil ; router les cas difficiles. **Changements cassants** : une nouvelle version peut changer format, refus, paramètres acceptés ou prix → épingler, lire les notes de migration, rejouer l'évaluation.

### d) Coûts et tokens
- Coût par requête ≈ tokens entrée × tarif entrée + tokens sortie × tarif sortie (+ écritures/lectures de cache, batch à tarif réduit).
- **Coût complet** = API + revues humaines + infrastructure.
- **Prompt caching** : `cache_control` sur un bloc marque un **point de cache** ; le préfixe jusqu'à ce point est réutilisé s'il est identique ; ordre tools → system → messages ; mesurer `cache_creation_input_tokens` et `cache_read_input_tokens`.
- Budget : `max_tokens` borne la **sortie** ; réduire l'entrée (contexte ciblé, sorties d'outils élaguées) ; compter les tokens avant envoi si nécessaire.

## 4. Exemple — calcul de coût complet
Modèle A : 0,02 € par document, 80 % de réussite ; modèle B : 0,06 €, 98 % ; revue d'un échec : 0,50 €.
A = 0,02 + 0,20 × 0,50 = **0,12 €** ; B = 0,06 + 0,02 × 0,50 = **0,07 €** → **B est moins cher au total**. (Hypothèses fictives ; [lab pricing](../../../labs/developer_foundations/README.md).)

## 5. Exercice guidé
Le coût ne baisse pas malgré le caching. Le prompt système commence par l'heure courante.
→ Préfixe différent à chaque appel : cache jamais lu. Déplacer l'heure après le point de cache.

## 6. Exercice à toi
- **E1.** Quel modèle et quels réglages pour : (a) tri de 1 M de tickets par jour ; (b) revue d'architecture d'un monorepo ; (c) chat client interactif ?
- **E2.** Le nouveau modèle refuse un paramètre que l'ancien acceptait. Démarche ?
- **E3.** Calcule : 10 000 requêtes/jour, 6 000 tokens de préfixe identique + 300 variables en entrée, 400 en sortie. Que gagne-t-on avec le caching (qualitativement) et que mesurer ?

## 7. Correction
<details><summary>Voir la correction</summary>

- **E1.** (a) **Haiku**, Message Batches, prompt en cache, évaluation par catégorie. (b) **Opus** avec raisonnement et effort élevé ; latence acceptable. (c) **Sonnet** (ou Haiku si l'évaluation tient), streaming, effort modéré, contexte en cache.
- **E2.** Lire les notes de migration ; adapter la requête ; rejouer la suite de tests et l'évaluation ; déployer progressivement ; garder l'ancienne version épinglée tant qu'elle est disponible.
- **E3.** Les 6 000 tokens identiques sont écrits une fois en cache puis **lus** à tarif réduit et plus vite à chaque appel ; seuls 300 tokens d'entrée restent au plein tarif. Mesurer `cache_read_input_tokens` / `cache_creation_input_tokens` (taux de lecture), latence au premier token, coût réel. Vérifier la durée de vie du cache vs le rythme des requêtes.
</details>

## 8. Questions d'entraînement (originales)
**Q1.** `max_tokens` limite :
A. La durée de la requête · B. La longueur de la sortie · C. La taille de l'entrée · D. Le nombre d'outils

**Q2.** Haiku et Sonnet ont la même exactitude sur ton évaluation. Choix ?
A. Sonnet par sécurité · B. Haiku, avec surveillance de qualité · C. Opus · D. Au hasard

**Q3.** (2 réponses) Cassent le prompt caching :
A. Un horodatage en tête du prompt système · B. Une question utilisateur variable en fin de message · C. Réordonner les outils à chaque requête · D. Un préfixe identique

<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | Plafond de sortie. |
| Q2 | **B** | Décision par la mesure. |
| Q3 | **A, C** | Le préfixe doit être identique ; la fin variable est normale. |
</details>

## 9. À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Tokens, fenêtre, non-déterminisme ; raisonnement étendu/adaptatif, effort, fast mode.
- Opus / Sonnet / Haiku : capacité vs coût vs latence ; choisir par évaluation ; router.
- Versions : épingler, lire les migrations, ré-évaluer.
- Coût complet ; caching = préfixe identique, points de cache, mesurer les tokens de cache.
</details>
