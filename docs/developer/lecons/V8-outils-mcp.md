# V8 — Tools and MCPs (10,6 %)

Trois familles : conception de schémas d'outils, boucle et résultats, MCP et intégration extensible.

## Tool use

Une définition d'outil comprend **nom distinct**, description qui explique *quand* l'utiliser, schéma des arguments avec types et contraintes, résultats structurés. Décrire l'erreur : introuvable ≠ accès refusé ≠ timeout ≠ liste vide. Pour une lecture inexistante, refuser le retry non pertinent ; pour une panne temporaire, appliquer backoff borné.

La boucle : génération `tool_use` → contrôle de schéma + permissions → exécution backend → `tool_result` avec `tool_use_id` correct → nouvel appel → `end_turn`. **Ne pas inventer de tool_result** en cas de panne. Pour les effets de bord : idempotence, audit et consentement explicite.

## MCP et outils directs

MCP standardise l'exposition d'outils et ressources. Il ne résout pas la sécurité métier : authentification et ACL restent obligatoires. Un unique backend peut garder une API directe, tandis qu'un serveur MCP peut faciliter la mutualisation entre clients, sous réserve de déploiement et isolation propres.

**Progressive discovery** : ne présenter au modèle que les outils utiles au tour courant plutôt qu'une liste monolithique très longue ; choisir sur exactitude de sélection, tokens et sécurité.

### Exercice et corrigé

Deux outils : `rechercher_client(nom)` et `consulter_contrat(numero)`. Le modèle confond les deux. **Corrigé** : descriptions non ambiguës avec cas d'usage et exemples d'entrée, schéma strict, suite de tests, et droits contrôlés même si la sélection demeure erronée.

**Preuves** : [labo tool use](../../../labs/m3/README.md), [serveur MCP](../../../labs/m4/README.md).
