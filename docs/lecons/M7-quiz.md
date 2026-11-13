# M7 · Synthèse et quiz

## Synthèse
- **Bloc de faits structurés**, maintenu par l'application, renvoyé à chaque tour, en tête.
- **Réduire** les sorties d'outils côté code (liste blanche) : moins de bruit, moins de données sensibles.
- Longues investigations : scratchpad, résumés guidés, état persistant.
- **Escalade** : déclencheurs explicites ; demande d'humain respectée ; transfert structuré (faits, cause, action, tentatives, points ouverts).
- **Confiance déclarée ≠ probabilité** ; seuils calibrés sur jeu annoté.
- Propager erreurs et résultats partiels ; jamais de couverture fictive.
- **Provenance** (extrait, source, date) ; **contradictions conservées** ; mesure **par type et par champ**.

## Quiz (questions originales)
**Q1.** Après 50 tours, l'agent oublie le montant convenu au début. Meilleure correction ?
A. Augmenter `max_tokens` · B. Maintenir un bloc de faits structurés renvoyé à chaque tour · C. Demander au client de répéter · D. Changer de modèle

**Q2.** Un client écrit « je veux parler à quelqu'un ». L'agent pense pouvoir résoudre seul. Que faire ?
A. Essayer encore deux échanges · B. Transférer à un humain avec un transfert structuré · C. Ignorer · D. Demander une confirmation trois fois

**Q3.** Exactitude globale 92 %. Que vérifier avant d'automatiser ?
A. Rien · B. L'exactitude par type de document et par champ · C. La latence · D. Le nombre de tokens

**Q4.** Deux sources donnent des dates différentes pour un même événement. Bon comportement ?
A. Garder la plus récente sans le dire · B. Faire la moyenne · C. Conserver les deux, attribuées et datées, et le signaler · D. Ne rien rapporter

**Q5.** (2 réponses) Bons déclencheurs d'escalade :
A. Montant au-delà d'un seuil défini · B. « Je ne suis pas sûr » selon le modèle, seul critère · C. Échecs répétés d'un outil · D. Longueur de la question

### Questions supplémentaires (banque d'entraînement)

**Q6.** Un agent interroge trois systèmes, mais un seul ne répond pas. Comment présenter le résultat à l'utilisateur ?
A. Présenter le résultat comme complet, pour ne pas inquiéter l'utilisateur avec un incident technique passager · B. Ne rien répondre tant que tout n'est pas disponible · C. Estimer les données manquantes · D. Répondre avec ce qui est confirmé, signaler la source manquante et son impact, et proposer une relance ou une escalade

**Q7.** Pour une décision automatique, le modèle annonce une « confiance de 95 % ». Comment l'utiliser ?
A. L'utiliser comme seuil d'automatisation : au-dessus de 90 % de confiance déclarée, la décision part sans revue · B. L'ignorer totalement · C. La calibrer d'abord sur des cas étiquetés, et la combiner à des règles objectives · D. La multiplier par deux pour être prudent

**Q8.** La revue humaine ne peut couvrir que 10 % des cas traités par l'agent. Comment choisir les cas à revoir ?
A. Un échantillon stratifié, avec priorité aux cas à risque (montant élevé, nouveaux types de demandes) · B. Les 10 % premiers de la journée · C. Un tirage purement aléatoire sur l'ensemble des cas, qui donne une estimation non biaisée de la qualité globale · D. Les cas les plus courts

**Q9.** Un agent de support escalade une conversation vers un conseiller. Que doit contenir le transfert ?
A. Rien de particulier : le conseiller a accès à tout l'historique de la conversation et pourra le relire · B. Uniquement le nom du client · C. Le dernier message du client · D. Un résumé structuré : demande, vérifications et actions faites, raison de l'escalade

## Corrigé
<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | Préserver les faits critiques hors du flux qui se dilue. A ne concerne que la réponse. |
| Q2 | **B** | Demande explicite d'humain = déclencheur immédiat, transfert structuré. |
| Q3 | **B** | Un global élevé peut masquer un segment défaillant. |
| Q4 | **C** | Provenance : conserver, attribuer, dater, signaler. |
| Q5 | **A, C** | Explicites et testables. B : confiance mal calibrée comme seul critère. |
| Q6 | **D** | A : résultat présenté comme fiable alors qu'il est partiel · B : bloque l'utilisateur sans raison · C : invention de données · D : transparence sur la couverture et suite d'action claire. À retenir : Résultat partiel : dire ce qui est confirmé et ce qui manque. |
| Q7 | **C** | A : une confiance déclarée n'est pas calibrée par défaut · B : elle peut être un signal utile une fois calibrée · C : la confiance doit être vérifiée contre des résultats réels · D : n'a aucun sens. À retenir : Une confiance déclarée se calibre avant de servir de seuil. |
| Q8 | **A** | A : couvre toutes les catégories et concentre l'effort sur le risque · B : biais temporel, cas à risque manqués · C : utile pour mesurer, mais insuffisant pour concentrer la revue sur le risque · D : la longueur n'est pas un indicateur de risque. À retenir : Revue humaine limitée : la cibler sur le risque, sans perdre la vue d'ensemble. |
| Q9 | **D** | A : fait perdre du temps et risque des oublis · B : insuffisant pour reprendre le dossier · C : manque le contexte et l'historique des actions · D : le conseiller reprend sans redemander ce qui est déjà connu. À retenir : Une escalade transmet un dossier structuré, pas une conversation brute. |

</details>
