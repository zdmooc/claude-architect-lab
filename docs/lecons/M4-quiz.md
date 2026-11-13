# M4 · Synthèse et quiz

## Synthèse
- MCP = **standard** de connexion : un serveur par système, réutilisable par tout client compatible.
- Rôles : hôte, client, serveur ; transport stdio ou HTTP.
- **Tool** = action décidée par le modèle ; **resource** = contenu de référence (URI) ; **prompt** = gabarit choisi par l'utilisateur.
- `mcp` 2.x : `MCPServer` (ex-`FastMCP`). `ToolError` → `is_error=True` avec message ; autre exception → message générique.
- Portée **projet** (`.mcp.json`, versionné) vs **utilisateur** (personnel).
- Secrets : `${VARIABLE}`, jamais en clair dans un fichier versionné.
- Hébergement de MCP en conteneurs, OAuth : hors programme Foundations (dossier).

## Quiz (questions originales)
**Q1.** Le guide de style rédactionnel de l'entreprise (stable, consulté souvent) doit être exposé via MCP. Primitive la plus adaptée ?
A. Tool · B. Resource · C. Prompt · D. Aucune

**Q2.** Un outil MCP plante sur un contrat inconnu avec une `KeyError` non gérée. Que voit le modèle ?
A. Le détail de la `KeyError` · B. Un message générique d'échec de l'outil · C. Rien, l'appel est ignoré · D. Un résultat vide sans erreur

**Q3.** (2 réponses) Bonnes pratiques pour un `.mcp.json` committé :
A. Référencer les secrets via `${VAR}` · B. Mettre le jeton de test en clair « temporairement » · C. Ne déclarer que les serveurs utiles au projet · D. Y déclarer ses serveurs personnels

**Q4.** Un développeur veut un serveur MCP pour sa to-do personnelle, dans tous ses projets. Portée ?
A. Projet · B. Utilisateur · C. Dans le code de l'application · D. Dans le prompt système

**Q5.** Pourquoi lever une erreur explicite et structurée plutôt que laisser l'exception remonter ?
A. Pour réduire la latence · B. Pour que le modèle sache s'il doit corriger, réessayer ou escalader · C. Parce que MCP l'impose · D. Pour éviter la journalisation

### Questions supplémentaires (banque d'entraînement)

**Q6.** Deux serveurs MCP exposent des outils aux noms proches, `get_client` et `fetch_customer`, et le modèle choisit souvent le mauvais. Quelle correction est la plus efficace ?
A. Ajouter au prompt système une règle demandant de toujours préférer `get_client`, sauf pour les clients étrangers · B. Augmenter la température · C. Supprimer un des deux serveurs au hasard · D. Distinguer clairement les outils (noms explicites, description qui dit quand utiliser l'un ou l'autre) ou les fusionner en un seul

**Q7.** Un outil de recherche renvoie 5 000 lignes à chaque appel et sature le contexte. Quelle conception adopter ?
A. Paginer et filtrer côté outil, ne renvoyer que les champs utiles, avec un total et un curseur pour la suite · B. Tout renvoyer : le modèle saura trier lui-même les lignes pertinentes, et la fenêtre de contexte est assez grande · C. Augmenter la fenêtre de contexte · D. Supprimer l'outil

## Corrigé
<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | Contenu de référence stable → resource. |
| Q2 | **B** | Exception non gérée → message générique ; seul `ToolError` transmet ton message. |
| Q3 | **A, C** | Secrets en `${VAR}`, serveurs utiles au projet. B : un jeton commité est compromis. D : le personnel va en portée utilisateur. |
| Q4 | **B** | Personnel et multi-projets → utilisateur. |
| Q5 | **B** | Le modèle a besoin de savoir quoi faire ensuite. C : pas une obligation du protocole. |
| Q6 | **D** | A : contourne l'ambiguïté par une règle cachée au lieu de la corriger dans les outils · B : rend le choix plus aléatoire, pas plus juste · C : risque de perdre une capacité nécessaire · D : le choix d'outil dépend des noms et descriptions : c'est là qu'on corrige. À retenir : Choix d'outil ambigu : corriger les noms et descriptions, ou consolider. |
| Q7 | **A** | A : l'outil maîtrise le volume et donne au modèle de quoi continuer · B : coût élevé et dilution de l'attention · C : ne règle pas le coût ni la dilution · D : perd la capacité au lieu de la concevoir correctement. À retenir : Un outil renvoie peu, utile, et paginé. |

</details>
