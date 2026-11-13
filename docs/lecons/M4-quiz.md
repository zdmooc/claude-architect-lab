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

*Correction après tes réponses.*
