# M2 · Leçon 2 — Sorties structurées : schéma, validation, relance (D4)

> **Statut du code** : extraits tirés de `labs/labo3_extraction/`, vérifiés contre le SDK `anthropic` 2.8.0 (`messages.parse`, `output_format`, `transform_schema`), compilés ; la validation métier a été **exécutée localement** sur un exemple (résultat observé : l'incohérence HT+TVA≠TTC est bien détectée). **Aucun appel API exécuté.**

## 1. Objectif et utilité
Obtenir du modèle des données **exploitables par un programme**, et savoir que « JSON valide » ne veut pas dire « données justes ».
Compétences D4 du dossier : schéma avec champs facultatifs et nullables, catégories extensibles, conformité syntaxique vs exactitude métier, erreurs précises pour la relance, limites de la relance.

## 2. Prérequis
M1·L1 (blocs de contenu, `stop_reason`), M2·L1 (consignes explicites). Notions de JSON Schema (tu les as via OpenAPI).

## 3. Cours

### a) Garantir la structure
L'API sait **contraindre** la réponse à un schéma JSON (`output_config.format`). En Python, le plus simple :
```python
response = client.messages.parse(model=MODEL, max_tokens=2000,
                                 system=SYSTEM, messages=messages,
                                 output_format=Facture)   # modèle Pydantic
facture = response.parsed_output                          # objet validé
```
👉 Analogie : un contrat OpenAPI côté serveur. La forme est garantie ; le contenu reste à vérifier.

### b) Concevoir le schéma pour ne pas forcer l'invention
| Choix | Pourquoi |
|---|---|
| **Nullable** (`Optional[str]`) quand l'info peut manquer | sinon le modèle est *obligé* de remplir → il invente |
| **Catégorie fermée + `"autre"` + précision** | les cas imprévus ne sont pas tordus pour rentrer dans une case |
| **Champ `ambiguites`** | le modèle signale l'incertitude au lieu de trancher en silence |

Piège d'examen : un champ **requis et non nullable** pour une donnée parfois absente fabrique des hallucinations *par conception*.

### c) Deux validations différentes
1. **Structure** (syntaxe) : le JSON respecte le schéma → garanti par l'API.
2. **Métier** (sémantique) : HT + TVA = TTC ? date plausible ? → **ton code** (`validation.py`).
Le schéma ne peut pas savoir qu'une facture à 7 300 € TTC pour 6 000 € HT + 1 200 € de TVA est fausse.

### d) Relancer intelligemment
- On renvoie **l'erreur précise** (« HT 6000 + TVA 1200 ≠ TTC 7300 ») et pas « c'est faux, recommence ».
- On **plafonne** les relances (ici 1).
- Si l'information **n'existe pas** dans la source (facture illisible), relancer ne la fera pas apparaître → `null` + **revue humaine**.

## 4. Exemple commenté : `labs/labo3_extraction/extraire.py`
1. `messages.parse(..., output_format=Facture)` → structure garantie.
2. `if response.stop_reason != "end_turn"` → on n'exploite pas une réponse tronquée ou refusée.
3. `valider(facture)` → règles métier.
4. En cas d'erreur : on ajoute la réponse + **les erreurs précises** à l'historique et on relance **une fois**.
5. Toujours en erreur → on marque `VALIDATION_ECHOUEE` dans `ambiguites` : l'humain prend le relais.

## 5. Exercice guidé
Facture F003 : « HT 6 000 €, TVA 1 200 €, TTC 7 300 € ».
1. Le schéma accepte-t-il ces valeurs ? Oui, ce sont trois nombres.
2. `valider()` ? Détecte l'incohérence (résultat observé localement).
3. Relance ciblée → le modèle relit. Mais la **source elle-même** est incohérente : il recopiera fidèlement 7 300.
4. Conclusion : la relance échoue → revue humaine. **C'est le bon comportement** : le système n'a pas « corrigé » une facture fournisseur à la place du comptable.

## 6. Exercice à toi
- **E1.** Dans `schema.py`, pourquoi `fournisseur` est-il le seul champ texte non nullable ? Est-ce un bon choix ? Argumente.
- **E2.** Ajoute (sur papier ou dans le code) une règle métier à `validation.py` pour détecter un `montant_tva` qui ne correspond à aucun taux usuel (20 %, 10 %, 5,5 %, 2,1 %). Quel message d'erreur précis renverrais-tu ?
- **E3.** Facture F005 (illisible). Décris ce que le système **doit** produire, champ par champ pour les montants, et pourquoi il ne faut pas relancer trois fois.

## 7. Correction
<details><summary>Voir la correction</summary>

- **E1.** Une facture sans fournisseur identifiable est inexploitable, d'où le champ requis. Mais si le nom est illisible, le modèle sera **forcé d'inventer**. Variante plus sûre : le rendre nullable et envoyer en revue humaine quand il vaut `null`. Les deux choix se défendent si on l'argumente.
- **E2.** Règle : si HT et TVA présents, `round(tva/ht, 3)` doit être proche de 0,20 / 0,10 / 0,055 / 0,021. Message : « montant_tva (73,00) = 14,6 % de montant_ht (500,00) : aucun taux usuel (20 %, 10 %, 5,5 %, 2,1 %). Relis la TVA dans la facture. »
- **E3.** Montants HT et TTC `null` (illisibles), date `null` ou ambiguë, `ambiguites` renseigné (« chiffres illisibles ») → **revue humaine**. Relancer ne fera pas apparaître une information absente de la source : on gaspille des appels et on pousse le modèle à deviner.

</details>

## 8. À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Le schéma garantit la **forme** ; ton code vérifie le **sens**.
- Champs **nullables** pour ce qui peut manquer ; catégorie `autre` + précision ; champ d'ambiguïtés.
- Relance : **erreur précise**, nombre **plafonné** ; info absente → humain.

</details>
