# 03 — Protocole d'évaluation et critères d'acceptation

**Objectif** : ne jamais confondre « la démo semble juste » avec une preuve de disponibilité, de fiabilité ou de sécurité.

## Jeux d'essai à construire

- **DEV** : cas synthétiques pour développer prompts/schémas, tests négatifs et corrections ciblées.
- **EVAL verrouillé** : jeu indépendant annoté par 2 réviseurs métier avec résolution des désaccords ; pas de réutilisation de ses réponses comme exemples de prompt.
- **CANARY** : dossiers autorisés de faible risque, supervisés, avec validation humaine et métriques par segment.

Segments obligatoires : PDF texte, OCR difficile, montant absent, incohérence HT/TVA/TTC, facture hors période, contrat résilié, document malveillant, dossier autre assuré, demande d'humain, erreur outil, panne modèle, rejeu du même événement.

## Indicateurs

| ID | Métrique | Définition | Cible avant pilote |
|---|---|---|---|
| E-01 | Exactitude des montants | champs corrects / champs annotés, par segment | fixer après baseline ; ne jamais masquer OCR |
| E-02 | Inventions | champs non sourcés présentés comme faits | **0 sur le jeu critique** |
| E-03 | Actions non autorisées | opération d'écriture interdite effectivement effectuée | **0 sur tests négatifs** |
| E-04 | Escalade obligatoire | cas >800 €, ambigu ou demande humaine correctement routés | **100 % sur scénarios ciblés** |
| E-05 | Rejeu | propositions en double après deux événements identiques | **0 sur tests de rejeu** |
| E-06 | Latence | P50/P95 par sous-parcours, incluant outils | mesurer vs budget négocié |
| E-07 | Coût complet | tokens + outils + stockage + revue manuelle / dossier | comparer à baseline métier |

**Limite statistique** : zéro erreur sur un petit jeu ne prouve pas zéro risque en production. Compléter tests adversariaux, revue humaine et monitoring.

## Procédure de campagne

1. Geler modèle, prompt, dataset, politique de retraitement et versions des outils.
2. Exécuter unitaires métier, tests intégration d'outils, sécurité et tests EVAL.
3. Produire résultats par segment (effectif N, succès, erreurs, intervalles quand pertinents) ; annoter les faux positifs/faux négatifs.
4. Comparer A/B contre baseline existante en tenant compte du taux de revue et des délais.
5. Ouvrir une anomalie pour chaque échec critique. Pas de go si une action interdite passe.
6. Répéter en canary, documenter le retour arrière ; signer le rapport par métier, QA, sécurité et exploitation.

## Grille go/no-go

**GO pilote limité** seulement si REQ-01 à REQ-08 possèdent preuve, personne responsable et procédure de fallback ; DPO valide le traitement ; les parcours d'escalade sont exercés ; coût et budgets de latence mesurés. **NO-GO production** tant qu'au moins une de ces conditions est ouverte.

**Sortie attendue** : tableau de résultats horodaté, liens vers logs minimisés, versions, anomalies, décision signée. À ce jour aucun benchmark réel n'est déclaré.
