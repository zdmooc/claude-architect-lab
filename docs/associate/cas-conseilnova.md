# Cas fil rouge Associate — ConseilNova

**Entreprise entièrement fictive.** ConseilNova est un cabinet qui prépare des notes d'aide à la décision pour des clients ; aucun document ni chiffre réel.

## Demande du sponsor

« Prépare une recommandation de recours à Claude pour notre équipe SAV, 100 demandes par semaine, avec un retour sur investissement clair, sans diffuser d'informations client. »

**Contraintes de simulation** : 3 utilisateurs, 2 superviseurs, procédures internes versionnées, aucun accès à un SI sensible autorisé, aucune pièce client réelle dans le POC. Le sponsor affirme un objectif de gain de 30 % de temps, **non mesuré**. L'équipe veut mettre en place un Project partagé et une validation humaine de chaque réponse externe.

## Documents synthétiques à utiliser

**SRC-A — Processus actuel, version 1 datée du 01/11/2026** : les demandes SAV sont reçues par formulaire ; un employé vérifie contrat, date et motif ; un superviseur approuve les réponses atypiques ; durée de traitement non mesurée.

**SRC-B — Politique de confidentialité, version 2 datée du 05/11/2026** : les données identifiantes ne peuvent pas être copiées dans des outils non autorisés ; les tests se font sur données synthétiques ; la conformité doit être validée par le DPO.

**SRC-C — Procédure SAV, version 3 datée du 07/11/2026** : réponse standard possible uniquement après vérification du contrat et de la règle applicable ; toute exception ou réclamation → superviseur.

**SRC-D — Note du sponsor, sans méthodologie** : « Claude permettra 30 % d'économie dès le premier mois ».

## Mission à réaliser en sept étapes

1. **A5** : sélectionner surface de travail, capacité requise et alternatives non-IA. Justifier pourquoi le Project est envisagé, mais pas autorisé sans validation.
2. **A4** : écrire un prompt de réponse SAV qui cite SRC-C, refuse les faits absents et garde une sortie en colonnes.
3. **A1** : évaluer une proposition contenant « gain mesuré de 30 % » et « réclamation résolue ». Ces deux affirmations n'ont **aucune preuve** : les signaler.
4. **A6** : établir un inventaire des documents, propriétaires, droits et versions. SRC-D ne peut pas devenir une référence chiffrée sans baseline.
5. **A2** : dessiner déclencheur → vérification déterministe de contrat → Claude comme aide rédactionnelle → relecture humaine → réponse.
6. **A3** : lister trois risques et les contrôles à faire approuver, avec preuve.
7. **A7** : simuler une réponse erronée à cause d'une ancienne procédure ; isoler la cause, corriger le document et revalider.

## Livrable attendu : note de décision (1 page)

- **Décision proposée** : pilote sur demandes entièrement synthétiques, sans réponse client automatique.
- **Bénéfice à mesurer** : temps de traitement moyen et taux de retouche, en comparant même type de dossier.
- **Risques et contrôles** : droits/confidentialité, vérification des références et revue humaine.
- **Conditions de GO** : validation DPO et métier, protocole de mesure, base documentaire actualisée, procédure de repli.
- **Critère de NO-GO** : une réponse contenant un fait financier non sourcé, ou des données clients hors outil autorisé.

## Correction type

Le 30 % est un **objectif**, pas un résultat. SRC-A ne fournit pas de baseline ; le ROI ne peut pas être chiffré honnêtement. Le système doit proposer un brouillon basé sur SRC-C, **sans action externe directe**, revu par un gestionnaire. Le Project ne doit contenir que les documents dont les droits ont été approuvés. L'architecture la plus simple répond au périmètre initial ; aucun agent autonome n'est requis.

**Auto-évaluation** : 1 point par preuve (7 étapes) + 3 points pour une note différenciant hypothèses, résultats mesurés et conditions de mise en œuvre. **Ce barème est pédagogique, non officiel.**
