# Claude Certified Developer — Foundations (CCDV-F)

**Public** : ingénieurs logiciels / AI, développeurs Python ou TypeScript, technical leads. Parcours de préparation francophone **basé sur le guide d'examen v1.0 (juillet 2026)** ; exemples en Python standard library, sans nécessité de clé API pour le premier niveau de tests.

**Format** : **53 questions**, 120 minutes, score minimal **720/1000 échelonné** (pas 72 % brut), **125 USD**, validité 12 mois, examen en anglais. L'accès aux examens exige actuellement un e-mail professionnel d'une organisation **Claude Partner Network**. Vérifier les informations sur la [page officielle de certifications](https://anthropic-partners.skilljar.com/page/partner-certifications) et sur [Pearson VUE](https://www.pearsonvue.com/us/en/anthropic.html).

## Eight domains — blueprint Developer v1.0

| # | Domaine officiel | Poids | Leçon |
|---|---|---:|---|
| V1 | Agents and Workflows | 14,7 % | [Architecture et boucles agentiques](lecons/V1-agents-workflows.md) |
| V2 | Applications and Integration | **33,1 %** | [Messages API, streaming, intégration](lecons/V2-applications-integration.md) |
| V3 | Claude Code | 3,1 % | [Environnements et permissions](lecons/V3-claude-code.md) |
| V4 | Eval, Testing, and Debugging | 2,6 % | [Tests et diagnostic](lecons/V4-evaluations-tests.md) |
| V5 | Model Selection and Optimization | 16,8 % | [Modèles, coûts, tokens](lecons/V5-modeles-optimisation.md) |
| V6 | Prompt and Context Engineering | 11,0 % | [Prompts et contexte](lecons/V6-prompt-contexte.md) |
| V7 | Security and Safety | 8,1 % | [Sécurité et sûreté](lecons/V7-securite.md) |
| V8 | Tools and MCPs | 10,6 % | [Outils et MCP](lecons/V8-outils-mcp.md) |
| | **Total** | **100 %** | |

**Les 25 compétences** du blueprint sont regroupées dans ces huit domaines (3 + 6 + 1 + 1 + 4 + 3 + 4 + 3). Les poids ne sont pas uniformes : **V2 et V5 comptent à eux deux pour 49,9 % de l'examen**.

## Correspondance aux cinq cours officiels Developer

| Cours de l'Anthropic Partner Academy | Domaines associés |
|---|---|
| MSO Foundations | V5, V6 |
| Production-Grade Prompting, Agents & Tool Use | V1, V6, V8 |
| Claude Code, MCP & Integration | V2, V3, V8 |
| Production Engineering, Evals & Security | V2, V4, V7 |
| Accelerators & IP Contribution | V2, V3, V4 |

Ceci est une **correspondance pédagogique** : l'ordre des cours et des domaines d'examen est différent. [Cours officiel Developer](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations).

## Travaux pratiques

- [Lab Developer autonome hors API](../../labs/developer_foundations/README.md) : adapter `anthropic.messages.create` avec un client fictif, contrôler `stop_reason`, validation d'extraction, autorisation de lecture, reprise et coût.
- [Cas fil rouge DevBank](cas-devbank.md) : dossier d'intégration, tool use, tracing, sécurité, critères de sortie.
- [16 questions originales corrigées](entrainement.md) : révision ciblée, **pas** un examen blanc de 53 questions.
- Réutiliser les laboratoires Foundations : [M1](../../labs/m1/README.md), [M3](../../labs/m3/README.md), [M4](../../labs/m4/README.md), [Labo 1](../../labs/labo1_support/README.md).

### Validation

~~~bash
python -m pip install -r requirements-dev.txt
python -m pytest -q tests
~~~

L'exécution hors API vérifie uniquement la logique Python locale. **Aucun test de facturation, de quota, de streaming en réseau ou de déploiement Claude n'est validé sans accès dédié.** Ne pas exposer de clé API dans les logs ou Git.

## Étapes de progression

1. Étudier **V2 Applications** en profondeur, puis V5 et V1.
2. Compléter V6–V8 et les labs d'API/outils.
3. Comprendre V3 et V4, sans confondre leur faible poids d'examen avec une faible importance de production.
4. Défendre le cas DevBank devant une revue contradictoire et exécuter l'évaluation segmentée.
5. Revenir au guide officiel pour vérifier chaque compétence avant l'examen.

**Statut** : cours et labos pédagogiques en développement ; CI offline ne prouve pas un produit en production ni un niveau de certification.
