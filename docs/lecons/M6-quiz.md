# M6 · Synthèse et quiz

## Synthèse
- Agent SDK = boucle + outils + MCP + sous-agents + hooks, hébergé par toi.
- **Prompt guide, hook impose** : étapes obligatoires → `PreToolUse` `deny` (ou contrôle dans l'outil).
- Outils maison via serveur MCP in-process (`mcp__serveur__outil`) ; `allowed_tools` minimal ; `max_turns` = garde-fou.
- Sous-agents : contexte **explicite**, périmètres complémentaires, format de retour commun, parallélisme pour l'indépendant.
- Pipeline séquentiel si le processus est connu ; décomposition adaptative si la tâche est ouverte.
- Reprise de session : revalider les faits critiques.

## Quiz (questions originales)
**Q1.** Un agent bancaire effectue parfois des virements sans double authentification malgré une consigne en majuscules. Correction ?
A. Répéter la consigne · B. Hook `PreToolUse` qui refuse le virement tant que la double authentification n'est pas validée · C. Exemple few-shot · D. Modèle plus gros

**Q2.** Un sous-agent produit une analyse hors sujet. Sa mission était « continue l'analyse ». Cause la plus probable ?
A. Modèle trop petit · B. Il n'a pas reçu explicitement le contexte · C. Trop d'outils · D. `max_turns` trop bas

**Q3.** (2 réponses) Bonnes pratiques de décomposition :
A. Périmètres complémentaires · B. Plusieurs sous-agents sur la même question pour « être sûr » · C. Format de retour commun · D. Laisser chaque sous-agent choisir son format

**Q4.** Traitement mensuel stable : extraire → valider → produire le rapport. Structure ?
A. Décomposition adaptative · B. Pipeline séquentiel · C. Un seul agent sans outils · D. Batch de sous-agents aléatoires

**Q5.** Rôle de `max_turns` ?
A. Condition d'arrêt normale · B. Garde-fou contre les boucles · C. Limite de coût exacte · D. Nombre de sous-agents

### Questions supplémentaires (banque d'entraînement)

**Q6.** Avec l'Agent SDK, un outil de comptabilité renvoie des montants en centimes, alors que l'agent raisonne en euros et se trompe parfois d'un facteur 100. Où corriger de façon fiable ?
A. Ajouter au prompt système une consigne explicite indiquant que tous les montants renvoyés par l'outil sont en centimes · B. En demandant à l'agent de vérifier chaque montant deux fois · C. Dans le code de l'outil (ou une couche d'adaptation) qui renvoie des montants normalisés et étiquetés avec leur unité · D. En changeant de modèle

**Q7.** (2 réponses) Dans quels cas un coordinateur gagne-t-il à lancer des sous-agents en parallèle ?
A. Les sous-tâches sont indépendantes (par exemple, des sources différentes à analyser) · B. Chaque étape dépend du résultat de la précédente · C. La lecture est volumineuse et saturerait le contexte du coordinateur · D. La question est simple et se traite en une étape

**Q8.** Un agent d'analyse est interrompu le soir et doit reprendre le lendemain là où il s'était arrêté. Quelle approche est la plus fiable ?
A. Relancer le lendemain le même prompt initial : avec les mêmes outils et données, l'agent retrouvera le même cheminement · B. Demander à l'agent de « se souvenir » de la veille · C. Copier-coller la dernière réponse affichée · D. Reprendre la session si le SDK le permet, ou repartir d'un état persisté (faits établis, décisions, prochaines étapes)

**Q9.** Un sous-agent renvoie « Aucun résultat trouvé » alors que l'outil a en réalité échoué (timeout). Quel est le problème ?
A. Aucun : pour le coordinateur, un timeout et une recherche sans résultat aboutissent de toute façon à l'absence d'information · B. Un problème de performance : augmenter le timeout de l'outil suffit, le message « aucun résultat » peut rester tel quel · C. Une confusion entre échec et résultat vide : l'erreur doit être signalée comme telle au coordinateur · D. Un problème de format de réponse

## Corrigé
<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | Règle critique → hook déterministe ; A et C restent du prompt. |
| Q2 | **B** | Le sous-agent ne connaît que ce qu'on lui passe. |
| Q3 | **A, C** | Couverture complète sans doublon, synthèse facile. B gaspille ; D complique l'agrégation. |
| Q4 | **B** | Étapes stables et connues → pipeline. |
| Q5 | **B** | Garde-fou ; l'arrêt normal est la fin de la tâche. |
| Q6 | **C** | A : une consigne réduit l'erreur sans l'empêcher · B : coûteux et toujours probabiliste · C : la conversion devient déterministe et le résultat explicite pour le modèle · D : le problème est dans les données, pas dans le modèle. À retenir : Normaliser les données dans le code des outils, pas dans le prompt. |
| Q7 | **A, C** | A : l'indépendance permet le parallélisme sans coordination fine · B : dépendances séquentielles : un pipeline convient mieux · C : le sous-agent isole la lecture et ne renvoie qu'un résultat condensé · D : le coût de coordination dépasse le gain. À retenir : Paralléliser des tâches indépendantes, et isoler les lectures lourdes. |
| Q8 | **D** | A : un nouveau run peut suivre un autre chemin et refait le travail · B : le modèle ne garde aucune mémoire entre deux appels · C : perd les résultats d'outils et l'historique utile · D : la continuité vient de la session ou d'un état explicite (détails de reprise : à vérifier dans la doc du SDK). À retenir : Le modèle est sans état : la continuité se construit par la session ou un état persisté. |
| Q9 | **C** | A : « rien trouvé » et « pas pu chercher » mènent à des décisions différentes · B : allonger le timeout ne corrige pas le message trompeur : le vrai risque est une conclusion fausse · C : propagation d'erreur explicite : condition d'une décision correcte du coordinateur · D : le format n'est pas en cause, c'est le sens. À retenir : Distinguer « résultat vide » et « échec » dans ce qu'un agent remonte. |

</details>
