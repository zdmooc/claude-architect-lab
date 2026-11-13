# M2 · Leçon 3 — Message Batches et labo 3 de bout en bout (D4)

> **Statut du code** : `labs/labo3_extraction/batch_extraire.py` — imports et helpers vérifiés contre le SDK `anthropic` 2.8.0, compilé, **non exécuté** contre l'API.
> Caractéristiques des batches : documentation SDK au 13/11/2026 et dossier §3.5. À revérifier avant un projet réel.

## 1. Objectif et utilité
Savoir **quand** utiliser le traitement par lots (et quand ne pas l'utiliser), et l'implémenter proprement : corrélation par `custom_id`, reprise sélective.
Ce choix synchrone / batch est une compétence D4 explicitement listée dans le dossier.

## 2. Prérequis
M2·L2 (schéma, validation, relance).

## 3. Cours

### a) Ce qu'est un batch
Tu envoies **beaucoup de requêtes d'un coup**, l'API les traite **en asynchrone**, tu récupères les résultats plus tard.
D'après la documentation :
- environ **50 % moins cher** que l'appel synchrone ;
- la plupart des lots finissent en **moins d'une heure**, mais le délai peut aller **jusqu'à 24 h** ;
- les résultats restent disponibles **29 jours**.

👉 Analogie : un job batch de nuit (JCL, CronJob Kubernetes) vs un appel transactionnel.

### b) Quand l'utiliser
| Situation | Choix |
|---|---|
| Extraction de 10 000 factures pour la clôture du mois | **Batch** |
| Un conseiller attend une réponse à l'écran | **Synchrone** |
| Contrôle qui **bloque une fusion de code** ou une transaction | **Synchrone** — aucune garantie de latence en batch |

Piège d'examen cité par le dossier : utiliser un batch pour un contrôle bloquant.

### c) Corrélation : `custom_id`
Chaque requête porte un `custom_id` (ici le nom du fichier). **Les résultats reviennent dans n'importe quel ordre** : on indexe par `custom_id`, jamais par position.
👉 Comme un `correlationId` JMS sur une file MQ.

### d) Reprise sélective
Chaque résultat a un type : `succeeded`, `errored`, `canceled`, `expired`.
On **ne relance que** les documents en échec technique. Les documents en échec **métier** vont en revue humaine (M2·L2), pas en relance aveugle.

## 4. Exemple commenté : `batch_extraire.py`
1. `requete(custom_id, texte)` : même prompt et même schéma qu'en synchrone (`transform_schema(Facture)` adapte le schéma Pydantic aux exigences de l'API).
2. `lancer()` : crée le lot, interroge l'état toutes les 60 s jusqu'à `ended`.
3. `collecter()` : trois paniers — `ok`, `a_reprendre` (technique), `revue_humaine` (métier).
4. Fin du script : relance **seulement** `a_reprendre`.

## 5. Exercice guidé
Sur 100 factures : 93 `succeeded`, 4 `errored`, 3 `expired`. Parmi les 93, 6 échouent la validation métier.
- À relancer en batch : 4 + 3 = **7**.
- En revue humaine : **6**.
- Prêtes : **87**.
- Erreur classique : relancer les 100 → double coût, et les 6 erreurs métier reviendront identiques.

## 6. Exercice à toi
- **E1.** Une équipe veut utiliser un batch pour vérifier la conformité de chaque virement **avant** exécution. Ton avis, en deux phrases.
- **E2.** Un développeur associe les résultats aux documents avec `zip(fichiers, resultats)`. Quel est le bug ?
- **E3.** (avec clé, facultatif — **coût faible mais réel, préviens-moi avant**) Lance `extraire.py` sur les 5 factures du corpus. Pour chacune, note : valide / relancée / revue humaine. Compare avec les « cas pièges » annoncés dans le README du labo.

## 7. Correction
<details><summary>Voir la correction</summary>

- **E1.** Non : le batch n'a **aucune garantie de délai** (jusqu'à 24 h) alors que le virement attend la décision. Il faut un appel **synchrone**, plus un contrôle programmatique.
- **E2.** Les résultats arrivent **dans n'importe quel ordre** → `zip` associe des résultats aux mauvais documents. Corréler par `custom_id`.
- **E3.** Attendu d'après les pièges : F001 valide ; F002 valide avec HT `null` ; F003 relancée puis revue humaine (source incohérente) ; F004 valide, catégorie `autre` + « espaces verts » ; F005 revue humaine (illisible). Tes résultats réels sont ton **résultat observé**.

</details>

## 8. À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Batch : environ 50 % moins cher, **asynchrone** (jusqu'à 24 h) → jamais pour un contrôle bloquant.
- **`custom_id`** pour corréler ; ordre non garanti.
- Reprise **sélective** des échecs techniques ; échecs métier → humain.

</details>
