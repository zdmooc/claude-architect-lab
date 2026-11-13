# M9 — Synthèse Foundations : exercice intégrateur, bilan, transition

## 1. Exercice de synthèse (à rendre)
**Contexte fictif.** Un assureur veut un **assistant de gestion des sinistres bris de glace** :
- les assurés écrivent par messagerie ;
- l'assistant consulte contrat et sinistres (référentiel), lit les factures de réparation (PDF déjà convertis en texte), et peut proposer un remboursement ;
- au-delà de 800 €, ou si l'assuré le demande, un gestionnaire humain reprend la main ;
- chaque nuit, les factures du jour sont extraites pour la comptabilité ;
- l'équipe de développement utilise Claude Code ; une revue automatique tourne en CI.

**Livrable attendu (1 à 2 pages, ton format) :**
1. **Surfaces** choisies pour chaque besoin (M0·L2) — justifie.
2. **Outils** : liste, descriptions (2 phrases), erreurs structurées, qui y a accès (M3, M4).
3. **Contrôles** : où et comment le seuil de 800 € et la vérification d'identité sont imposés (M6·L1).
4. **Extraction nocturne** : schéma (champs nullables), validation métier, batch, reprise, revue humaine (M2).
5. **Contexte et escalade** : bloc de faits, déclencheurs, contenu du transfert (M7).
6. **Claude Code** : ce qui va dans `CLAUDE.md` projet, une règle `paths`, la commande CI (M5).
7. **Mesure** : comment tu sais que l'extraction est assez bonne, par segment (M7·L3).

Je corrige avec une grille par domaine D1–D5. Un corrigé type est ci-dessous, à ouvrir **après** avoir rédigé ta version.

<details><summary>Corrigé type (proposition, d'autres choix se défendent)</summary>

1. **Surfaces** : assistant assurés → **API Messages + boucle tool use** (ou Agent SDK si besoin de hooks/sous-agents) hébergé chez l'assureur ; extraction nocturne → **Message Batches** ; développeurs → **Claude Code** ; revue → **Claude Code en CI** (`-p`) ; référentiel → **serveur MCP** réutilisable par l'agent et par Claude Code.
2. **Outils** : `verifier_identite`, `consulter_contrat`, `lister_sinistres`, `lire_facture`, `proposer_remboursement`, `transferer_gestionnaire`. Chacun avec quoi/quand/quand pas ; erreurs `{categorie, message, reessayable}` ; vide ≠ échec. L'assistant n'a **pas** d'outil de paiement direct.
3. **Contrôles** : dans le code de `proposer_remboursement` **et** un hook `PreToolUse` : refus si identité non vérifiée ; si montant > 800 € → refus + `transferer_gestionnaire`. Tests aux limites (800,00 / 800,01).
4. **Extraction** : schéma Pydantic (fournisseur, date, HT, TVA, TTC nullables, `ambiguites`) ; validation HT+TVA=TTC ; batch avec `custom_id` ; reprise sélective des échecs techniques ; échecs métier → file de revue humaine.
5. **Contexte et escalade** : bloc de faits (assuré, contrat, sinistre, montant facture, identité vérifiée oui/non, étape) ; déclencheurs : > 800 €, demande d'humain, 2 échecs d'outil, contrat résilié ; transfert structuré (qui, quoi, déjà fait, manque, cause).
6. **Claude Code** : `CLAUDE.md` projet (commandes de test, conventions, interdits : pas de secrets, données synthétiques) ; règle `paths: "src/remboursement/**"` rappelant le seuil et les tests de limite ; CI : `claude -p --output-format json --json-schema ... --allowedTools "Read,Grep,Glob"`.
7. **Mesure** : jeu annoté de factures réelles anonymisées, exactitude **par champ et par type** (garage agréé, indépendant, scan) ; seuil d'automatisation par segment ; échantillonnage continu en production.
</details>

## 2. Bilan (à remplir avec moi)
| Domaine | Poids (dossier) | Niveau (0 inconnu · 1 expliqué · 2 reproduit avec aide · 3 autonome) | Point à retravailler |
|---|---:|---|---|
| D1 Agentique | 27 % | | |
| D2 Outils & MCP | 18 % | | |
| D3 Claude Code | 20 % | | |
| D4 Prompting & sorties | 20 % | | |
| D5 Contexte & fiabilité | 15 % | | |
Échelle reprise de ton dossier (§10.3) : un outil d'orientation, **pas** une prédiction du score officiel.

## 3. Transition vers Professional (orientation provisoire)
Ce qui est **confirmé** (FAQ) : examen distinct, Foundations non obligatoire, 120 min, score 720/1000, 175 USD avant remise.
Ce qui est **à vérifier** : domaines, pondérations, nombre de questions — **guide Professional non consulté**.
D'après les objectifs du cours officiel (via ton dossier), le saut porte sur : cadrer un besoin ambigu, arbitrer coût/latence/fiabilité, contrôles d'entrée/sortie/outils, **évaluations comme critère d'acceptation**, conformité reliée à un contrôle, un propriétaire et une preuve, parties prenantes et passage en exploitation.
**Pont naturel** : ton exercice de synthèse devient le point de départ d'un **dossier d'architecture** (HLD, ADR, matrice de contrôles, plan d'évaluation, runbook) — dossier §8.

Prochaine étape quand tu seras prêt : récupérer le **guide Professional** officiel pour caler P1–P4.
