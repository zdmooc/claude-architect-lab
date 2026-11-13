# D5 — Governance, Safety & Risk Management (14 %)

**But** : placer les contrôles au bon endroit et relier chaque exigence de conformité à un propriétaire et une preuve.

## 1. Modèle de menace

Énumérer : prompt injection dans documents, exfiltration par outil, accès non autorisé, mauvaise attribution de contrat, hallucination de garanties, doubles paiements, biais de traitement, fuite dans les logs, dérive de coût, panne fournisseur, conservation excessive de données.

## 2. Défense en profondeur

- **À l'entrée** : identité, consentement/base légale, filtrage données, limitation de taille et de débit, politiques de confidentialité.
- **Avant les outils** : authentification, autorisation côté service métier, liste d'outils autorisés, schémas contrôlés, idempotence, anti-replay, séparation des rôles.
- **Après génération** : validation schéma, cohérence métier, vérification citations, garde-fou de montant, refus humain sur ambiguïté.
- **À l'action** : confirmation et autorisation indépendantes du modèle ; fail closed si identité, contrat ou règle indisponible.
- **En exploitation** : traces minimales, suivi incidents, gestion versions, revue des accès, suppression/retention, plan de repli.

Les **hooks/guardrails** côté agent renforcent l'application, mais n'exemptent jamais la vérification dans le service métier lui-même.

## 3. Exigences et preuves

Exemple : « aucun remboursement > 800 € sans gestionnaire » → contrôle déterministe de l'API de proposition, rôle APPROBATEUR, test au seuil 800,00/800,01 €, événements d'audit, propriétaire métier, revue sécurité. Le prompt n'est qu'une consigne de présentation.

Matrice obligatoire : exigence, risque, contrôle préventif/détectif, emplacement, owner, test, journal de preuve, fréquence de révision, mode d'échec.

## 4. Exercice

Le modèle reconnaît un contrat d'un autre assuré et propose sa garantie. Détailler le chemin d'attaque BOLA, le contrôle d'identité/ownership au serveur, le test de non-régression et l'événement d'audit minimal.

**Livrable** : threat model, matrice contrôles + RACI, plan d'incident et décision de risque résiduel.

Voir [contrôles/RACI](../cas-assurnova/04-controles-raci.md).
