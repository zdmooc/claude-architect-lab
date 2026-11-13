# V5 — Model Selection and Optimization (16,8 %)

Quatre compétences du blueprint : **LLM Fundamentals (5,2 %)**, **Technical Fundamentals (6,1 %)**, **Model Selection and Tradeoffs (2,7 %)**, **Cost and Token Management (2,8 %)**.

## 1. Fondamentaux opérationnels

Un token est une unité de traitement (ni un caractère ni un mot constant). La fenêtre de contexte **limite** l'entrée, l'historique, les descriptions d'outils et la sortie éventuelle ; l'application doit prévoir le budget au lieu de faire croître l'historique sans limite. La génération est **non déterministe** : tester sur plusieurs exemples et exécutions, en particulier les cas critiques.

Connaître les familles de modèles par capacité, vitesse, coût et fonctions supportées. La liste exacte, les context windows, les tarifs, le caching, la disponibilité Bedrock/Vertex/Claude API et les limites de taux **changent** ; les vérifier sur le fournisseur utilisé avant un benchmark.

## 2. Choisir la variante d'architecture

| Besoin | Option candidate | Critère de rejet |
|---|---|---|
| Classement simple de 10 000 messages | modèle économique + batch | taux d'erreur par catégorie non acceptable |
| Analyse complexe de dossier | modèle capable + retrieval ciblé | latence ou coût excèdent budget |
| Chat interactif | streaming + contexte ciblé | erreurs d'accès ou hallucinations |
| Préfixe identique sur nombreuses requêtes | prompt caching si supporté | hit rate trop bas ou coût réel défavorable |

### Coût complet

Coût estimé = tokens entrée × tarif entrée + tokens sortie × tarif sortie + cache/batch facturés selon conditions + outils + stockage + infrastructure + revue humaine. Une baisse des tokens d'entrée n'est pas nécessairement un gain si la réponse génère plus de corrections humaines.

`max_tokens` limite **la longueur de sortie**, pas une durée en secondes et pas le nombre de tokens d'entrée. Un `stop_reason=max_tokens` indique une réponse tronquée.

## Exercice et correction

Modèle A : 0,02 € par document et 80 % de réussite, coût de revue 0,50 € si échec. Modèle B : 0,06 € et 98 % de réussite, revue même coût. Calcul : A = 0,02 + 0,20×0,50 = **0,12 €** ; B = 0,06 + 0,02×0,50 = **0,07 €**. **B est moins cher au total** dans ces hypothèses ; vérifier la distribution des erreurs et la latence avant décision réelle.

**Preuve** : [lab pricing hors API](../../../labs/developer_foundations/README.md).
