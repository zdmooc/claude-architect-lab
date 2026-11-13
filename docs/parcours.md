# Parcours de formation

> **Recommandation pédagogique**, pas l'ordre officiel des domaines.
> Les codes D1–D5 renvoient aux domaines Foundations décrits dans le dossier de préparation
> (synthèse du guide officiel v1.0, juillet 2026 — PDF officiel non encore vérifié directement).

| Domaine | Intitulé | Poids (selon dossier) |
|---|---|---:|
| D1 | Architecture agentique et orchestration | 27 % |
| D2 | Conception des outils et intégration MCP | 18 % |
| D3 | Claude Code : configuration et workflows | 20 % |
| D4 | Prompt engineering et sorties structurées | 20 % |
| D5 | Gestion du contexte et fiabilité | 15 % |

## A. Bases nécessaires

| Module | Objectif | Notions | Pratique | Lien certif |
|---|---|---|---|---|
| M0 | Comprendre Claude | tokens, contexte, stateless, hallucinations, surfaces (claude.ai, API, Claude Code, Agent SDK, MCP) | cours gratuits Claude Academy, essais claude.ai | vocabulaire commun |
| M1 | API Messages | rôles, system, `max_tokens`, `stop_reason`, coûts, clé API | compte Console, premier script Python | prérequis D1, D4 |

## B. Parcours Foundations

| Module | Objectif | Notions | Pratique | Lien certif |
|---|---|---|---|---|
| M2 | Prompting et sorties structurées | critères explicites, few-shot, schéma JSON, validation, relance ciblée, Message Batches, `custom_id` | Labo 3 : extraction de factures fictives | D4 |
| M3 | Tool use | boucle `tool_use` → `end_turn`, descriptions, `tool_choice`, erreurs structurées | boucle codée à la main | D1, D2 |
| M4 | MCP | client/serveur, outils, ressources, `isError`, portée projet/utilisateur, secrets par variables | serveur MCP « contrats d'assurance » fictif | D2 |
| M5 | Claude Code | `CLAUDE.md`, `.claude/rules/`, commandes, Skills, plan mode, `-p`, sortie JSON | Labo 2 dans ce dépôt | D3 |
| M6 | Agentique et Agent SDK | coordinateur/sous-agents, contexte explicite, parallélisme, hooks, contrôles bloquants | Labo 1 (support) et Labo 4 (multi-agent) | D1 |
| M7 | Contexte et fiabilité | faits structurés, escalade, résultats partiels, confiance non calibrée, provenance | renforcement des labos 1, 3, 4 | D5 |

## C. Pratique et consolidation

| Module | Contenu |
|---|---|
| M8 | Les 6 scénarios, exclusions, pièges ; questions originales justifiées |
| M9 | Exercice de synthèse, bilan, transition vers Professional |

## D. Professional (orientation provisoire)

Basée uniquement sur les 4 modules du cours officiel — **pas un blueprint d'examen** ; guide Professional à consulter.

- P1. Conception de solution (cadrage, architecture, modèle, coût/latence)
- P2. Intégration entreprise et production
- P3. IA responsable, sécurité et risques
- P4. Parties prenantes, cycle de vie et adoption

Pratique : dossier d'architecture construit sur les labos (HLD, ADR, matrice de contrôles, plan d'évaluation, runbook).

## Avancement

| Module | Leçons | Statut |
|---|---|---|
| M0 | L1, L2 | rédigé |
| M1 | L1, L2 + `labs/m1` | rédigé |
| M2 | L1, L2, L3 + quiz + `labs/labo3_extraction` | rédigé |
| M3 | L1, L2, L3 + quiz + `labs/m3` | rédigé |
| M4 | L1, L2, L3 + quiz + `labs/m4` | rédigé |
| M5 | L1, L2, L3 + quiz + `labs/labo2_claude_code` | rédigé |
| M6 | L1, L2 + quiz + `labs/labo1_support`, `labs/labo4_multiagent` | rédigé |
