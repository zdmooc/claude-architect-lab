# V1 — Agents and Workflows (14,7 %)

Compétences du blueprint : **Agent Architecture (4,5 %)**, **Agent Construction with Claude (5,3 %)**, **Agent Patterns and Frameworks (4,9 %)**.

## Comprendre le choix d'architecture

La question n'est pas « comment écrire un agent », mais **faut-il lui donner de l'autonomie ?** Distinguer :

| Motif | Contrôle du flux | Indication |
|---|---|---|
| API single-shot | appel d'une fonction applicative | classification ou extraction simple |
| Workflow déterministe | le code choisit les étapes | processus connu, règles stables, approbations |
| Agent avec outils | le modèle choisit outil et ordre | chemin ouvert, exploration sous contraintes |
| Manager + sous-agents | délégués spécialisés, coordinateur | exploration indépendante et provenance nécessaire |

Une boucle d'outils respecte le protocole : recevoir `tool_use`, exécuter uniquement un outil **autorisé**, retourner son `tool_result` avec l'ID correspondant, conserver le contexte métier nécessaire, recommencer jusqu'à `end_turn` ou budget d'étapes. La limite `max_turns` est un garde-fou, pas un état métier.

### Claude Agent SDK et frameworks

Agent SDK : outillage, hooks, permissions, subagents et sessions gérées par le runtime. Une boucle API manuelle peut suffire avec très peu d'outils. Comparer sur besoin, gouvernance, coût et opérabilité ; **ne pas choisir un framework sans preuve**. Pour les sous-agents, décrire explicitement la tâche, le contexte, le résultat attendu et la gestion des échecs : ils n'héritent pas automatiquement de toutes les informations.

### Mémoire et humain

Conserver les faits fiables dans le système applicatif, avec leur provenance ; réduire sorties d'outils énormes et conserver les IDs critiques. Une action irréversible (paiement, suppression, envoi externe) exige contrôle déterministe + approbation humaine lorsque prévue, **dans le service**, pas seulement dans un prompt ou hook.

## Exercice / correction

Scénario : lecture d'une facture, consultation de la garantie et création de **proposition**, puis accord humain. **Correction** : workflow avec extraction ciblée, contrôle d'accès serveur, validation montant et idempotence ; ne pas exposer `payer` au modèle.

**Preuves** : [lab Agent SDK](../../../labs/labo1_support/README.md), [cas DevBank](../cas-devbank.md).
