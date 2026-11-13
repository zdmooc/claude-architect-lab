# Claude Architect Lab

Laboratoire francophone de préparation aux certifications **Claude Certified Architect — Foundations (CCAR-F)** et **Professional (CCAR-P)**. Contenus personnels et **données exclusivement synthétiques** : pas de secrets, de dossiers clients, ni de questions officielles copiées.

## Deux parcours

| Parcours | Niveau | Point d'entrée | État |
|---|---|---|---|
| **Foundations (CCAR-F)** | agents, tools, MCP, Claude Code, prompting, fiabilité | [Parcours M0–M9](docs/parcours.md) | cours, quiz et labos rédigés sur cette branche ; validation partielle |
| **Professional (CCAR-P)** | conception entreprise, intégration, sécurité, évaluation, gouvernance, exploitation | [Programme D1–D7](docs/professional/README.md) | sept cours + étude de cas + 21 questions originales ; architecture simulée |

## Entrées directes

- [Cours Foundations](docs/lecons/) et [8 dossiers de labs](labs/)
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

Le pipeline GitHub Actions `.github/workflows/verify-offline.yml` automatise ces tests **sans API key ni dépense de tokens**. Il ne constitue **pas** un test d'intégration à Claude : SDK, MCP et appels réseau doivent être validés séparément. Pour le labo Agent SDK : suivre [labs/labo1_support/README.md](labs/labo1_support/README.md).

## Référentiel officiel et limite d'accès

Le programme d'examen peut évoluer ; les guides de l'[Anthropic Partner Academy](https://anthropic-partners.skilljar.com/page/partner-certifications) sont la source d'autorité. **Les inscriptions aux examens sont actuellement réservées aux personnes éligibles d'organisations du Claude Partner Network**. Un dépôt de préparation n'est pas une certification.

## Hygiène

Python, configuration locale et secrets exclus par `.gitignore`. Ne jamais committer de vraie clé API, pièce d'identité, document confidentiel ou données client. Les coûts, SLO et tests du cas AssurNova sont des **hypothèses pédagogiques**, pas des performances mesurées.
