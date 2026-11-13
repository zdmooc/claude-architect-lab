# D1 — Solution Design & Architecture (17 %)

**But** : transformer une demande métier incertaine en architecture dont on sait expliquer la valeur, les limites, le comportement en échec et les choix rejetés.

## 1. Déroulement d'une mission

1. **Discovery** : objectifs mesurables, parcours AS-IS, acteurs, exceptions, préjudice d'une erreur, processus sans IA, volumétrie et contraintes de souveraineté. Faire préciser « automatiser les sinistres » en critères observables.
2. **Frontière du système** : entrées/sorties, données personnelles, identités, actions autorisées, validations humaines, SLA/SLO. Ne pas laisser le LLM décider des droits.
3. **Choix du motif** :

| Architecture | Indication | Compromis |
|---|---|---|
| Workflow déterministe + extraction LLM | étapes stables, règles financières, conformité | moins flexible, mais testable |
| Single-shot / LLM augmenté d'outils | analyse documentaire avec quelques lectures | besoin de boucles et timeouts |
| Agent autonome | exploration peu structurée et actions non critiques | coût, autonomie, dérive |
| Multi-agent | spécialités indépendantes, gain mesuré par délégation | orchestration, provenance, latence |

4. **Comparer** via ADR : exactitude par cas, délai P95, coût par dossier, réversibilité, sécurité, exploitabilité. Une optimisation annoncée sans mesure est une hypothèse.
5. **Définir les échecs** : timeout Claude, contrat inaccessible, réponse incohérente, facture illisible, suspicion fraude, demande d'un humain. Prévoir un chemin de sortie sûr pour chaque situation.

## 2. Cas AssurNova

Assureur fictif, 10 000 dossiers bris de glace/mois. L'IA classe les demandes, lit les factures, prépare une proposition **sans paiement automatique**. Le moteur de règles valide statut du contrat, droits du demandeur, seuil d'escalade de 800 € et idempotence. Un gestionnaire approuve les cas sensibles.

Décision proposée : **workflow orchestré + appels Claude ciblés** en V1. Justification : étapes connues, action financière sensible et réduction de la surface agentique. Réexaminer si la mesure de tâches ouvertes démontre un bénéfice net des agents.

## 3. Livrable

Produire un HLD comportant au moins : vue contexte, composants, séquence nominale, chemins d'échec, diagramme de confiance, budget latence, surfaces de responsabilité, journalisation, autorité de décision. Chaque exigence est liée à un composant, un responsable et un test.

**Question de revue** : que reste-t-il opérationnel si Claude n'est pas disponible pendant 30 minutes ? Si la réponse est « tout le SI s'arrête », revoir la découpe.

Voir [cadrage](../cas-assurnova/00-cadrage.md), [HLD](../cas-assurnova/01-hld.md), [ADR](../cas-assurnova/02-adr.md).
