# M2 · Synthèse et quiz

## Synthèse
- Une consigne doit être **vérifiable** : critères explicites, raison donnée, données balisées.
- **Few-shot** : peu d'exemples, mais **difficiles et variés**, dont un cas « information absente ».
- Un prompt **guide**, un **contrôle programmatique** garantit.
- **Schéma** : nullable pour ce qui peut manquer, catégorie `autre` + précision, champ d'ambiguïtés.
- **Structure ≠ métier** : l'API garantit la forme, ton code vérifie le sens.
- **Relance** : erreur précise, nombre plafonné ; information absente → revue humaine.
- **Batch** : moins cher, asynchrone (jusqu'à 24 h) → jamais pour un contrôle bloquant ; `custom_id` ; reprise sélective.

## Quiz (questions originales d'entraînement)
Réponds par la lettre et **une phrase de justification**. Une seule bonne réponse sauf indication.

**Q1.** Un extracteur invente régulièrement des numéros de contrat quand le document n'en contient pas. Le schéma déclare `numero_contrat: str` (requis). Quelle est la meilleure première correction ?
- A. Ajouter « n'invente rien » en majuscules dans le prompt
- B. Rendre le champ nullable et ajouter un exemple few-shot où il vaut null
- C. Relancer jusqu'à trois fois quand le numéro ne figure pas dans le document
- D. Passer à un modèle plus puissant

**Q2.** Le JSON retourné respecte parfaitement le schéma, mais le TTC ne correspond pas à HT + TVA. Que montre ce cas ?
- A. Le schéma est mal conçu
- B. La conformité syntaxique ne garantit pas l'exactitude métier
- C. Il faut utiliser le mode batch
- D. Le modèle a refusé la demande

**Q3.** (2 réponses) Quelles situations conviennent au traitement par Message Batches ?
- A. Classer 50 000 courriels archivés pour une étude
- B. Valider une demande de crédit pendant que le client attend en agence
- C. Extraire les données de toutes les factures du mois, la nuit
- D. Bloquer une pull request tant que la revue de sécurité n'est pas passée

**Q4.** Après un batch, un script associe chaque résultat au document de même position dans la liste d'entrée. Quel est le risque ?
- A. Aucun, l'ordre est garanti
- B. Les résultats peuvent arriver dans un ordre différent : il faut corréler par `custom_id`
- C. Le batch coûte plus cher
- D. Les résultats expirent immédiatement

**Q5.** Un document scanné est illisible sur le montant. Après une relance ciblée, le montant est toujours absent. Que faire ?
- A. Relancer encore deux fois
- B. Demander au modèle d'estimer le montant
- C. Laisser le montant à null, noter l'ambiguïté et orienter vers une revue humaine
- D. Supprimer le document du lot

**Q6.** Quelle consigne est la plus explicite pour un assistant de banque ?
- A. « Sois prudent avec les montants »
- B. « Ne fais pas d'erreur »
- C. « Au-delà de 1 000 €, n'exécute rien : réponds que la demande est transmise à un conseiller »
- D. « Réponds de façon professionnelle »

### Questions supplémentaires (banque d'entraînement)

**Q7.** Le champ `devise` d'une extraction reçoit tantôt « euros », tantôt « EUR », tantôt « € ». Quelle correction est la plus robuste ?
A. Un `enum` dans le schéma (`EUR`, `USD`, …, `AUTRE`) avec un champ de précision pour les cas non prévus · B. Une consigne « sois cohérent » · C. Un post-traitement manuel hebdomadaire qui harmonise les valeurs de devise dans la base, après l'extraction · D. Supprimer le champ

**Q8.** Où placer le rôle et les règles stables d'un assistant, et où placer la demande variable de l'utilisateur ?
A. Tout dans le message `user`, à chaque fois · B. Tout dans le system prompt, y compris la demande de l'utilisateur, pour que le modèle lui donne la priorité maximale · C. Les règles dans un document joint · D. Le rôle et les règles stables dans le system prompt, la demande et les données variables dans le message `user`

**Q9.** On veut que Claude raisonne avant de donner un verdict, mais seul le verdict doit être parsé par le programme. Comment structurer la sortie ?
A. Interdire le raisonnement · B. Parser tout le texte avec une expression régulière · C. Séparer raisonnement et verdict (balises distinctes, ou champ `justification` avant `verdict` dans le schéma) et ne parser que le verdict · D. Demander le verdict en premier puis le raisonnement, pour que le programme trouve le verdict au début de la réponse

**Q10.** Avant d'itérer sur un prompt de classification, que faut-il définir ?
A. Le nombre de mots du prompt · B. La couleur de l'interface · C. Un jugement qualitatif d'un collègue expert, qui relira quelques sorties après chaque modification du prompt · D. Des critères mesurables sur un jeu étiqueté (exactitude par classe, taux d'« incertain »)

## Corrigé
<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | Champ requis = invention forcée. A : le prompt seul ne règle pas la contrainte du schéma. C : relancer n'ajoute pas l'info absente. D : disproportionné, même cause. |
| Q2 | **B** | Le schéma garantit la forme, pas le sens → validation métier dans le code. |
| Q3 | **A, C** | Volume, pas d'attente. B et D attendent une réponse immédiate : jamais en batch. |
| Q4 | **B** | Ordre non garanti : corréler par `custom_id`. |
| Q5 | **C** | Information absente de la source : null + ambiguïté + humain. B serait une invention. |
| Q6 | **C** | Seuil chiffré et action précise : vérifiable. Les autres sont vagues. |
| Q7 | **A** | A : le schéma contraint les valeurs et prévoit une issue pour l'imprévu · B : consigne vague, cohérence non garantie · C : coûteux et non systématique · D : perd une information métier. À retenir : Valeurs attendues fermées : `enum`, avec une option « autre ». |
| Q8 | **D** | A : répétition et risque d'oubli des règles · B : le system prompt change alors à chaque requête (et le cache ne sert plus) · C : les règles perdent leur statut d'instructions · D : séparation claire, cohérente avec le cache du préfixe stable. À retenir : System prompt = cadre stable ; message user = demande variable. |
| Q9 | **C** | A : peut réduire la qualité sur une tâche qui demande de l'analyse · B : fragile, le verdict peut être mal extrait · C : le raisonnement est conservé et le parsing reste fiable · D : le verdict ne bénéficie plus du raisonnement qui le suit. À retenir : Raisonner avant de conclure, dans une structure séparable. |
| Q10 | **D** | A : sans lien avec la qualité · B : sans rapport · C : trop peu de cas, pas de mesure · D : sans critère de succès défini à l'avance, on ne peut pas savoir si une itération améliore. À retenir : Définir les critères de succès avant d'optimiser un prompt. |

</details>
