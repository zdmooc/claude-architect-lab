# M2 · Leçon 1 — Prompts explicites et exemples few-shot (D4)

> Sources : dossier de préparation §3.5 (synthèse du guide Foundations), documentation API Claude (13/11/2026).

## 1. Objectif et utilité
Écrire des consignes qui donnent un comportement **prévisible** : critères explicites plutôt que vœux pieux, exemples pour les cas ambigus.
D4 pèse 20 % de l'examen (selon le dossier). La première compétence listée : « remplacer les consignes vagues par des critères explicites ».

## 2. Prérequis
M1 (rôles `system` / `user`, appel de base).

## 3. Cours

### a) Une consigne vague ne se teste pas
| Vague | Explicite |
|---|---|
| « Sois concis » | « 3 phrases maximum, sans liste » |
| « Signale les réclamations graves » | « Grave = mention d'un avocat, d'une plainte, d'un montant > 5 000 €, ou d'un risque de santé » |
| « Ne dis pas de bêtises » | « Si l'information n'est pas dans le document fourni, réponds : *je ne trouve pas cette information* » |

👉 Analogie : une exigence non fonctionnelle « le système doit être rapide » vs « p95 < 300 ms ». Seule la seconde est vérifiable.

### b) Ce qui va où
- **`system`** : le rôle, les règles stables, le format attendu.
- **`messages` (user)** : la donnée du moment (le document, la question).
- **Balises** pour délimiter les données : `<document>…</document>`. Le modèle distingue mieux la consigne du contenu, et un texte malveillant dans le document passe moins facilement pour une consigne.

### c) Expliquer le *pourquoi*
Les modèles récents suivent mieux une règle quand on donne la raison :
« Réponds sans jargon, **car les lecteurs sont des assurés non spécialistes** ».
La raison aide le modèle à généraliser aux cas que la règle n'a pas prévus.

### d) Few-shot : des exemples pour les cas difficiles
Un **exemple** vaut souvent mieux qu'un paragraphe de règles, surtout pour :
- les **cas ambigus** (deux catégories possibles) ;
- un **format** précis ;
- la **frontière** entre deux décisions (« ceci est grave / ceci ne l'est pas »).

Règles d'or :
- choisir des exemples **variés** et **difficiles**, pas trois fois le cas facile ;
- montrer aussi le cas « **information absente** » → le modèle apprend qu'il a le droit de répondre `null` ;
- éviter que tous les exemples aient la même réponse (sinon biais).

### e) Ce que le prompt ne fait pas
Un prompt **guide**, il ne **garantit** pas. Pour une règle critique (montant max d'un remboursement, vérification d'identité), on ajoute un **contrôle par programme**. C'est un piège récurrent de l'examen (D1, dossier §3.2).

## 4. Exemple concret commenté
Tri de courriels clients d'un assureur :
```text
system :
Tu classes les courriels clients d'un assureur auto.
Catégories : sinistre, contrat, facturation, reclamation, autre.
- "reclamation" = le client exprime un mécontentement sur un traitement déjà en cours.
  Un premier signalement de sinistre, même énervé, est "sinistre".
- Si le courriel couvre plusieurs sujets, choisis le sujet de la DEMANDE principale.
Réponds uniquement par le nom de la catégorie.

<exemple>
Courriel : "Ça fait 3 semaines que j'attends l'expert pour mon pare-brise, c'est inadmissible."
Catégorie : reclamation
</exemple>
<exemple>
Courriel : "On m'a embouti ce matin sur le parking, je suis furieux, que dois-je faire ?"
Catégorie : sinistre
</exemple>
```
Commentaires :
- la définition de `reclamation` **tranche la frontière** avec `sinistre` ;
- les deux exemples portent **exactement** sur cette frontière (colère dans les deux cas) ;
- la règle « plusieurs sujets » traite un cas que les exemples ne couvrent pas.

## 5. Exercice guidé
Prompt d'origine : *« Résume ce dossier sinistre de façon professionnelle. »*
Problèmes : « résume » (quelle longueur ?), « professionnelle » (pour qui ?), aucune consigne sur les infos manquantes.
Réécriture :
```text
Tu résumes un dossier sinistre pour un gestionnaire qui reprend le dossier
d'un collègue absent (il doit pouvoir agir sans relire tout le dossier).
Format : 
- Faits : 3 puces max (date, nature, montant estimé).
- Statut : une phrase.
- Prochaine action : une phrase.
Si une information manque dans le dossier, écris "non indiqué" — n'estime pas.
```
Chaque critère est maintenant **vérifiable** par un relecteur ou un test.

## 6. Exercice à toi
- **E1.** Réécris cette consigne en critères explicites : *« Détecte les demandes urgentes dans les messages des clients bancaires. »*
- **E2.** Pour ta consigne, écris **deux exemples few-shot** qui se situent sur la frontière urgent / non urgent.
- **E3.** Ton prompt dit « ne rembourse jamais plus de 1 000 € sans validation ». Pourquoi est-ce insuffisant en production, et que faut-il ajouter ?

## 7. Correction
<details><summary>Voir la correction</summary>

- **E1.** Exemple : « Un message est **urgent** s'il mentionne : une opération non reconnue sur le compte, une carte perdue ou volée, un prélèvement en cours à bloquer, ou une échéance dans les 24 h. Sinon il est **normal**. Si le message en contient plusieurs, il suffit qu'un critère soit présent. »
- **E2.** « *Ma carte a été avalée par le distributeur, je pars demain à l'étranger* » → urgent (risque + échéance). « *Je voudrais augmenter mon plafond pour un achat le mois prochain* » → normal (pas de risque, pas d'échéance proche).
- **E3.** Un prompt **guide**, il ne **garantit** pas : le modèle peut s'en écarter (prompt long, cas inattendu, injection). Il faut un **contrôle programmatique** dans l'outil ou un hook (si montant > 1 000 € : refus + validation humaine).

</details>

## 8. À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Critères **vérifiables**, raison donnée, données **balisées**.
- Few-shot : exemples **difficiles et variés**, dont un cas « absent ».
- Règle critique → **code**, pas seulement prompt.

</details>
