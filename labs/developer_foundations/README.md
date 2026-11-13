# CCDV-F — Laboratoire Developer hors API

**But** : tester un vrai design d'intégration Claude sans clé API et sans frais. Le client Messages est injecté ; les tests utilisent un **fake** qui reproduit quelques champs du SDK officiel. Cela prouve le contrat de notre application, **pas la compatibilité complète ni la qualité de Claude**.

## Fichiers

| Fichier | Responsabilité |
|---|---|
| `gateway.py` | requête Messages injectée ; distinguer `end_turn`, `tool_use`, `max_tokens`, `stop_sequence` et refus de blocs inattendus |
| `contracts.py` | contrôle d'autorisation côté serveur, isolation par utilisateur, résumé synthétique sans outil d'écriture |
| `pricing.py` | calcul monétaire exact en Decimal de la consommation token, tarifs **fournis par l'appelant** |
| `tests/test_developer_gateway.py` | clients fictifs et cas d'erreur/troncature |
| `tests/test_developer_contracts.py` | BOLA, refus d'accès et cas autorisé |
| `tests/test_developer_pricing.py` | coût, arrondis, valeurs invalides |

## Lancer hors API

~~~bash
python -m pip install -r requirements-dev.txt
python -m pytest -q tests
~~~

Le workflow GitHub Actions `verify-offline.yml` exécute ces tests automatiquement. Les noms de modèles, tarifs, fenêtres de contexte et fonctionnalités sont volontairement **non hardcodés** : ils doivent être vérifiés avant un essai réel.

## Passer ensuite à un test réel (action volontaire)

1. Configurer un compte et un modèle Claude autorisés dans un environnement isolé, avec **budget et quotas**.
2. Injecter le SDK officiel `anthropic.Anthropic()` dans `gateway.complete_text`; aucun secret dans le dépôt.
3. Exécuter un test `end_turn`, un test de troncature et un test de `tool_use`, avec logs minimisés.
4. Tester streaming, batch, vision/PDF, accès inter-contrats, pannes réseau et autorisations dans les **véritables services**.
5. Compléter une grille d'évaluation versionnée et publier les métriques réellement observées.

**Danger** : `contracts.py` est une simulation purement en mémoire avec données fictives ; il n'implémente ni OIDC, ni base multi-tenant, ni audit durable. **Ne jamais le déployer tel quel en banque.**
