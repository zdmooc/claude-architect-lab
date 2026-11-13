# M3 · Synthèse et quiz

## Synthèse
- Claude **demande**, ton code **exécute**. La boucle s'arrête sur `stop_reason == "end_turn"`, pas sur la présence de texte.
- Réponse complète de l'assistant **puis** tous les `tool_result` dans **un seul** message user, liés par `tool_use_id`.
- Le compteur d'itérations est un **garde-fou** ; l'atteindre est une anomalie → escalade.
- **Descriptions** : quoi, quand, quand pas, formats. Les améliorer avant d'ajouter du routage.
- **Erreurs structurées** (`is_error`, catégorie, réessayable). **Vide ≠ échec.**
- Outils **limités au rôle**. Contrôles critiques **dans le code** de l'outil.
- `tool_choice` : auto / any / forcé / none — vérifier ce que le modèle utilisé accepte.
- Tool Runner = boucle fournie, outils à toi. ≠ Agent SDK.

## Quiz (questions originales)
**Q1.** Une réponse a `stop_reason: "tool_use"` et contient aussi du texte. Que fait la boucle ?
A. Affiche le texte et s'arrête · B. Exécute les outils, renvoie les résultats et relance · C. Ignore les outils · D. Relance sans rien ajouter

**Q2.** L'agent confond régulièrement `chercher_contrat` et `chercher_client`. Meilleure première action ?
A. Ajouter un agent routeur · B. Passer à un modèle plus gros · C. Réécrire les descriptions pour dire quand utiliser chacun et quand ne pas l'utiliser · D. Supprimer un des deux outils

**Q3.** La base clients est en panne ; l'outil renvoie une liste vide. L'agent répond « client inconnu ». Cause racine ?
A. Le prompt est trop long · B. L'outil ne distingue pas échec d'accès et absence de résultat · C. `max_tokens` trop bas · D. Il manque un exemple few-shot

**Q4.** (2 réponses) Bonnes pratiques pour renvoyer 3 résultats d'outils demandés dans la même réponse :
A. Un seul message user avec les 3 `tool_result` · B. Trois messages user successifs · C. Chaque `tool_result` porte le `tool_use_id` correspondant · D. Ne renvoyer que les résultats réussis

**Q5.** Une règle impose une vérification d'identité avant toute modification d'IBAN. Où l'implémenter ?
A. Dans le prompt système, en gras · B. Dans le code : `modifier_iban` refuse si l'identité n'est pas vérifiée · C. Dans un exemple few-shot · D. Dans la description de l'outil uniquement

**Q6.** La boucle atteint `MAX_TOURS`. Que faire ?
A. Renvoyer la dernière réponse comme finale · B. Augmenter `MAX_TOURS` à 100 · C. Traiter comme une anomalie : journaliser et escalader · D. Relancer depuis zéro

*Correction après tes réponses.*
