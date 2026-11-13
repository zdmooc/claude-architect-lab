# M6 · Leçon 1 — Agent SDK, hooks et contrôles programmatiques (D1)

> **Statut** : `labs/labo1_support/` vérifié contre `claude-agent-sdk` 0.2.181 ; le **hook est exécuté** hors API (4 tests OK) ; l'agent complet n'est **pas** exécuté.

## 1. Objectif et utilité
Construire un agent avec le **Claude Agent SDK** et y placer des **contrôles déterministes** que le modèle ne peut pas contourner.
Dossier §3.2 : « appliquer des contrôles programmatiques pour les étapes métier obligatoires », « utiliser les hooks pour contrôler les appels ». Piège cité : *une instruction dans un prompt ne remplace pas un contrôle bloquant pour une opération financière*.

## 2. Prérequis
M3 (boucle, outils), M4 (MCP), M5 (Claude Code : l'Agent SDK en est le moteur). Le SDK Python s'appuie sur Claude Code installé (coût : voir M5).

## 3. Cours
### a) Ce que fournit l'Agent SDK
`query(prompt, options)` lance la boucle complète de Claude Code : outils intégrés, MCP, sous-agents, hooks, permissions, sessions. Tu ne réécris pas la boucle de M3.

### b) Outils maison
`@tool(nom, description, schéma)` + `create_sdk_mcp_server(...)` → un serveur MCP **dans le même processus**. Les outils s'appellent alors `mcp__<serveur>__<outil>`.

### c) Hooks : intercepter les événements
| Hook | Moment | Usage typique |
|---|---|---|
| `PreToolUse` | **avant** un appel d'outil | autoriser / refuser / demander (`permissionDecision`), modifier l'entrée |
| `PostToolUse` | après | normaliser ou filtrer le résultat, journaliser |
| `UserPromptSubmit`, `Stop`, `SubagentStop`… | autres événements | garde-fous, traces |
Un hook `PreToolUse` qui renvoie `permissionDecision: "deny"` + une raison : l'appel n'a **pas lieu**, et le modèle reçoit la raison.

### d) Prompt vs hook
- **Prompt** : « vérifie l'identité avant de rembourser » → le modèle le fera *souvent*.
- **Hook** : `if not identite_verifiee: deny` → l'opération est impossible *toujours*.
Pour une étape **obligatoire** (conformité, argent, sécurité) → hook (ou contrôle dans l'outil, M3·L3).

### e) Moindre privilège et garde-fous
`allowed_tools=[...]` limite les outils ; `max_turns` est un **garde-fou**, pas une condition d'arrêt (M3·L1).

## 4. Exemple commenté : `agent_support.py`
- `ETAT["identite_verifiee"]` : l'état métier vit **dans le code**, pas dans la mémoire du modèle.
- `controle_remboursement` : 3 décisions — refus sans identité, refus au-delà de 1 000 € (avec orientation vers un humain), sinon rien (laisse passer).
- `HookMatcher(matcher=NOM_OUTIL_REMBOURSER, ...)` : le hook ne s'applique qu'à cet outil.
- Le prompt système **et** le hook : le premier guide, le second garantit.

## 5. Exercice guidé — `test_hook.py` (résultats observés)
1. Identité non vérifiée, 200 € → `deny` ✔
2. Identité vérifiée, 200 € → autorisé ✔
3. Identité vérifiée, 1 500 € → `deny` + « conseiller humain » ✔
4. Autre outil → non concerné ✔
Le contrôle est **testable sans IA** : c'est aussi un argument d'architecture.

## 6. Exercice à toi
- **E1.** Ajoute dans `test_hook.py` un cas : identité vérifiée, montant **exactement** 1 000 €. Résultat attendu selon le code ? Est-ce la règle métier souhaitée ?
- **E2.** Écris (pseudo-code) un hook `PostToolUse` qui retire les numéros IBAN des résultats d'outils avant que le modèle ne les voie. Pourquoi est-ce utile (pense D5) ?
- **E3.** Un collègue propose de supprimer le hook « puisque le prompt le dit déjà ». Réponds-lui en trois phrases.

## 7. Correction
<details><summary>Voir la correction</summary>

- **E1.** Le code teste `montant > 1000` → **1 000 € exactement passe**. Est-ce voulu ? Cela dépend de la règle métier (« au-delà de » ou « à partir de ») : à **faire préciser** et à couvrir par un test de limite.
- **E2.**
```python
async def masquer_iban(input_data, tool_use_id, context):
    texte = str(input_data.get("tool_response", ""))
    propre = re.sub(r"\bFR\d{2}(?:\s?\w{4}){5}\s?\w{3}\b", "[IBAN masqué]", texte)
    return {"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": propre}}
```
(Selon la version du SDK, vérifier comment remplacer réellement la sortie.) Utile pour D5 : on réduit le contexte au **nécessaire** et on évite qu'une donnée sensible soit reprise dans une réponse ou un journal.
- **E3.** « Le prompt guide, il ne garantit pas : un message ambigu ou une injection peut le contourner. Le hook est **déterministe** et s'exécute à chaque appel. On garde les deux : le prompt pour bien se comporter, le hook pour ne jamais franchir la limite. »

</details>
## 8. À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Agent SDK = harnais de Claude Code dans ton code (`query`, `ClaudeAgentOptions`).
- Hook `PreToolUse` → `permissionDecision: "deny"` pour une règle critique.
- Tester les **valeurs limites** des seuils.

</details>
