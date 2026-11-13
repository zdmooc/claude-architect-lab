# V8 — Tools and MCPs (10,6 %)

> **Source des objectifs** : guide officiel CCDV-F v1.0, §6, Domain 8. Cours et questions **originaux**.

## 1. Objectif
Compétences officielles :
- **Tool Implementation (4,4 %)** : tool use / function calling, descriptions d'outils, gestion d'erreurs, outils **côté client vs côté serveur**, motifs d'approbation, construction du jeu d'outils ;
- **MCP Server Development (2,1 %)** : écriture et déploiement de serveurs, resources/tools/prompts, **stdio vs sockets** ;
- **Agentic Customization (4,1 %)** : arbitrer entre outils intégrés, outils personnalisés, **Skills** et **MCP**.

## 2. Prérequis
Architect Foundations M3 et M4 (labos M3, M4).

## 3. Cours

### a) Implémenter un outil
- **Nom** distinct, **description** (quoi, quand, quand pas, formats), **schéma** d'entrée strict (`strict: true` si disponible).
- **Résultat** structuré ; erreurs distinguées : introuvable ≠ accès refusé ≠ panne temporaire ≠ liste vide ; `is_error` + catégorie + réessayable.
- **Client vs serveur** : un outil **client** est exécuté par ton code (tu reçois `tool_use`, tu renvoies `tool_result`) ; un outil **côté serveur** est exécuté par la plateforme Anthropic (ex. recherche web, exécution de code) et son résultat arrive directement dans la réponse.
- **Approbation** : pour les effets de bord, demander confirmation (humaine ou règle) avant exécution ; idempotence ; audit. Ne jamais **inventer** un `tool_result`.
- **Jeu d'outils** : minimal pour le rôle ; regrouper ou séparer selon la confusion mesurée.

### b) Serveurs MCP
- Primitives : **tools** (actions décidées par le modèle), **resources** (contenus de référence par URI), **prompts** (gabarits choisis par l'utilisateur).
- SDK Python `mcp` 2.x : `MCPServer`, `@serveur.tool()`, `@serveur.resource(uri)`, `ToolError` pour une erreur explicite.
- **Transports** : **stdio** (processus local lancé par le client, simple, mono-utilisateur) ; **HTTP/sockets** (serveur distant partagé : authentification, TLS, montée en charge, déploiement).
- MCP ne règle pas l'autorisation métier : contrôles **dans** le serveur.

### c) Choisir le mécanisme d'extension
| Besoin | Choix |
|---|---|
| Lire/éditer des fichiers, chercher, exécuter dans Claude Code | **outils intégrés** |
| Fonction propre à une seule application | **outil personnalisé** dans l'app |
| Accès à un système partagé par plusieurs clients | **serveur MCP** |
| Savoir-faire/procédure réutilisable, chargé à la demande | **Skill** |
Critères : réutilisation, sécurité, coût en contexte (descriptions envoyées), maintenance.

## 4. Exemple — DevBank
`get_contract` (outil client, lecture seule, ownership vérifié) ; serveur MCP « référentiel produits » en HTTP pour trois équipes ; Skill « rédiger un résumé de garantie » ; recherche web (outil serveur) **désactivée** car inutile au rôle.

## 5. Exercice guidé
Le modèle confond `rechercher_client(nom)` et `consulter_contrat(numero)`. → Descriptions avec cas d'usage et exemples d'entrée, schéma strict (motif du numéro), tests de sélection ; contrôle d'accès maintenu même si la sélection se trompe.

## 6. Exercice à toi
- **E1.** Écris la définition JSON d'un outil `consulter_contrat` (nom, description, schéma).
- **E2.** stdio ou HTTP pour : (a) un serveur MCP qui lit les notes locales d'un développeur ; (b) le référentiel produits partagé par 50 développeurs ?
- **E3.** Outil, MCP ou Skill : (a) « appliquer notre checklist de revue de PR » ; (b) accès au CRM pour Claude Code et l'assistant interne ; (c) calcul de TVA dans une seule app.

## 7. Correction
<details><summary>Voir la correction</summary>

- **E1.**
```json
{"name": "consulter_contrat",
 "description": "Renvoie statut, garanties et franchise d'UN contrat du client authentifié. À utiliser quand on connaît le numéro de contrat. Ne cherche pas de client par nom (utiliser rechercher_client).",
 "input_schema": {"type": "object", "properties": {"numero": {"type": "string", "pattern": "^[A-Z]{3,4}-\\d{4}$"}},
                  "required": ["numero"], "additionalProperties": false}}
```
- **E2.** (a) **stdio** (local, personnel). (b) **HTTP** (partagé, authentification, déploiement central).
- **E3.** (a) **Skill**. (b) **MCP**. (c) **Outil personnalisé** (ou simple fonction applicative, sans LLM).
</details>

## 8. Questions d'entraînement (originales)
**Q1.** Une panne de base fait renvoyer `[]` à l'outil ; l'agent répond « client inconnu ». Correction ?
A. Prompt plus long · B. Renvoyer une erreur structurée réessayable distincte du résultat vide · C. Modèle plus grand · D. Retirer l'outil

**Q2.** (2 réponses) Arguments pour un serveur MCP plutôt qu'un outil dans l'app :
A. Plusieurs clients doivent l'utiliser · B. Une seule app, une fonction · C. Standardiser descriptions et découverte · D. Éviter toute autorisation

<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | Vide ≠ échec. |
| Q2 | **A, C** | B → outil local ; D est faux. |
</details>

## 9. À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Outil : nom, description quoi/quand/quand pas, schéma strict, erreurs distinguées, jamais de résultat inventé.
- Client (ton code exécute) vs serveur (la plateforme exécute).
- Approbation et idempotence pour les effets de bord ; jeu d'outils minimal.
- MCP : tools/resources/prompts ; stdio local vs HTTP partagé ; autorisation dans le serveur.
- Intégrés / personnalisés / MCP / Skills selon réutilisation, sécurité, contexte.
</details>

**Pratique** : [labo M3](../../../labs/m3/README.md), [serveur MCP M4](../../../labs/m4/README.md).
