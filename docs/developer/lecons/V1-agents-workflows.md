# V1 — Agents and Workflows (14,7 %)

> **Source des objectifs** : guide officiel CCDV-F v1.0 (juillet 2026), §6, Domain 1. Cours, exemples et questions **originaux**. Fil rouge : [cas DevBank](../cas-devbank.md) (données fictives).

## 1. Objectif
Compétences officielles du domaine :
- **Agent Architecture (4,5 %)** : critères workflow vs agent, hiérarchies manager/superviseur, rôle des sous-agents ;
- **Agent Construction with Claude (5,3 %)** : Claude Agent SDK, boucles et harnais maison, agents auto-hébergés vs agents gérés par Anthropic, **hooks** pour les actions déterministes ;
- **Agent Patterns and Frameworks (4,9 %)** : boucles d'outils, sous-agents, mémoire, gestion de la fenêtre de contexte ; frameworks tiers (ex. Strands, LangGraph, PydanticAI).

## 2. Prérequis
Architect Foundations M3 (boucle tool use) et M6 (Agent SDK, hooks, sous-agents). Python de base.

## 3. Cours

### a) Faut-il un agent ?
| Motif | Qui contrôle le flux | Quand |
|---|---|---|
| Appel unique | ton code, un appel | classer, extraire, résumer |
| Workflow | ton code enchaîne les étapes | processus connu, règles stables, approbations |
| Agent avec outils | le **modèle** choisit outils et ordre | chemin ouvert : enquête, recherche, diagnostic |
| Manager + sous-agents | un coordinateur délègue | sous-tâches indépendantes, contextes lourds |
Critère : **le plus simple qui suffit**. L'autonomie coûte en tokens, en latence et en contrôle ; on la justifie par un gain mesuré.

### b) La boucle d'outils (à savoir écrire)
1. Envoyer `messages` + `tools`.
2. Si `stop_reason == "tool_use"` : exécuter **chaque** bloc `tool_use` (seulement des outils autorisés), renvoyer la réponse assistant complète puis un message `user` contenant **tous** les `tool_result` avec le bon `tool_use_id` (et `is_error` si échec).
3. Recommencer jusqu'à `end_turn`. Un **budget d'itérations** (`max_turns`) est un garde-fou : l'atteindre est une anomalie (journaliser, escalader).

### c) Construire avec Claude
- **Boucle manuelle** (SDK client) : contrôle total, peu d'outils, logique simple.
- **Tool Runner** (SDK client, bêta) : boucle fournie pour tes fonctions.
- **Claude Agent SDK** : le harnais de Claude Code dans ton programme (outils fichiers/bash, sous-agents, **hooks**, permissions, sessions).
- **Auto-hébergé vs géré** : tu héberges le runtime (contrôle, conformité, exploitation à ta charge) ou tu utilises une offre d'agents gérée par Anthropic (moins d'exploitation, contraintes de la plateforme). Choisir selon données, réseau, conformité et équipe d'exploitation. Vérifier la disponibilité exacte dans la documentation.
- **Hooks** : code exécuté à des moments du cycle (`PreToolUse`, `PostToolUse`…) pour **refuser**, modifier ou journaliser de façon déterministe.

### d) Motifs et frameworks
- **Sous-agents** : contexte isolé ; on leur passe **explicitement** tâche, contexte, format de retour, gestion d'échec.
- **Mémoire** : faits fiables stockés par l'application (avec provenance), pas « dans la tête » du modèle.
- **Contexte** : élaguer les sorties d'outils, compacter les longs historiques, isoler par sous-agents.
- **Frameworks tiers** (Strands, LangGraph, PydanticAI…) : utiles pour graphes d'états, typage, intégrations ; ils ajoutent dépendances et abstraction. Choisir sur preuve (besoin, gouvernance, opérabilité), pas par mode.

## 4. Exemple — DevBank
Résumé de garantie : **workflow** (authentification → `consulter_contrat` → extraction → résumé sourcé). Un agent n'est utilisé que pour « retrouver une pièce manquante » (chemin ouvert), avec outils en lecture seule et `max_turns=6`. Hook `PreToolUse` : refus de tout outil hors liste.

## 5. Exercice guidé
Un agent appelle deux outils dans la même réponse. Le code renvoie deux messages `user` successifs, un par résultat → erreur API ou comportement incohérent.
Correction : **un seul** message `user` avec les deux `tool_result`, chacun avec son `tool_use_id`.

## 6. Exercice à toi
- **E1.** Workflow ou agent : (a) envoyer un relevé mensuel ; (b) trouver pourquoi un virement est bloqué entre 4 systèmes.
- **E2.** Écris en pseudo-code la boucle d'outils avec budget de 8 tours et gestion d'erreur d'outil.
- **E3.** Ton équipe veut adopter un framework multi-agents « parce que c'est la tendance » pour un FAQ bot à 2 outils. Que réponds-tu ?

## 7. Correction
<details><summary>Voir la correction</summary>

- **E1.** (a) **Workflow** (étapes fixes, aucun choix ouvert). (b) **Agent** en lecture seule (chemin imprévisible), avec traces et budget.
- **E2.**
```python
for tour in range(8):
    r = client.messages.create(model=M, max_tokens=1024, tools=TOOLS, messages=msgs)
    msgs.append({"role": "assistant", "content": r.content})
    if r.stop_reason == "end_turn":
        return r
    if r.stop_reason != "tool_use":
        raise Anomalie(r.stop_reason)          # max_tokens, refusal…
    resultats = []
    for b in r.content:
        if b.type == "tool_use":
            try:
                resultats.append({"type": "tool_result", "tool_use_id": b.id, "content": executer(b.name, b.input)})
            except ErreurOutil as e:
                resultats.append({"type": "tool_result", "tool_use_id": b.id, "content": str(e), "is_error": True})
    msgs.append({"role": "user", "content": resultats})
raise BudgetDepasse()                          # journaliser + escalader
```
- **E3.** Une boucle simple (ou le Tool Runner) suffit : 2 outils, chemin court. Un framework ajoute dépendances et complexité sans gain mesurable. On y reviendra si le besoin (graphe d'états, nombreux agents) apparaît.
</details>

## 8. Questions d'entraînement (originales)
**Q1.** Une réponse contient un bloc `text` et un bloc `tool_use`, `stop_reason="tool_use"`. Que fait le code ?
A. Affiche le texte et s'arrête · B. Exécute l'outil, renvoie le `tool_result`, relance · C. Ignore l'outil · D. Relance sans rien ajouter

**Q2.** Quel mécanisme garantit qu'un outil de suppression n'est jamais exécuté sans validation ?
A. Une consigne dans le prompt · B. Un hook `PreToolUse` qui refuse (et un contrôle côté service) · C. Un modèle plus grand · D. Un exemple few-shot

**Q3.** (2 réponses) Ce qu'un sous-agent doit recevoir explicitement :
A. La tâche et le contexte utile · B. Rien, il hérite de tout · C. Le format de retour attendu · D. La clé API en clair dans le prompt

<details><summary>Voir les réponses</summary>

| Q | Réponse | Justification |
|---|---|---|
| Q1 | **B** | On suit `stop_reason`. |
| Q2 | **B** | Déterministe, pas probabiliste. |
| Q3 | **A, C** | Pas d'héritage implicite ; jamais de secret dans un prompt. |
</details>

## 9. À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Workflow si le chemin est connu ; agent si ouvert ; sous-agents si indépendants.
- Boucle : `tool_use` → tous les `tool_result` dans un message → jusqu'à `end_turn` ; budget = garde-fou.
- Agent SDK = harnais Claude Code ; hooks = contrôles déterministes.
- Mémoire et faits dans l'application ; contexte élagué, compacté, isolé.
- Frameworks tiers : sur preuve de besoin.
</details>

**Pratique** : [labo 1 Agent SDK](../../../labs/labo1_support/README.md), [labo M3](../../../labs/m3/README.md).
