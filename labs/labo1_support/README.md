# Labo 1 — Agent de support avec contrôles métier (M6, D1/D5)

- `agent_support.py` : Agent SDK, 2 outils via serveur MCP in-process, **hook PreToolUse** qui bloque le remboursement sans identité vérifiée ou au-delà de 800 €.
- **Défense en profondeur** : la règle déterministe (`politique.py`) est utilisée par le hook **et** par l'outil, avec contrôle du contrat autorisé, par le hook **et** dans l'outil `rembourser`. Si le hook est retiré, mal ciblé, ou si l'outil est appelé par un autre client, l'outil refuse quand même (erreur structurée, non réessayable).
- `test_hook.py` : tests **sans API** : hook, outil appelé sans hook, limite à 800,00 €, montants invalides.

```bash
pip install claude-agent-sdk
cd labs/labo1_support && python test_hook.py      # sans clé
python agent_support.py                            # nécessite Claude Code installé + accès (coût)
```
Statut : `test_hook.py` **exécuté** par le formateur (résultats à vérifier sur cette branche) et à réexécuter manuellement avec la version de `claude-agent-sdk` installée ; agent complet **non exécuté**.


**Limite de la démonstration** : l'état `ETAT` est global, donc **non adapté à plusieurs utilisateurs simultanés**. En production, identité, scopes et droits contractuels sont liés à chaque requête dans un backend sécurisé ; le lab ne doit jamais effectuer de paiement.
