# Claude Certified Architect — Professional (CCAR-P)

Parcours indépendant, en français, pour concevoir et gouverner des solutions Claude en entreprise. Il complète [Foundations](../parcours.md), sans se substituer au guide officiel Anthropic.

## Référentiel et examen

- Guide d'examen **v1.0, juillet 2026**, à revalider : un nouveau guide est annoncé pour le **17/11/2026**, avec examen révisé à partir du **07/12/2026**.
- 63 questions à choix unique/multiple, 120 minutes, score minimal **720/1000 échelonné** (pas un pourcentage brut), tarif affiché **175 USD**.
- Inscription réservée, à ce jour, aux membres éligibles du **Claude Partner Network**.
- Sources : [certifications](https://anthropic-partners.skilljar.com/page/partner-certifications), [cours officiel Professional](https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional), [FAQ Anthropic](https://anthropic-partners.skilljar.com/page/faq-certifications).

## Programme : sept domaines d'examen

| Domaine (version juillet 2026) | Poids | Formation |
|---|---:|---|
| D1 Solution Design & Architecture | 17 % | [Cadrage et HLD](domaines/D1-design-architecture.md) |
| D2 Claude Models, Prompting & Context Engineering | 13 % | [Modèles et contexte](domaines/D2-modeles-contexte.md) |
| D3 Integration | 19 % | [Intégration d'entreprise](domaines/D3-integration.md) |
| D4 Evaluation, Testing & Optimization | 16 % | [Évaluation et optimisation](domaines/D4-evaluation-optimisation.md) |
| D5 Governance, Safety & Risk Management | 14 % | [Gouvernance et sécurité](domaines/D5-gouvernance-risques.md) |
| D6 Stakeholder Communication & Lifecycle Management | 14 % | [Décision et cycle de vie](domaines/D6-parties-prenantes-lifecycle.md) |
| D7 Developer Productivity & Operational Enablement | 7 % | [Exploitation et adoption](domaines/D7-productivite-exploitation.md) |

Ces sept domaines sont ceux du guide CCAR-P v1.0. Les cinq cours du parcours officiel sont organisés différemment : **Claude Platform & Solution Design**, **Enterprise Integration & Production**, **Responsible AI, Safety & Risk for Architects**, **Stakeholder Engagement, Lifecycle & GTM**, **Team Enablement & Operational Productivity**.

## Travaux pratiques livrables

[Cas d'architecture AssurNova](cas-assurnova/README.md) : un assureur IARD fictif. Le dossier constitue un vrai exercice de conception avec cadrage, HLD, ADR, contrat d'intégration, évaluation, matrice des contrôles, runbook et note pour comité d'architecture. Toutes les données sont synthétiques ; objectifs de performance et coûts sont hypothétiques avant essais.

[Questions d'entraînement originales](entrainement.md) : scénarios, arbitrages et justification des réponses. Aucun contenu d'examen réel n'est reproduit.

## Mode d'étude

Lire le cours d'un domaine, appliquer ses décisions au cas AssurNova, documenter trois arbitrages, puis vérifier le livrable avec une grille : exigences sourcées, alternatives, hypothèses, métriques, contrôles côté code, responsabilité humaine et preuve de fonctionnement. La lecture seule ne constitue pas une validation technique.

**Règle de maintenance** : revalider les poids et objectifs après publication du nouveau guide, conserver les versions dans l'historique Git et ne pas affirmer que la préparation est définitive tant que la mise à jour n'a pas été intégrée.
