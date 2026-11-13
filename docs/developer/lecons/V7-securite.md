# V7 — Security and Safety (8,1 %)

Quatre familles : mécanismes de défense, sécurité des agents, hooks/permissions, identité-secrets et gestion des clés.

## Modèle de menace

Entrées dangereuses : prompt injection par document ou retour d'outil, accès inter-dossiers (BOLA), token d'administration fourni au modèle, exfiltration de contenu, outil d'écriture trop large, coût incontrôlé par boucle, divulgation dans les traces.

**Defense in depth** :
1. Contrôle OIDC et ownership **côté serveur** ; chaque outil n'expose que les contrats de l'utilisateur authentifié.
2. Validation des arguments, schémas et actions avant appel ; allowlist d'outils, moindre privilège, limites d'exécution.
3. Hooks `PreToolUse` et permissions pour réduire le risque, mais ne pas leur confier l'unique règle d'argent.
4. Secrets depuis un coffre, hors code et hors contexte du modèle ; rotation, egress contrôlé, journalisation minimisée.
5. Approbation humaine avant actions irréversibles et reprise en mode sûr si permission/service indisponible.

Le refus écrit dans la réponse n'est pas une preuve que l'action a été bloquée : tester **l'effet réellement exécuté**, notamment en appel direct de l'API métier.

## Exercice et corrigé

Un agent dispose de `list_all_customer_contracts()` avec token administrateur, bien que sa mission soit de répondre pour un seul client. **Correction** : retirer l'outil global, service `get_contract` avec scope/ownership contrôlés, compte de service restreint, tests BOLA et journaux.

**À tester** : [politique métier](../../../labs/labo1_support/politique.py), [matrice risques](../../professional/cas-assurnova/04-controles-raci.md).
