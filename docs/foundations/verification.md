# Foundations — procédure de vérification

Cette page distingue trois niveaux : **cours rédigé**, **test de logique métier hors API**, **preuve d'intégration Claude**. Le troisième niveau n'est pas acquis par un simple commit.

## Référentiel

Leçons M0–M9 : [parcours](../parcours.md), [cours](../lecons/). Les cinq domaines de l'examen CCAR-F sont D1 agentic 27 %, D2 tool/MCP 18 %, D3 Claude Code 20 %, D4 prompting 20 %, D5 contexte/fiabilité 15 %. Source de référence : [Anthropic Academy Foundations](https://anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification).

## Tests locaux sans clé

1. Avoir Python 3.11+ et un environnement virtuel.
2. Installer les dépendances de test depuis la racine du dépôt :

~~~bash
python -m pip install -r requirements-dev.txt
python -m compileall -q labs
python -m pytest -q tests
PYTHONPATH=labs/labo2_claude_code python -m pytest -q labs/labo2_claude_code/tests
~~~

3. Vérifier le workflow [verify-offline.yml](../../.github/workflows/verify-offline.yml) sur la PR. Un résultat **vert CI** atteste ces tests seulement.

| Test | Preuve attendue | Dépendance externe |
|---|---|---|
| `tests/test_politique.py` | 800 exact autorisé, >800 rejeté ; identité, contrat, NaN/Inf invalides | aucune |
| `tests/test_outils.py` | « vide ≠ panne », statut erreur, retry | aucune |
| `tests/test_factures.py` | incohérence TTC, null, date, catégorie | Pydantic |
| `labs/labo2_claude_code/tests/test_devis.py` | calcul et borne d'âge | aucune |

## Tests complémentaires hors API, mais avec SDK

- `labs/labo1_support/test_hook.py` : vérifie **hook et outil** sans endpoint Claude ; nécessite `claude-agent-sdk` compatible. L'agent reste **non exécuté** dans le workflow offline.
- `labs/m4/test_serveur.py` : exige le SDK MCP correspondant au code et une version de Python compatible ; exécuter séparément en environnement jetable.
- Les tests de rendu du prompt et de validité des schémas ne prouvent pas l'absence d'hallucinations.

## Intégration réelle (non réalisée par ce workflow)

Sur une console Anthropic autorisée, budget plafonné et données synthétiques :
- [ ] Vérifier le modèle, tarif, quota, région et credential
- [ ] Appel M1, arrêt `end_turn`, consommation tokens
- [ ] M3 boucle d'outils avec erreur temporaire et retour `tool_result`
- [ ] M4 serveur MCP vu par un client réel, permissions et messages d'erreur
- [ ] M6 agent et hook en contexte, dont bypass de hook et multi-session
- [ ] M2 extraction 5 corpus + reprise, validation métier et provenance
- [ ] M7 maintien des faits après 20 tours, panne d'outil et escalade
- [ ] Évaluations avec preuves horodatées et aucun vrai dossier client

**Limite de sécurité** : le labo `agent_support.py` utilise un état global démonstratif ; il ne doit pas servir en production multi-tenant. Le contrôle du service réel doit réévaluer identité, accès, montants et idempotence pour chaque requête.

## Conditions de sortie Foundations

Quiz justifiés, labos hors API au vert, test d'intégration avec preuves, matrice des domaines renseignée, points faibles identifiés. Le score d'examen n'est **pas** prédictible à partir des tests de ce dépôt.
