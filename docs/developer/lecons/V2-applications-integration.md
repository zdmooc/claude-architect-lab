# V2 — Applications and Integration (33,1 %)

**Domaine le plus lourd.** Six familles de compétences : comprendre les besoins (**3,4 %**), cycle de vie (**2,8 %**), mécanismes API (**6,8 %**), bases d'ingénierie logicielle (**7,4 %**), conception d'application Claude (**8,6 %**), gestion des configurations (**4,1 %**).

## 1. Choisir le bon mode d'intégration

L'API **Messages** reçoit un `model`, un `max_tokens`, une liste de `messages`, un éventuel `system`, et des `tools`. Les tours passés ne sont pas stockés par magie : **l'application gère l'historique**. Interpréter les réponses :
- `end_turn` : réponse finale de Claude ;
- `tool_use` : une exécution d'outil est nécessaire dans le client ;
- `max_tokens` : sortie interrompue ; **ne pas utiliser comme réponse complète** ;
- `stop_sequence` : arrêt déclenché par une séquence configurée.

Ne pas agréger aveuglément tous les blocs : une réponse peut mélanger texte, `tool_use` et autres types. Contrôler la structure et le statut avant le traitement métier.

### Modes de charge

| Mode | Pour quoi | Point de vigilance |
|---|---|---|
| Synchrone | interface interactive et réponse rapide | timeout et budget latence |
| Streaming | perception temps réel et longs résultats | **chunks partiels** : valider seulement la réponse complète |
| Batch | gros volumes non urgents | suivi `custom_id`, erreurs partielles, reprise |
| PDF / image | lecture multimodale | permission du fichier, qualité du document et preuve de source |
| Cache de prompt | longs préfixes identiques | variabilité du préfixe, TTL et facturation réelle |

### API, cloud et SDK

SDK officiel vs REST brut : le SDK peut faciliter retries/types et streaming ; vérifier sa **version**. Sur Bedrock/Vertex ou un fournisseur compatible, vérifier modèles/régions, credentials, quotas et variations supportées ; ne pas supposer que toutes les fonctions existent au même moment.

## 2. Contrats et logiciel de production

- Schéma JSON précis, `required` et champs nullable si l'information peut manquer ; **valider après génération**.
- Distinguer erreurs 4xx permanentes, rate limits et 5xx transitoires ; backoff/jitter **bornés** quand l'opération est sûre.
- Propager `correlation_id`, fixer timeout, annulation, quota tokens, idempotence et logs minimisés.
- Conserver version du modèle/prompt/schema/config ; tests unitaires, intégration et revues en PR.
- Ne jamais confondre simple statut HTTP 200 avec un **résultat métier fiable**.

## 3. Cas pratique

Pour classer 2 000 pièces : utiliser batch si temps non critique ; conserver `custom_id`, vérifier les erreurs individuelles, relancer **sélectivement** et rejeter les sorties partielles. Pour un chat client, streaming peut améliorer le ressenti, mais afficher « proposition provisoire » tant que la validation finale n'est pas réalisée.

**À exécuter** : [lab client Messages API fictif](../../../labs/developer_foundations/README.md), [M1](../../../labs/m1/README.md), [M3](../../../labs/m3/README.md).
