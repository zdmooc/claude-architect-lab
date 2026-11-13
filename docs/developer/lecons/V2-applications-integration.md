# V2 — Applications and Integration (33,1 %, domaine le plus lourd)

> **Source des objectifs** : guide officiel CCDV-F v1.0, §6, Domain 2. Cours et questions **originaux**. Un tiers de l'examen : à travailler en priorité.

## 1. Objectif
Compétences officielles :
- **Understanding Requirements (3,4 %)** : besoins fonctionnels et d'infrastructure à partir du besoin métier et de l'architecture ;
- **Systems Life Cycle (2,8 %)** : développer, mettre en œuvre, exploiter, maintenir ;
- **Claude API Mechanics (6,8 %)** : messages, outils, streaming, vision, thinking, caching, accès via fournisseurs tiers, accès aux données, batch vs temps réel ;
- **Software Engineering Foundations (7,4 %)** : REST, JSON, asynchrone, gestion de versions, intégration au SDLC, revue de code, refactoring ;
- **Claude Application Design (8,6 %)** : comment Claude interprète les instructions selon la surface (Claude Code, Desktop, claude.ai, API, SDK) ; frontières de contenu, conception de schémas, hygiène de session, gestion des plugins ;
- **Configuration Management (4,1 %)** : `CLAUDE.md`, `settings.json`, épinglage de version de modèle, versionnement des prompts, dépendances de plugins.

## 2. Prérequis
Architect Foundations M1, M2. REST/JSON, Python async de base.

## 3. Cours

### a) Besoins → exigences
Traduire « résumer les dossiers » en exigences : volume, latence, langue, formats d'entrée (PDF, images), sources, sensibilité des données, droits d'accès, disponibilité, coût cible, critères d'acceptation. Exigences d'infrastructure : réseau sortant, secrets, région/fournisseur, quotas, journalisation.

### b) Mécanique de l'API Messages
- Requête : `model`, `max_tokens`, `system`, `messages` (l'**application** gère l'historique : API sans état), `tools`.
- Réponse : liste de **blocs** (`text`, `tool_use`, `thinking`…) + `stop_reason` + `usage`.
- `stop_reason` : `end_turn` (fini), `tool_use` (exécuter un outil), `max_tokens` (**tronqué** : ne pas traiter comme complet), `stop_sequence`, `pause_turn`, `refusal`.
- **Streaming** : événements au fil de l'eau ; ne valider/exploiter que la réponse **complète**.
- **Vision / PDF** : images et documents en entrée ; vérifier qualité et droits.
- **Thinking** (raisonnement étendu/adaptatif) : blocs de réflexion à conserver tels quels dans l'historique lors d'une boucle d'outils.
- **Prompt caching** : préfixe stable (outils, système, documents) mis en cache ; statique avant dynamique.
- **Batch vs temps réel** : Message Batches pour le volume non urgent (moins cher, asynchrone, résultats corrélés par `custom_id`) ; synchrone/streaming pour l'interactif.
- **Fournisseurs tiers** (Bedrock, Vertex AI, Foundry…) : identifiants de modèles, régions, quotas et fonctionnalités peuvent différer ; vérifier avant de supposer.

### c) Ingénierie logicielle
- REST/JSON : codes HTTP (4xx permanent, 429 limite de débit, 5xx transitoire), retries **bornés** avec backoff + jitter seulement si l'opération est sûre (idempotente).
- Asynchrone : appels concurrents avec limite de concurrence, timeouts, annulation.
- SDLC : clés hors du code, tests unitaires avec **faux client**, tests d'intégration séparés, revue de code, PR, refactoring couvert par tests.
- Un HTTP 200 n'est pas un résultat métier fiable : **valider** la sortie.

### d) Concevoir une application Claude
- Chaque surface a son contexte : Claude Code lit `CLAUDE.md` et ses règles ; claude.ai/Desktop utilisent Projets, instructions, connecteurs ; l'API ne reçoit que ce que **tu** envoies.
- **Frontières de contenu** : séparer instructions et données (balises), traiter documents et résultats d'outils comme non fiables.
- **Schémas** : champs `required`, nullables quand l'info peut manquer, énumérations fermées + `autre`, champ d'ambiguïté ; sorties structurées puis validation métier.
- **Hygiène de session** : repartir d'un contexte propre pour une nouvelle tâche, compacter/résumer, ne pas mélanger clients.
- **Plugins** : regroupent commandes, Skills, agents, hooks, serveurs MCP ; versionner et revoir leurs dépendances.

### e) Gestion de configuration
Versionner : `CLAUDE.md`, `settings.json` (permissions, hooks), prompts (fichiers versionnés, identifiant de version journalisé), schémas, **version de modèle épinglée** (identifiant précis, migration testée), dépendances de plugins.

## 4. Exemple — DevBank
Chat de consultation : streaming pour l'affichage, mais la réponse n'est enregistrée qu'à `end_turn` après validation ; prompt système versionné `v3` en cache ; modèle épinglé ; tests avec faux client ([lab](../../../labs/developer_foundations/README.md)). Traitement nocturne des pièces : Message Batches avec `custom_id` = id de pièce, reprise sélective.

## 5. Exercice guidé
Le code concatène `content[0].text`. Avec le raisonnement activé, il plante.
→ Le premier bloc peut être `thinking`. Filtrer par `type == "text"`, et vérifier `stop_reason` avant.

## 6. Exercice à toi
- **E1.** Liste 5 exigences fonctionnelles et 5 d'infrastructure pour « assistant de lecture de relevés bancaires ».
- **E2.** L'API renvoie 429 puis 529/5xx pendant 10 minutes. Décris la politique de reprise et ce qui ne doit **pas** être relancé.
- **E3.** Pourquoi épingler une version précise de modèle, et comment migrer ?

## 7. Correction
<details><summary>Voir la correction</summary>

- **E1.** Fonctionnel : lire PDF de relevé ; extraire opérations (date, libellé, montant) ; signaler les incohérences ; répondre sur un relevé du client seulement ; citer la ligne source. Infrastructure : clé API dans un coffre ; sortie réseau autorisée vers l'API ; journaux sans données personnelles brutes ; quotas et budget ; disponibilité + mode dégradé.
- **E2.** Backoff exponentiel avec jitter, nombre de tentatives borné, respect de l'en-tête de délai si présent ; disjoncteur (circuit breaker) puis mode dégradé (file d'attente, message à l'utilisateur). Ne pas relancer : les 4xx permanents (requête invalide, authentification), et toute **écriture non idempotente** sans clé d'idempotence.
- **E3.** Comportement reproductible ; une nouvelle version peut changer qualité, format ou coût. Migration : passer le jeu d'évaluation, comparer coût/latence, ajuster prompts, déploiement progressif, retour arrière possible.
</details>

## 8. Questions d'entraînement (originales)
**Q1.** `stop_reason = "max_tokens"` sur une extraction JSON. Que faire ?
A. Parser ce qui est reçu · B. Considérer la réponse incomplète : augmenter le budget ou découper, puis revalider · C. Ignorer · D. Passer en streaming

**Q2.** 50 000 documents à classer pour demain, budget serré. Mode ?
A. Streaming · B. Message Batches avec `custom_id` · C. Un appel par seconde en synchrone · D. Claude Code

**Q3.** (2 réponses) À versionner dans le dépôt :
A. Prompts et schémas · B. Clé API · C. `settings.json` d'équipe · D. Journaux de production

<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | Réponse tronquée = incomplète. |
| Q2 | **B** | Volume non urgent, moins cher ; corrélation par `custom_id`. |
| Q3 | **A, C** | Secrets et données de prod hors Git. |
</details>

## 9. À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- API sans état ; blocs typés ; **`stop_reason` avant tout**.
- Streaming = affichage ; validation sur réponse complète.
- Batch pour volume non urgent (`custom_id`) ; caching pour préfixe stable.
- Retries bornés, backoff + jitter, idempotence ; 4xx permanents non relancés.
- Schémas avec nullables ; frontières instructions/données ; hygiène de session.
- Versionner prompts, schémas, config ; **épingler le modèle** et migrer par évaluation.
</details>
