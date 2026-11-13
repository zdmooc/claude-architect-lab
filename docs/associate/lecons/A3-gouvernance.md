# A3 — Governance, Risk, and Responsible Use (15 %)

**Compétence** : reconnaître quand Claude est inapproprié, protéger les données et organiser une validation humaine proportionnée au risque.

## Cours

Avant d'envoyer un document : **ai-je le droit de l'utiliser ?** Vérifier classification interne, données personnelles, contrats de sous-traitance, conservation, politique d'entreprise et contrôle d'accès. Ne pas supposer qu'un abonnement grand public permet l'envoi d'un dossier confidentiel.

Risques à examiner : réponses inventées, **prompt injection** via documents externes, biais, erreurs sur montants, données datées, confidentialité, dépendance à une réponse automatisée, surconfiance. Une personne vérifie les décisions à impact élevé, avec possibilité effective de refuser ou corriger. **Le modèle ne doit jamais être la source de l'autorisation**.

| Risque | Contrôle | Preuve |
|---|---|---|
| Fuite de données | classification et accès restreints | revue des droits |
| Chiffres faux | vérification contre système de référence | grille signée |
| Procédure obsolète | propriétaire, date/version de mise à jour | journal de révision |
| Message malveillant dans un document | document traité comme données non fiables | cas de test d'injection |
| Décision critique automatisée | approbation par responsable habilité | décision et historique |

## Exercice

Un manager souhaite charger dans un Project partagé des CV avec données personnelles. **Corrigé** : suspendre le chargement, vérifier base légale, droits, outil autorisé et minimisation ; utiliser des profils synthétiques pour la démonstration.

## Piège

« Claude chiffre les données » ne répond pas seul aux questions : **qui peut les lire ? où sont-elles traitées ? combien de temps sont-elles conservées ? qui a approuvé ?**

**À produire** : registre simple **risque, gravité, responsable, contrôle, preuve**.
