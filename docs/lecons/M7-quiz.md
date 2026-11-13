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

## Corrigé
<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | Préserver les faits critiques hors du flux qui se dilue. A ne concerne que la réponse. |
| Q2 | **B** | Demande explicite d'humain = déclencheur immédiat, transfert structuré. |
| Q3 | **B** | Un global élevé peut masquer un segment défaillant. |
| Q4 | **C** | Provenance : conserver, attribuer, dater, signaler. |
| Q5 | **A, C** | Explicites et testables. B : confiance mal calibrée comme seul critère. |

</details>
