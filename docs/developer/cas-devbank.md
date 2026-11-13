# Cas intégrateur Developer — DevBank (100 % fictif)

## Demande

Développer un assistant **interne** d'aide à la lecture de dossiers bancaires synthétiques. Cas V1 : obtenir la garantie d'un contrat et proposer un résumé sourcé ; **pas de paiement, virement ni modification de compte**. Il doit refuser l'accès inter-clients et préserver la cohérence du contexte sur plusieurs tours.

### Exigences traçables

| ID | Besoin | Test/gate |
|---|---|---|
| DEV-01 | API Messages, arrêt et contenu correctement gérés | `end_turn` vs `max_tokens` |
| DEV-02 | Dossier accessible uniquement au titulaire | test IDOR/BOLA côté outil |
| DEV-03 | Pas d'outil de paiement | revue du catalogue et tests permissions |
| DEV-04 | Montant extrait cohérent | null si absent, HT/TVA/TTC vérifiés |
| DEV-05 | Panne transitoire bornée | backoff/repli, pas de retry permanent |
| DEV-06 | Historique long et provenance | faits vérifiés, source/version, compaction |
| DEV-07 | Conformité/risque | traces minimales, secrets hors dépôt |
| DEV-08 | Coût/qualité | éval par segment, montant réel des coûts |
| DEV-09 | Déploiement sûr | unitaires, intégration, canary, rollback |

## Design proposé

~~~mermaid
flowchart LR
 UI[Portail authentifié] --> GW[API Gateway et autorisation]
 GW --> ORCH[Orchestrateur de workflow]
 ORCH --> TOOL[Outils de lecture à scopes limités]
 ORCH --> CLAUDE[Claude API : résumé/extraction]
 CLAUDE --> VAL[Validation de schéma et sources]
 TOOL --> VAL
 VAL --> REVIEW[Réponse vérifiée ou revue humaine]
 ORCH --> AUDIT[Trace corrélée et coût]
~~~

### Choix d'ingénierie

- **Workflow** (pas agent autonome) : séquence connue et absence de décision financière déléguée.
- **Client API injectable** : tests locaux avec un fake, pas besoin de clé.
- **Modèle configurable** : choix basé sur benchmark, pas identifiant hardcodé dans l'application.
- **Autorisation** dans le backend de contrats et non dans un texte au modèle.
- **Données** : `SYN-CONTRAT-001` et `SYN-CLIENT-01`, aucun vrai compte bancaire.
- **Résilience** : erreur structurée, canal de reprise humaine, idempotence si un jour on autorise l'écriture.

### Niveau de preuve

| Niveau | Statut |
|---|---|
| Cadrage/HLD | écrit, non approuvé en entreprise |
| Contrôles offline | à exécuter par pytest en CI |
| API Claude réelle | **non validée** |
| MCP / Agent SDK connectés | **non validés** |
| Benchmark modèle, SLO, coût | **non mesurés** |
| Production | **non autorisée** |

## Exercice de revue

Simuler une facture tronquée `stop_reason=max_tokens`, un contrat appartenant à un autre utilisateur et une panne API. Pour chaque cas : résultat attendu, couche responsable, journal minimal, correction testée. **Correction type** : rejeter le résultat partiel, refuser l'accès dans la couche service, passer en file humaine si indisponible ; jamais fabriquer une garantie.
