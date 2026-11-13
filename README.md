# Claude Architect Lab

Laboratoire francophone de préparation aux quatre certifications **Claude Certified Associate (CCAO-F), Developer (CCDV-F) et Architect (CCAR-F, CCAR-P)**. Contenus personnels et **données exclusivement synthétiques** : pas de secrets, de dossiers clients, ni de questions officielles copiées.

## Certifications couvertes — 4 parcours

| Certification | Code | Programme et exercices | Statut |
|---|---|---|---|
| **Associate – Foundations** | CCAO-F | [7 domaines et cas ConseilNova](docs/associate/README.md) | cours rédigés ; 14 QCM ; pas d'examen complet |
| **Developer – Foundations** | CCDV-F | [8 domaines et lab Developer](docs/developer/README.md) | cours rédigés ; 16 QCM ; tests offline |
| **Architect – Foundations** | CCAR-F | [M0–M9](docs/parcours.md) | cours/labos ; intégration API à confirmer |
| **Architect – Professional** | CCAR-P | [P1–P7 et AssurNova](docs/professional/README.md) | cours/cas ; intégration à confirmer |

**Suivi des domaines, des preuves et des examens blancs manquants** : [tableau de bord des certifications](docs/certifications/suivi.md). Les montants, domaines et conditions d'inscription sont ceux des guides connus ; vérifier la version courante sur [Anthropic Partner Academy](https://anthropic-partners.skilljar.com/page/partner-certifications). Les contenus de ce dépôt ne sont **pas des supports officiels**.

## Entrées directes

- [Cours Associate](docs/associate/README.md) et [cours Developer](docs/developer/README.md)
- [Cours Architect Foundations](docs/lecons/) et [8 dossiers de labs](labs/)
- [Tests et limites de validation Foundations](docs/foundations/verification.md)
- [Cours Professional par domaine](docs/professional/README.md)
- [Cas fil rouge AssurNova — 7 livrables d'architecture](docs/professional/cas-assurnova/README.md)
- [21 questions Professional originales](docs/professional/entrainement.md)

## Tester hors API

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q tests
PYTHONPATH=labs/labo2_claude_code python -m pytest -q labs/labo2_claude_code/tests
```

Le pipeline GitHub Actions `.github/workflows/verify-offline.yml` automatise ces tests, y compris les nouveaux tests du labo Developer, **sans API key ni dépense de tokens**. Il ne constitue **pas** un test d'intégration à Claude : SDK, MCP et appels réseau doivent être validés séparément. Pour le labo Agent SDK : suivre [labs/labo1_support/README.md](labs/labo1_support/README.md).

## Référentiel officiel et limite d'accès

Le programme d'examen peut évoluer ; les guides de l'[Anthropic Partner Academy](https://anthropic-partners.skilljar.com/page/partner-certifications) sont la source d'autorité. **Les inscriptions aux examens sont actuellement réservées aux personnes éligibles d'organisations du Claude Partner Network**. Un dépôt de préparation n'est pas une certification.

## Hygiène

Python, configuration locale et secrets exclus par `.gitignore`. Ne jamais committer de vraie clé API, pièce d'identité, document confidentiel ou données client. Les coûts, SLO et tests du cas AssurNova sont des **hypothèses pédagogiques**, pas des performances mesurées.
