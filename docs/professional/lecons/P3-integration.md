# P3 — Integration (D3, 19 %, domaine le plus lourd)

> **Source des objectifs** : guide officiel CCAR-P v1.0, §6, Domain 3. Cours et questions **originaux**.
> Le guide donne lui-même un exemple de question D3 (moindre privilège sur un agent de support) : c'est exactement le raisonnement de la section a).

## 1. Objectif
Objectifs officiels :
- évaluer la configuration outils/agents pour éviter la **capability bloat** ;
- analyser authentification et autorisation pour trouver les failles ;
- évaluer les compromis **exactitude / latence** et justifier la configuration ;
- analyser l'observabilité à l'échelle et choisir une stratégie de supervision ;
- concevoir un pipeline **RAG** (découpage, indexation) ;
- adapter la stratégie de récupération à la forme des données et des requêtes ;
- choisir le mécanisme d'intégration : **MCP, API/CLI, agent-to-agent** ;
- évaluer **progressive discovery** vs **contexte monolithique**.

## 2. Prérequis
Foundations M3 (outils), M4 (MCP), M6 (hooks), M7. P1, P2.

## 3. Cours

### a) Capability bloat et moindre privilège
Chaque outil est une **surface d'action** et du **contexte consommé** (sa description est envoyée). Trop d'outils = confusions de choix, coût, risque.
Revue d'une configuration : pour chaque outil, *le rôle en a-t-il besoin ?* Sinon **le retirer** — c'est plus fort que journaliser ou demander confirmation (contrôles compensatoires). Préférer des outils **lecture seule** et des écritures étroites (« soumettre une proposition » plutôt que « exécuter un paiement »).

### b) Authentification et autorisation : où sont les failles
- L'agent agit **pour un utilisateur** : propager son identité (jeton délégué, scopes) jusqu'au système métier, qui **décide** de l'autorisation. Un compte technique tout-puissant derrière l'agent = faille classique (le modèle peut être manipulé pour lire le contrat d'un autre).
- Autorisation **dans le serveur d'outils**, pas dans le prompt.
- Secrets hors du contexte du modèle et hors Git ; rotation gérée par la plateforme.
- Résultats d'outils et documents = **données non fiables** (injection indirecte) : ils ne doivent pas pouvoir élargir les droits.

### c) Exactitude vs latence
Leviers : taille du modèle, raisonnement étendu, nombre de documents récupérés, nombre d'allers-retours d'outils, validations supplémentaires. Chaque levier se **mesure** (D4). Justifier par le besoin : un assistant conversationnel vise une latence courte (streaming, petit modèle, contexte en cache) ; une analyse de dossier nocturne vise l'exactitude.

### d) Observabilité à l'échelle
À tracer par requête : identifiant de corrélation, modèle et version de prompt, tokens (entrée, sortie, cache), latence, outils appelés et résultats (statut), décision finale, escalade. **Sans** données personnelles brutes dans les journaux. À superviser : taux d'erreurs d'outils, `stop_reason` anormaux, coût par parcours, dérive des métriques qualité (échantillonnage + évaluation automatique), alertes sur seuils. Les traces d'agents (arbre d'appels) sont indispensables pour diagnostiquer.

### e) RAG : découpage et indexation
- **Découpage** selon la structure : par section/article pour un contrat, par question pour une FAQ ; taille adaptée ; chevauchement léger ; **métadonnées** (source, version, date, droits d'accès).
- **Indexation** : lexicale (mots exacts, références, codes) et/ou sémantique (sens) ; **hybride** souvent le meilleur choix ; reclassement (*reranking*) des meilleurs résultats.
- **Filtrer par droits avant** de récupérer.
- Ré-indexer après mise à jour des documents, et **tester** après chaque ré-indexation (exemple officiel : réponses fausses après rafraîchissement → regarder d'abord la récupération).

### f) Récupération adaptée aux données
| Forme des données / requêtes | Stratégie |
|---|---|
| Références exactes (n° de contrat, article) | recherche lexicale ou requête structurée |
| Questions en langage naturel sur des textes | sémantique ou hybride + reranking |
| Données tabulaires, chiffres | requête SQL/API via outil, pas d'embedding |
| Petit corpus stable | le mettre directement en contexte (avec caching) |
| Questions multi-sauts | récupération itérative (agentique) |

### g) Choisir le mécanisme d'intégration
- **API/CLI directe** : une application, peu d'outils, contrôle maximal.
- **MCP** : exposer outils/ressources/prompts une fois pour plusieurs clients (Claude Code, assistants, agents) ; standardise découverte et descriptions.
- **Agent-to-agent** : déléguer à un **autre agent autonome** (autre équipe, autre système) via un protocole d'échange entre agents ; utile quand l'autre partie a sa propre logique et ses propres outils. Coût : contrat d'interface, confiance et traçabilité inter-agents.

### h) Progressive discovery vs contexte monolithique
- **Monolithique** : tout charger d'emblée (tous les outils, toute la doc). Simple, mais contexte saturé, coût, confusions.
- **Progressive discovery** : n'exposer d'abord que des **résumés** (descriptions de Skills, liste de ressources, outil de recherche d'outils) et charger le détail **à la demande**. Adapté aux grands catalogues d'outils et de connaissances. Inconvénient : un aller-retour de plus et le risque de ne pas « découvrir » le bon élément si les descriptions sont mauvaises.

## 4. Exemple — AssurNova
- Outils : `consulter_contrat`, `rechercher_procedure`, `lire_facture` (lecture seule) ; `soumettre_proposition` (écriture étroite, idempotente) ; `escalader`. **Pas** de paiement.
- Identité du client propagée jusqu'au référentiel ; le serveur refuse un contrat qui n'est pas le sien (test inter-contrats).
- Procédures internes : RAG hybride, découpage par article, métadonnées de version ; filtrage par habilitation.
- Intégration : serveur **MCP** « référentiel sinistres » partagé avec Claude Code des développeurs et l'assistant.

## 5. Exercice guidé
Un agent RH a 35 outils (paie, congés, recrutement, formation…) ; il choisit souvent le mauvais.
1. Mesurer : quels outils sont réellement appelés, par quel rôle.
2. Retirer ceux que le rôle n'utilise pas (capability bloat).
3. Pour le reste : améliorer les descriptions, regrouper par domaine, ou **progressive discovery** (Skills/outil de recherche d'outils).
4. Ré-évaluer le taux de bon choix d'outil.

## 6. Exercice à toi
- **E1.** L'agent de support utilise un compte de service qui lit tous les contrats ; le client fournit son numéro dans la conversation. Quelle faille, et quelle correction ?
- **E2.** Corpus : 2 000 procédures internes versionnées + une base SQL des sinistres. Les questions sont « comment traiter X ? » et « combien de sinistres de type Y en octobre ? ». Propose la stratégie de récupération pour chacune.
- **E3.** Trois équipes veulent que leurs assistants accèdent au référentiel produits. API directe, MCP ou agent-to-agent ? Justifie.

## 7. Correction
<details><summary>Voir la correction</summary>

- **E1.** Autorisation fondée sur une donnée **fournie par l'utilisateur** et un compte trop puissant : n'importe qui peut lire le contrat d'un autre (ou une injection peut le provoquer). Correction : authentifier le client, propager **son** identité (jeton délégué) au serveur, qui n'autorise que ses contrats ; test inter-contrats en CI ; journal d'accès.
- **E2.** Procédures : RAG **hybride** (termes métier exacts + sens), découpage par section, métadonnées de version et filtre « version en vigueur », reranking, citation de la source. Statistiques : **outil de requête SQL** paramétré (lecture seule, requêtes autorisées), pas de RAG : les chiffres doivent venir de la base.
- **E3.** **MCP** : un serveur maintenu par l'équipe propriétaire du référentiel, réutilisé par trois clients, avec autorisation côté serveur. API directe = trois intégrations à maintenir. Agent-to-agent seulement si le référentiel était lui-même un agent autonome avec sa logique.
</details>

## 8. Questions d'entraînement (originales)
**Q1.** Après la mise à jour du catalogue de garanties, l'assistant cite des garanties supprimées, avec assurance. Le modèle n'a pas changé. Première piste ?
A. Changer de modèle · B. Index non reconstruit ou anciennes versions non filtrées · C. Température trop haute · D. `max_tokens` trop bas

**Q2.** Un agent d'analyse n'a besoin que de lire des tickets ; il dispose aussi de `fermer_ticket` et `supprimer_client`. Meilleure action ?
A. Journaliser ces deux outils · B. Les retirer de sa configuration · C. Ajouter une confirmation · D. Ajouter une consigne dans le prompt

**Q3.** (2 réponses) Arguments en faveur de la progressive discovery :
A. Catalogue de 200 outils · B. Base documentaire très large · C. Deux outils seulement · D. Exigence de latence minimale absolue sur chaque requête

<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | Symptôme lié à un changement de documents → récupération/indexation. |
| Q2 | **B** | Moindre privilège : supprimer la capacité inutile. A et C sont compensatoires. |
| Q3 | **A, B** | Gros catalogues ; avec 2 outils ou une latence critique, le chargement direct est préférable. |
</details>

## 9. À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- **Retirer** les capacités inutiles avant tout autre contrôle.
- Identité de l'utilisateur **propagée**, autorisation **dans le serveur**, jamais sur une donnée fournie par l'utilisateur.
- Observabilité : corrélation, modèle/prompt versionnés, tokens, outils, décisions, sans données sensibles brutes.
- RAG : découpage par structure, métadonnées, hybride + reranking, filtre de droits, tests après ré-indexation.
- Stratégie de récupération selon la forme des données ; chiffres → requête structurée.
- MCP pour mutualiser ; API directe pour un usage unique ; agent-to-agent pour déléguer à un agent autonome.
- Progressive discovery pour les grands catalogues.
</details>
