# M8 — Les 6 scénarios : raisonner comme à l'examen

> D'après ton dossier (§3.7), l'examen présente **4 scénarios tirés parmi 6**, 60 questions en 120 minutes. Les questions ci-dessous sont **originales**, écrites pour l'entraînement ; elles ne reproduisent aucune question d'examen.

## 1. Méthode de résolution (recommandation pédagogique)
Pour chaque question :
1. **Quel est le vrai problème ?** (souvent caché derrière le symptôme)
2. **Quelle contrainte compte ?** (argent, délai, conformité, humain qui attend…)
3. **Quelle est la correction à la cause racine, la plus proportionnée ?**
4. **Pourquoi les autres options sont-elles fausses ?** (trop lourdes, à côté, ou elles traitent le symptôme)

Raisonnements récurrents relevés par ton dossier (§10.1) : corriger la cause racine ; préférer la solution proportionnée ; améliorer les descriptions d'outils avant d'ajouter du routage ; contrôle programmatique pour une contrainte critique ; préserver l'information utile ; distinguer échec technique et résultat vide.

## 2. Hors périmètre — ne pas y passer de temps
Fine-tuning, architecture interne du modèle, embeddings et bases vectorielles, computer use, vision, streaming, OAuth et rotation de clés, configurations cloud spécifiques, hébergement de MCP en conteneurs, tokenisation, détails du prompt caching (dossier §3.8). Une option de réponse qui t'emmène là est souvent un **distracteur**.

## 3. Les scénarios, modules associés et questions d'entraînement

### S1 — Agent de support client (M3, M6, M7)
*Outils métier, vérification préalable, erreurs, escalade.*
- **S1-Q1.** L'agent rembourse parfois avant d'avoir vérifié l'identité. Prompt déjà explicite. Meilleure action ?
  A. Ajouter des exemples · B. Hook/contrôle qui bloque `rembourser` tant que l'identité n'est pas vérifiée · C. Réduire la température · D. Ajouter un sous-agent vérificateur
- **S1-Q2.** Le client envoie un message avec trois demandes (adresse, attestation, réclamation). L'agent ne traite que la première. Cause la plus probable et correction ?
  A. `max_tokens` trop bas · B. La consigne ne demande pas d'identifier et traiter toutes les demandes ; l'ajouter et vérifier la complétude · C. Il faut trois agents · D. Batch

### S2 — Génération de code avec Claude Code (M5)
*Configuration d'équipe, commandes, planification, contexte.*
- **S2-Q1.** Les conventions ne sont appliquées que pour un développeur. Cause ?
  A. Elles sont dans sa config utilisateur, pas dans le `CLAUDE.md` projet · B. Le modèle est différent · C. Il manque une Skill · D. Il faut le plan mode
- **S2-Q2.** Migration de framework sur 60 fichiers aux dépendances floues. Premier geste ?
  A. Exécution directe · B. Plan mode puis validation · C. CI non interactive · D. Une commande personnelle

### S3 — Recherche multi-agent (M6, M7)
*Décomposition, délégation, agrégation, provenance.*
- **S3-Q1.** Le rapport final omet entièrement l'analyse réglementaire. Les sous-agents sont bons. Cause ?
  A. Modèle trop petit · B. La décomposition du coordinateur n'a pas couvert ce volet · C. Trop de parallélisme · D. Sources contradictoires
- **S3-Q2.** Deux sous-agents rapportent des chiffres différents pour le même coût. Que doit faire la synthèse ?
  A. Moyenne · B. Garder le plus élevé · C. Conserver les deux, attribués et datés, et le signaler · D. Relancer jusqu'à accord

### S4 — Productivité développeur (M4, M5)
*Exploration de code, outils intégrés, MCP.*
- **S4-Q1.** Trouver tous les fichiers `*.properties` du dépôt. Outil intégré le plus adapté ?
  A. Bash avec `cat` · B. Glob · C. Edit · D. Write
- **S4-Q2.** L'équipe veut que Claude Code interroge le référentiel interne des API. Le jeton d'accès est personnel. Configuration ?
  A. Serveur MCP en portée projet avec `${API_TOKEN}` dans `.mcp.json` · B. Jeton en clair dans `.mcp.json` · C. Jeton dans `CLAUDE.md` · D. Copier-coller la doc dans chaque prompt

### S5 — Claude Code en CI (M5, M2)
*Revue, génération de tests, sorties structurées, faux positifs.*
- **S5-Q1.** La revue automatique signale 40 « problèmes » par PR, l'équipe l'ignore. Meilleure correction ?
  A. La désactiver · B. Exiger gravité + uniquement les problèmes réels, ne bloquer que sur « bloquant » · C. Passer en batch · D. Augmenter `max_turns`
- **S5-Q2.** Le pipeline doit lire le résultat de la revue. Options ? (2 réponses)
  A. `-p` · B. `--output-format json` (+ `--json-schema`) · C. Mode interactif · D. Plan mode

### S6 — Extraction de données (M2, M7)
*Schémas, validation, cas absents, revue humaine.*
- **S6-Q1.** Le modèle invente des numéros de SIRET absents des documents. Le champ est requis non nullable. Correction ?
  A. Relances multiples · B. Champ nullable + exemple où il est absent · C. Modèle plus gros · D. Batch
- **S6-Q2.** Clôture mensuelle de 30 000 factures, résultat attendu sous 48 h, budget serré. Mode ?
  A. Synchrone · B. Message Batches avec `custom_id` et reprise sélective · C. Un agent multi-sous-agents · D. Claude Code en CI

## Corrigé
<details><summary>Voir les réponses</summary>

| Q | Réponse | Pourquoi | Pourquoi pas les autres |
|---|---|---|---|
| S1-Q1 | **B** | Le prompt est déjà explicite : il faut un contrôle déterministe. | A, C : toujours probabiliste. D : lourd, et toujours un modèle. |
| S1-Q2 | **B** | Cause = consigne incomplète ; ajouter « identifie toutes les demandes » + vérification de complétude. | A : la réponse n'est pas coupée. C, D : disproportionné ou hors sujet. |
| S2-Q1 | **A** | Config utilisateur invisible pour l'équipe → `CLAUDE.md` projet. | B, C, D : ne traitent pas la portée. |
| S2-Q2 | **B** | Large et flou : planifier puis valider. | A : risqué. C, D : hors sujet. |
| S3-Q1 | **B** | Les sous-agents font ce qu'on leur confie : trou de décomposition. | A : les sous-agents sont bons. C, D : n'expliquent pas une omission totale. |
| S3-Q2 | **C** | Provenance conservée et signalée. | A, B : perte d'information. D : coût sans garantie. |
| S4-Q1 | **B** | Glob = recherche de fichiers par motif. | A lit le contenu ; C, D modifient. |
| S4-Q2 | **A** | Serveur partagé en projet, jeton personnel via variable d'environnement de chacun. | B, C : secret en clair. D : ni maintenable ni à jour. |
| S5-Q1 | **B** | Faux positifs → gravité + précision ; on rétablit la confiance. | A : perte de la revue. C, D : hors sujet. |
| S5-Q2 | **A, B** | Non interactif + sortie structurée. | C : interactif. D : ne produit pas un résultat lisible par le pipeline à lui seul. |
| S6-Q1 | **B** | Champ requis = invention forcée ; nullable + exemple d'absence. | A : n'ajoute pas l'info. C, D : même cause. |
| S6-Q2 | **B** | Volume, 48 h, budget → batch (≤ 24 h, environ −50 %). | A : plus cher. C, D : inadapté. |

</details>
