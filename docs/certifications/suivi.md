# Tableau de couverture — 4 certifications Claude

**Date de construction initiale : 13/11/2026.** La présence d'un fichier ou un test offline vert n'est **pas** une certification. Les examens appartiennent à Anthropic et peuvent évoluer ; actualiser à chaque publication du guide officiel.

## Portfolio

| Certification | Code | Domaines documentés | Questions originales | Pratique | Évaluation réelle |
|---|---|---|---:|---|---|
| Associate Foundations | CCAO-F | 7/7 | 14 | cas ConseilNova + grille, sans code | non passée |
| Developer Foundations | CCDV-F | 8/8 | 16 | faux client Messages + ACL + prix, pytest offline | non passée |
| Architect Foundations | CCAR-F | 5 domaines / M0–M9 | quiz et scénarios historiques | labos M1–M7, CI offline | non passée |
| Architect Professional | CCAR-P | 7/7 | 21 | cas AssurNova, dossier d'architecture | non passée |

**Important :** ces nombres décrivent la **présence des contenus** et non une certification complète de chaque objectif. En particulier, Developer possède 25 compétences officielles à vérifier individuellement, et Associate 7 domaines mais des sous-compétences qui demandent une comparaison avec la dernière édition du guide.

## Avancement technique par type de preuve

| Preuve | CCAO-F | CCDV-F | CCAR-F | CCAR-P |
|---|---|---|---|---|
| Cours/domaines rédigés | oui | oui | oui | oui |
| Cas de décision rédigé | ConseilNova | DevBank | cas du dépôt | AssurNova |
| Questions originales corrigées | 14 | 16 | quiz/scénarios | 21 |
| Logiciel hors API exécutable | non requis | **oui, à vérifier CI** | **oui, CI existante** | surtout conceptuel |
| Appels réels à Claude | non vérifiés | non vérifiés | non vérifiés | non vérifiés |
| Benchmarks coût/latence/qualité | non mesurés | non mesurés | non mesurés | non mesurés |
| Examens blancs complets au format officiel | **à créer : 60** | **à créer : 53** | **à créer : 60** | **à créer : 63** |
| Accès officiel à l'inscription | **à vérifier** | **à vérifier** | **à vérifier** | **à vérifier** |

## Règle de travail

1. Recharger le guide de l'[Anthropic Academy](https://anthropic-partners.skilljar.com/page/partner-certifications), contrôler version, domaines, compétences et tarif.
2. Ajouter une ligne de couverture **objectif → leçon → exercice → preuve → état** par objectif officiel.
3. Ne déclarer un test « réussi » qu'avec le lien du run CI ou la preuve d'une session d'intégration.
4. À la prochaine itération, prioriser les examens blancs **originaux** complets, l'automatisation des scores et l'évaluation API réelle, plutôt que dupliquer des fiches.
5. Corriger les éventuelles incompatibilités de version d'API avant d'exposer un lab à de vraies données ou à un vrai client.

## Accès aux examens

Selon [FAQ Anthropic](https://anthropic-partners.skilljar.com/page/faq-certifications), le **Claude Partner Network** est actuellement requis pour l'inscription ; le cours et le code sont indépendants de ce droit. **Associate** ne compte pas dans la progression de niveau partenaire, contrairement aux trois autres.
