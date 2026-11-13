# M4 · Leçon 3 — Brancher un serveur MCP : portée projet / utilisateur, secrets (D2)

> **Statut** : `labs/m4/mcp.json.exemple` est une **proposition** suivant le format `.mcp.json` de Claude Code ; syntaxe exacte et commandes `claude mcp` **à vérifier** sur ta version de Claude Code en M5 (non testé par le formateur).

## 1. Objectif et utilité
Savoir **où** déclarer un serveur MCP (pour toute l'équipe ou pour soi), et comment y passer un secret proprement. Compétences D2 du dossier : configuration projet/utilisateur, expansion de variables d'environnement plutôt que secrets committés.

## 2. Prérequis
M4·L2.

## 3. Cours
### a) Deux portées principales
| Portée | Où | Pour qui | Versionné ? |
|---|---|---|---|
| **Projet** | fichier `.mcp.json` à la racine du dépôt | toute l'équipe qui clone le dépôt | **oui** |
| **Utilisateur** | configuration personnelle de Claude Code | toi seul, dans tous tes projets | non |
Claude Code propose aussi une portée **locale** (toi seul, ce projet). Règle : un serveur **nécessaire au projet** → portée projet ; un outil **personnel** (ton agenda, tes notes) → portée utilisateur.

### b) Secrets : référence, pas valeur
```json
"env": { "REFERENTIEL_TOKEN": "${REFERENTIEL_TOKEN}" }
```
Le fichier versionné contient la **référence** ; la valeur vit dans l'environnement de chaque développeur ou dans le coffre de la CI.
👉 Même logique qu'un `Secret` OpenShift monté en variable : le manifeste est dans Git, la valeur non.

### c) Sécurité
Un serveur MCP exécute du code avec **tes droits**. Avant d'en ajouter un : lire ses permissions et ses dépendances (ton dossier le rappelle pour le dépôt `modelcontextprotocol/servers`). Claude Code demande une approbation pour les serveurs d'un `.mcp.json` de projet.

## 4. Exemple commenté : `mcp.json.exemple`
- `"command": "python", "args": [...]` → transport **stdio** : Claude Code lance le serveur comme sous-processus.
- `"env"` → le jeton vient de la variable `REFERENTIEL_TOKEN` du poste.
- Rien de secret dans le fichier → il peut être committé.

## 5. Exercice guidé
Un développeur committe `.mcp.json` avec `"REFERENTIEL_TOKEN": "eyJhbGciOi..."`.
1. Risque : le jeton est dans l'historique Git (même si on le supprime ensuite).
2. Action : **révoquer** le jeton, puis remplacer par `${REFERENTIEL_TOKEN}`.
3. Prévention : revue de code, scan de secrets en CI.

## 6. Exercice à toi
- **E1.** Ton équipe partage un serveur MCP « référentiel contrats » ; toi seul utilises un serveur MCP « mes notes ». Où déclares-tu chacun ?
- **E2.** Écris le bloc `.mcp.json` pour un serveur `ged-sinistres` lancé par `node ged.js`, qui a besoin de `GED_URL` (non secret) et `GED_TOKEN` (secret).
- **E3.** Un nouveau développeur clone le dépôt et le serveur MCP échoue au démarrage. Cite deux causes probables liées à cette leçon.

## 7. Correction
*Après ta réponse.*
## 8. À retenir pour l'examen
*Avec la correction.*
