# M7 · Leçon 1 — Préserver les faits, réduire le bruit (D5)

> **Statut** : `labs/m7/contexte.py` **exécuté** (observé : sortie d'outil réduite de 216 à 61 caractères, IBAN retiré).

## 1. Objectif et utilité
Garder l'agent fiable sur les **longues** interactions : les faits critiques ne se perdent pas, le contexte n'est pas saturé de bruit.
D5 (15 %, selon le dossier) : préserver montants, dates, identifiants et attentes dans des faits structurés ; réduire les sorties d'outils ; positionner clairement les éléments importants.

## 2. Prérequis
M0·L1 (contexte fini, stateless), M1·L2 (historique), M3 (sorties d'outils).

## 3. Cours
### a) Le problème
Au fil des tours, l'historique grossit, des résumés automatiques ou des troncatures interviennent, et un détail donné au tour 2 (« contrat AUTO-4471, attente : avant le 20/11 ») se perd ou se dilue.

### b) Faits structurés
Un **bloc dédié** (`<faits_dossier>…</faits_dossier>`), maintenu par l'application, **renvoyé à chaque tour** et placé **en tête**. Il contient : identifiants, montants, dates, **attentes du client**.
👉 Comme l'état d'une saga : on ne le reconstruit pas à partir des logs, on le maintient explicitement.

### c) Réduire les sorties d'outils
Un référentiel renvoie 200 lignes dont 3 utiles. On **filtre côté code** avant de les donner au modèle : moins de tokens, moins de distraction, moins de données sensibles exposées.

### d) Longues investigations
Pour un travail sur plusieurs heures ou sessions : **scratchpad** (notes de travail), **résumés intermédiaires**, **état persistant** (fichier ou base) relu au début de chaque étape. Le résumé doit **conserver** les faits critiques, pas seulement l'ambiance.

## 4. Exemple commenté : `contexte.py`
- `bloc_faits()` : rendu JSON stable, balisé.
- `reduire()` : liste blanche de champs → `historique_technique`, `metadonnees_internes` et `iban` disparaissent.

## 5. Exercice guidé
Une conversation de 40 tours a été résumée automatiquement : « Le client a un problème de vitrage et est mécontent. » Qu'est-ce qui a été perdu ? Le numéro de contrat, la date, le montant estimé, l'échéance attendue. → Le résumé doit être **guidé** (« conserve identifiants, montants, dates, engagements ») ou remplacé par le bloc de faits.

## 6. Exercice à toi
- **E1.** Liste les champs du bloc de faits pour un dossier de **demande de crédit immobilier**.
- **E2.** Un outil renvoie un dossier client complet (120 champs). L'agent ne doit répondre qu'à « où en est mon dossier ? ». Quels champs gardes-tu, et où fais-tu le filtrage ?
- **E3.** Pourquoi placer le bloc de faits **en tête** plutôt qu'au milieu de l'historique ?

## 7. Correction
<details><summary>Voir la correction</summary>

- **E1.** Client (id), projet (adresse, prix), montant demandé, durée, taux proposé, apport, revenus, pièces reçues et manquantes, étape du dossier, échéances, décisions déjà prises, conseiller.
- **E2.** Garder : numéro de dossier, étape, date de dernière mise à jour, pièces manquantes, prochaine action. Filtrer **dans l'outil** (ou un hook `PostToolUse`), avant que le modèle ne voie le résultat.
- **E3.** Le modèle exploite moins bien l'information **noyée au milieu** d'un long contexte ; en tête, elle est vue à chaque tour et ne disparaît pas lors d'un résumé.

</details>
## 8. À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- **Bloc de faits** structuré, renvoyé à chaque tour, en tête.
- Réduire les résultats d'outils **à la source**.
- Résumé guidé qui préserve montants, dates, engagements.

</details>
