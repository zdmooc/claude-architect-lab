# M1 · Leçon 1 — Premier appel à l'API Messages

> **Statut du code** : proposé, vérifié contre la documentation du SDK Python et la version installée `anthropic 2.8.0` (contrôle des champs `stop_reason` et `usage`, compilation OK).
> **Non exécuté** contre l'API par le formateur : pas de clé. Le résultat observé sera le tien.

## 1. Objectif et utilité
Faire ton premier appel Python à Claude, et **savoir lire la réponse** : blocs de contenu, `stop_reason`, `usage`.
C'est le geste de base de tous les labos et le prérequis de D1 (boucle agentique) et D4 (sorties structurées).

## 2. Prérequis
- Leçons M0·L1 et M0·L2.
- Python 3.10+ installé sur ton poste (`python3 --version`).
- Git et un clone de `claude-architect-lab`.

## 3. Cours

### a) Anatomie d'une requête
| Champ | Rôle |
|---|---|
| `model` | identifiant exact du modèle (ex. `claude-opus-5-5`) |
| `max_tokens` | plafond de la **réponse** (pas de la requête) |
| `system` | consignes stables (rôle, ton, règles) |
| `messages` | l'historique : alternance `user` / `assistant` |

### b) Anatomie d'une réponse
- `content` : une **liste de blocs**. Les plus courants : `text`, `thinking` (raisonnement du modèle, souvent vide à l'affichage), `tool_use` (demande d'appel d'outil — M3).
  → On ne lit jamais « la réponse » d'un bloc ; on **filtre** par `type`.
- `stop_reason` : **pourquoi** le modèle s'est arrêté. Valeurs observées dans le SDK :
  - `end_turn` : il a fini normalement ;
  - `max_tokens` : coupé par ton plafond → réponse tronquée ;
  - `tool_use` : il attend que tu exécutes un outil (cœur de D1) ;
  - `refusal` : il a refusé la demande ;
  - `stop_sequence`, `pause_turn`, `model_context_window_exceeded` : cas plus rares, on les verra en temps utile.
- `usage` : `input_tokens` et `output_tokens` → c'est ta **facture**.

### c) La clé API : un secret, traité comme tel
- Créée dans la **Claude Console** (plateforme développeur d'Anthropic).
- **Jamais dans le code ni dans Git** : variable d'environnement `ANTHROPIC_API_KEY`. Le SDK la lit tout seul.
- Ton `.gitignore` exclut déjà `.env`.
👉 Même discipline qu'un mot de passe de datasource WebSphere : dans un secret, jamais dans l'EAR.

### d) Coûts
Facturation au token, **différente selon le modèle**. Ordres de grandeur relevés le 03/11/2026 (à revérifier sur la page tarifs) :
| Modèle | Entrée / 1 M tokens | Sortie / 1 M tokens |
|---|---:|---:|
| `claude-opus-5-5` (défaut recommandé) | 4 $ | 20 $ |
| `claude-haiku-5-5` (le moins cher) | 0,10 $ | 0,50 $ |

Un exercice de cette leçon consomme quelques centaines de tokens : **une fraction de centime**. Mais il faut des crédits sur le compte.

## 4. ⚠️ Mise en place pas à pas — **dépense possible, lis avant d'agir**
1. Crée un compte sur la Claude Console (lien depuis claude.com, rubrique développeurs).
2. Regarde dans *Billing* si un crédit d'essai est offert. **S'il faut acheter des crédits, arrête-toi et préviens-moi** : on choisit ensemble le montant minimum. Active une **limite de dépense** mensuelle basse.
3. Crée une clé API (*API Keys* → *Create Key*), nomme-la `claude-architect-lab`. Copie-la une seule fois.
4. Dans ton terminal :
   ```bash
   cd claude-architect-lab
   python3 -m venv .venv && source .venv/bin/activate      # Windows : .venv\Scripts\activate
   pip install -r labs/m1/requirements.txt
   export ANTHROPIC_API_KEY="colle-ta-cle-ici"            # Windows PowerShell : $env:ANTHROPIC_API_KEY="..."
   python labs/m1/premier_appel.py
   ```

## 5. Exemple commenté : `labs/m1/premier_appel.py`
- `anthropic.Anthropic()` : aucun secret dans le code, la clé vient de l'environnement.
- `system=` fixe le rôle « assistant sinistres ».
- La boucle `for block in response.content` n'affiche que les blocs `text` : avec les modèles récents, un bloc `thinking` peut précéder le texte.
- Les trois dernières lignes affichent `stop_reason` et la consommation : **prends l'habitude de toujours les regarder**.

## 6. Exercice guidé (sans clé, sur papier)
Une réponse revient avec `stop_reason = "max_tokens"` et un texte qui s'arrête au milieu d'une phrase.
1. Que s'est-il passé ? La réponse a atteint le plafond `max_tokens`.
2. Est-ce une erreur du modèle ? Non : c'est **ta** limite.
3. Que faire ? Augmenter `max_tokens`, ou demander une réponse plus courte dans le prompt.
4. Que **ne pas** faire ? Utiliser ce texte tronqué comme s'il était complet (ex. un JSON coupé → invalide).
Réflexe examen : **toujours tester `stop_reason` avant d'exploiter le contenu**.

## 7. Exercice à toi
Si tu as fait la mise en place :
- **E1.** Lance `premier_appel.py`. Note le texte, `stop_reason`, `input_tokens`, `output_tokens`.
- **E2.** Mets `max_tokens=20` et relance. Qu'observes-tu ? Quel `stop_reason` ?

Sans mise en place (ou en plus) :
- **E3.** Pourquoi le script filtre-t-il `block.type == "text"` au lieu d'afficher `response.content[0].text` directement ?
- **E4.** Un collègue écrit la clé en dur dans le script « juste pour tester » et commit. Cite deux risques et la correction.

## 8. Correction
<details><summary>Voir la correction</summary>

- **E1.** Résultat attendu : un texte court, `stop_reason = end_turn`, quelques dizaines à centaines de tokens. Tes chiffres exacts sont ton **résultat observé**.
- **E2.** Réponse coupée net, `stop_reason = max_tokens`. Ce n'est pas une erreur du modèle : c'est ton plafond.
- **E3.** `content` est une **liste de blocs** ; le premier peut être un bloc `thinking` (sans `.text`) → `content[0].text` peut échouer ou afficher autre chose. On filtre par `type`.
- **E4.** Risques : clé exposée dans l'historique Git (même après suppression), utilisation frauduleuse facturée sur ton compte. Correction : **révoquer** la clé, en créer une nouvelle, la passer par variable d'environnement, scanner les secrets.

</details>

## 9. À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Requête : `model`, `max_tokens` (borne la réponse), `system`, `messages`.
- Réponse : liste de blocs, **`stop_reason`** (tester avant d'exploiter), `usage` (facture).
- Clé API = secret : variable d'environnement, jamais dans Git.

</details>
