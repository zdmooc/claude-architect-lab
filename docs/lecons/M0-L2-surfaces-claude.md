# M0 · Leçon 2 — Les surfaces Claude : qui fait quoi ?

> Sources : documentation de référence de l'API Claude consultée le 13/11/2026 (via la skill officielle `claude-api`), dossier de préparation (synthèse du guide Foundations).
> Les noms de produits évoluent vite : vérifier la doc avant un projet réel.

## 1. Objectif et utilité
Savoir **choisir la bonne surface** pour un besoin : claude.ai, API Messages, Tool Runner, Claude Agent SDK, Claude Code, MCP.
À l'examen, beaucoup de questions sont des choix d'architecture : « quelle brique pour ce scénario ? ».
Confondre deux surfaces, c'est se tromper de réponse même en connaissant chaque produit.

## 2. Prérequis
Leçon M0·L1 (stateless, contexte, tokens).

## 3. Cours

### a) Deux grandes familles
| Famille | Pour qui | Exemples |
|---|---|---|
| **Applications prêtes à l'emploi** | un utilisateur humain | claude.ai (web, desktop, mobile), Claude Code (terminal, IDE) |
| **Briques pour construire** | un développeur / architecte | API Messages, SDK Anthropic, Claude Agent SDK, MCP |

### b) Les briques, de la plus simple à la plus complète

**1. API Messages** (`POST /v1/messages`) — le socle. Une requête, une réponse. Tout le reste passe par elle.
Tu gères tout : historique (stateless !), outils, boucle.
👉 Analogie : JDBC brut. Tu maîtrises tout, tu écris tout.

**2. Tool use (« function calling »)** — une fonctionnalité *de l'API Messages*, pas une API séparée.
Tu déclares des outils (nom, description, schéma JSON). Claude répond « appelle tel outil avec tels paramètres » ; **ton code exécute** et renvoie le résultat.
Deux façons :
- **boucle manuelle** : tu écris `tant que stop_reason == "tool_use" : exécuter, renvoyer` ;
- **Tool Runner** : un helper du SDK Anthropic qui écrit cette boucle pour toi, sur *tes* outils.

**3. Claude Agent SDK** — produit **distinct** (`claude-agent-sdk`). C'est le moteur de Claude Code packagé en bibliothèque :
boucle agentique, outils intégrés (Read, Write, Edit, Bash, Grep, Glob…), sous-agents, hooks, permissions, sessions.
👉 Analogie : un serveur d'applications (WebSphere) vs une servlet nue : beaucoup de services fournis, mais tu l'héberges toi-même.

**4. Claude Code** — l'application de développement (terminal/IDE) construite sur ce moteur.
Configurable par fichiers : `CLAUDE.md`, règles, commandes, Skills, serveurs MCP. Utilisable en CI en mode non interactif.

**5. MCP (Model Context Protocol)** — un **protocole standard** pour brancher des outils et des données à une application IA (Claude Code, claude.ai, ton agent…).
Un serveur MCP expose des *tools*, des *resources*, des *prompts* ; un client MCP les consomme.
👉 Analogie : JCA / connecteurs standard : on écrit le connecteur une fois, n'importe quel client compatible l'utilise.

### c) Le piège classique : Tool Runner ≠ Claude Agent SDK
| | Tool Runner | Claude Agent SDK |
|---|---|---|
| Package | SDK Anthropic standard (`anthropic`) | Package séparé (`claude-agent-sdk`) |
| Outils | **Uniquement les tiens** | Outils intégrés (fichiers, bash, recherche) + les tiens + MCP |
| Ce qu'il fournit | La boucle | La boucle + tout le « harnais » de Claude Code |
| Hébergement | Toi | Toi |

### d) Où vit l'état ?
- API Messages : **chez toi** (ton application renvoie l'historique).
- claude.ai, Claude Code, Agent SDK : l'application/le SDK gère l'historique et les sessions pour toi.

### e) Remarque sur le périmètre
Il existe aussi des agents hébergés par Anthropic (« Managed Agents », en bêta). Ton dossier ne les cite pas dans le programme Foundations : on les garde en culture générale, sans y passer de temps pour l'instant.

## 4. Exemple concret commenté
Besoin : *« Un assistant interne qui répond aux questions des gestionnaires sur les procédures sinistres, en consultant une base documentaire. »*

- Pas besoin d'éditer des fichiers ni d'exécuter du bash → **pas besoin de l'Agent SDK**.
- Besoin d'un ou deux outils maison (`rechercher_procedure`, `lire_procedure`) → **API Messages + tool use** (boucle manuelle ou Tool Runner).
- Si d'autres applications (Claude Code des développeurs, claude.ai) doivent aussi accéder à cette base → exposer les outils via un **serveur MCP**, réutilisable partout.

Règle d'architecte : **commencer par la surface la plus simple qui répond au besoin**. Un agent coûte plus cher et se teste plus difficilement qu'un appel unique ou un workflow codé.

## 5. Exercice guidé
Besoin : *« Chaque nuit, la CI doit relire les PR du dépôt et produire un rapport JSON des problèmes trouvés. »*

1. Qui lit le code ? Il faut lire des fichiers, parcourir l'arborescence → outils fichiers/recherche.
2. Existe-t-il une surface qui les fournit déjà ? Oui : **Claude Code** (et son moteur, l'Agent SDK).
3. Mode d'exécution ? Pas d'humain la nuit → **mode non interactif** (`claude -p`, sortie JSON).
4. Conclusion : **Claude Code en CI** — c'est d'ailleurs l'un des 6 scénarios du guide.
5. Mauvaise réponse tentante : « API Messages + j'écris mes propres outils de lecture de fichiers » → possible, mais on réinvente ce qui existe.

## 6. Exercice à toi
Pour chaque besoin, indique **la surface** la plus adaptée et **une phrase de justification** :

- **A.** Classer 10 000 courriels clients en 5 catégories, la nuit, sans urgence.
- **B.** Un conseiller veut rédiger un courrier de réclamation, une fois, sans rien coder.
- **C.** Une équipe veut que Claude Code, claude.ai **et** un agent maison puissent tous interroger le référentiel des contrats.
- **D.** Un agent qui doit lire des fichiers, lancer des scripts et déléguer à des sous-agents, hébergé dans ton OpenShift.

## 7. Correction
*Ajoutée après la réponse de l'apprenant.*

## 8. À retenir pour l'examen
*Ajouté avec la correction.*
