# M0 · Leçon 1 — Comment fonctionne un LLM (et ce que ça change pour un architecte)

## 1. Objectif
Savoir expliquer **token**, **fenêtre de contexte**, **API sans état (stateless)** et **hallucination**.
Ces notions sous-tendent D1 (renvoyer les résultats d'outils dans l'historique) et D5 (préserver les faits critiques).

## 2. Prérequis
Notion d'API HTTP/JSON.

## 3. Cours

### a) Ce que fait un LLM
Il **prédit la suite la plus plausible** d'un texte, token par token, à partir de son entraînement et de ce qu'on lui envoie.
Conséquences : date de coupure des connaissances ; réponses fluides mais parfois fausses (hallucinations) ; génération non strictement déterministe.

### b) Tokens
Unité de lecture du modèle (fragments de mots ; ≈ ¾ de mot en anglais, un peu plus de tokens en français).
Unité de **facturation** (input + output), de **taille maximale de la requête**, et de **longueur de réponse** (`max_tokens`).
L'algorithme de tokenisation est **hors programme** Foundations (dossier §3.8).

### c) Fenêtre de contexte
Tout ce que le modèle voit lors d'un appel : system prompt, historique, documents, résultats d'outils, réponse en cours.
Grande mais **finie** (taille selon le modèle — à vérifier dans la documentation). Coûte cher ; une information noyée dans un long contexte peut être moins bien prise en compte.

### d) Stateless
L'API Messages **ne garde aucune mémoire** entre deux appels : l'application **renvoie tout l'historique** à chaque requête.
Analogie : un service REST sans `HttpSession` ni session affinity — l'état vit côté client.
- Ce qui n'est pas renvoyé n'existe plus pour le modèle.
- L'historique grossit → coût et latence augmentent.
- L'architecte décide quoi garder, résumer, jeter.

claude.ai et Claude Code donnent l'illusion d'une session parce que **l'application** gère l'historique.

## 4. Exemple commenté
*Code proposé, non exécuté — syntaxe à vérifier en M1.*

```json
{
  "model": "<id du modèle>",
  "max_tokens": 500,
  "system": "Tu es un assistant de gestion de sinistres. Réponds en français.",
  "messages": [
    {"role": "user", "content": "Mon contrat est le AUTO-4471. J'ai eu un bris de glace."},
    {"role": "assistant", "content": "Bien noté, contrat AUTO-4471, bris de glace. Quelle est la date ?"},
    {"role": "user", "content": "Le 3 novembre."}
  ]
}
```
- Les deux premiers messages sont renvoyés par l'application.
- `system` porte les consignes stables.
- `max_tokens` limite la **réponse**, pas la requête.

## 5. Exercice guidé
« Au 40ᵉ échange, l'assistant a oublié le numéro de contrat. »
1. Le numéro était dans le 1er message.
2. L'application gère l'historique (stateless).
3. Hypothèses : troncature des vieux messages, ou information noyée dans un long contexte.
4. Remède : un **bloc de faits structurés** (contrat, date, montant) renvoyé à chaque tour (compétence D5).

Réflexe : vérifier **ce que l'application envoie réellement** avant d'accuser le modèle.

## 6. Exercice autonome
- **Q1.** « Claude garde la session côté serveur comme un EJB stateful. » Qu'est-ce qui est faux, et quelle conséquence sur l'application ?
- **Q2.** Un PDF de 200 pages collé dans chaque requête d'une conversation de 30 tours : deux problèmes et une piste.
- **Q3.** Un assistant invente un article de loi : nom du phénomène, cause, contrôle à prévoir en contexte bancaire.

## 7. Correction
*Ajoutée après la réponse de l'apprenant.*

## 8. À retenir pour l'examen
*Ajouté avec la correction.*
