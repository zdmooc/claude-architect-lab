# M7 · Leçon 2 — Escalade, erreurs et résultats partiels (D5)

> **Statut** : `labs/m7/escalade.py` **exécuté** (observé : 3 déclencheurs détectés, 1 cas sans escalade, transfert structuré produit).

## 1. Objectif et utilité
Savoir **quand** un agent doit passer la main, **comment** il le fait, et comment il propage échecs et résultats partiels sans les cacher.
Dossier D5 : déclencheurs d'escalade explicites, respect de la demande d'humain, propagation des erreurs, résultats partiels et tentatives.

## 2. Prérequis
M3·L2 (erreurs structurées), M6·L1 (hooks).

## 3. Cours
### a) Déclencheurs explicites
Des règles **écrites et testables** : demande d'un humain, seuil de montant, échecs répétés, sujet sensible (décès, litige). Pas « escalade si tu n'es pas sûr ».

### b) Le client demande un humain → on transfère
Sans insister, sans « laissez-moi d'abord essayer ». C'est une règle de qualité de service citée dans le dossier.

### c) Le score de confiance du modèle
Un « je suis sûr à 90 % » produit par le modèle **n'est pas une probabilité calibrée** (dossier §3.6). Ne pas en faire le déclencheur principal d'escalade. Si on veut des seuils de confiance, on les **calibre** sur un jeu annoté (L3).

### d) Transfert structuré
L'humain qui reprend ne doit pas tout relire : identifiant, faits, **cause** de l'escalade, **action proposée**, **tentatives déjà faites**, **points non résolus** (dossier §7.1).

### e) Propager, ne pas masquer
Un sous-agent en échec → le coordinateur reçoit l'erreur **et** ce qui a été fait. Un rapport partiel est signalé comme partiel. Pire que l'échec : la **couverture complète fictive**.

## 4. Exemple commenté : `escalade.py`
- `doit_escalader()` renvoie une **cause**, pas un booléen : elle alimente le transfert.
- `Transfert` : dataclass avec les 6 rubriques ci-dessus.

## 5. Exercice guidé
L'outil de suivi échoue deux fois. L'agent répond : « Votre dossier est en cours de traitement. » Problème : il **invente** un statut. Correct : « Je n'arrive pas à consulter votre dossier pour l'instant. Je transmets à un conseiller avec votre demande. » + transfert structuré (cause : échecs répétés).

## 6. Exercice à toi
- **E1.** Ajoute dans `escalade.py` un déclencheur « sujet sensible » (décès, accident corporel). Donne deux mots-clés et explique la limite de la détection par mots-clés.
- **E2.** Rédige le transfert structuré pour : client C-1002, contrat HAB-2210 résilié, demande d'indemnisation dégâts des eaux, outil d'historique en panne.
- **E3.** Pourquoi « escalade si ta confiance < 70 % » est-il un mauvais déclencheur principal ?

## 7. Correction
<details><summary>Voir la correction</summary>

- **E1.** Mots-clés : « décès », « blessé ». Limite : synonymes, fautes, négations (« personne n'est blessé »), contexte. À compléter par une classification du modèle **et** des règles, avec tests.
- **E2.** `{"client": "C-1002", "contrat": "HAB-2210", "statut_contrat": "résilié", "demande": "indemnisation dégâts des eaux", "cause_escalade": "contrat résilié + outil historique indisponible", "deja_fait": ["contrat consulté"], "manque": ["historique des sinistres"], "action_suggeree": "vérifier date de résiliation vs date du sinistre"}`.
- **E3.** La confiance auto-déclarée est **mal calibrée** et non vérifiable. Les déclencheurs principaux doivent être **explicites et testables** : demande d'humain, seuil, échecs répétés, sujet sensible.

</details>
## 8. À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Déclencheurs explicites : demande d'un humain, seuil, échecs d'outil, sujet sensible.
- Transfert **structuré** : qui, quoi, déjà fait, ce qui manque, cause.
- Distinguer erreur réessayable / non réessayable / résultat vide.

</details>
