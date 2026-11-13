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

*Correction et points à retravailler après tes réponses.*
