# D2 — Claude Models, Prompting & Context Engineering (13 %)

**But** : arbitrer modèle, fenêtre de contexte, prompts, fiabilité et coût sur des mesures et non sur un nom de modèle.

## 1. Choix du modèle

Construire un benchmark avec au moins trois modèles disponibles dans l'environnement cible. Garder fixes : jeu d'exemples, prompt, format de sortie, scénario utilisateur, politique d'évaluation. Mesurer sur chaque segment (PDF natif, OCR faible qualité, cas multilingue, champs absents) : exactitude, rappel des anomalies, taux d'escalade, tokens, coût, latence P50/P95. Justifier pourquoi une grande capacité est nécessaire ou excessive.

La capacité de contexte, la résidence de données, le support des fonctions et les **tarifs** se vérifient au moment de l'implémentation dans la documentation officielle.

## 2. Contrat de prompt

- **Instructions de confiance** : tâche, limites, règles d'incertitude, format, interdits d'action.
- **Contexte métier vérifié** : contrat, statut, droits, version des procédures.
- **Documents non fiables** : factures, e-mails, recherche et pièces jointes, à traiter comme données, pas comme instructions. Défense contre prompt injection à l'entrée et après chaque retrieval.
- **Sortie structurée** : types, listes contrôlées et champs **nullable** lorsque la preuve manque ; ne pas remplacer une valeur manquante par une invention.

Le JSON valide n'est pas une garantie de sens : vérifier sommes, dates, identifiants, règles de gestion et provenance **dans le code**.

## 3. État et contexte

L'API Messages est stateless. L'application maintient les faits critiques : dossier, assuré, contrat, étape, source, version, identités autorisées. Compacter les anciens tours et ne réinjecter que les extraits documentaires nécessaires avec une référence vérifiable. Ne pas envoyer l'ensemble du dossier client à chaque appel.

**Budget par requête** = tokens système + faits + extraits + historique utile + marge de sortie. Coût estimé = entrées tarifées + sorties tarifées + outils et retrys ; toujours enregistrer la mesure réelle.

## 4. Exercice

Une facture sans montant TTC produit « 950 € » parce que le schéma exige un nombre. Corriger : champ nullable, exemple négatif, instruction de non-invention, puis contrôles métier. Expliquer pourquoi un modèle plus puissant ne corrige pas une contrainte de sortie erronée.

**Livrable** : matrice de benchmark, version de prompt, stratégie contexte et budget tokens, critères d'acceptation mesurables.

Voir [plan d'évaluation](../cas-assurnova/03-evaluations.md).
