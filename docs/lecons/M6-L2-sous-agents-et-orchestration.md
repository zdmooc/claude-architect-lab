# M6 · Leçon 2 — Coordinateur, sous-agents et décomposition (D1)

> **Statut** : `labs/labo4_multiagent/` vérifié contre `claude-agent-sdk` 0.2.181 (`AgentDefinition`, `agents=`), **non exécuté**.
> Nom de l'outil de délégation : le guide (juillet 2026, d'après ton dossier) parle de `Task` ; le SDK 0.2.181 mentionne « the Agent tool ». **Retiens le concept** ; vérifie le nom dans ta version.

## 1. Objectif et utilité
Concevoir un système multi-agent qui **décompose** bien, **transmet** le contexte et **agrège** les résultats. Compétences D1 : coordinateur et sous-agents spécialisés, contexte explicite, parallélisme, pipeline séquentiel vs décomposition adaptative.

## 2. Prérequis
M6·L1.

## 3. Cours
### a) Pourquoi des sous-agents ?
- **Spécialisation** : prompt et outils ciblés.
- **Isolation du contexte** : chaque sous-agent lit beaucoup, ne renvoie qu'une synthèse → le coordinateur garde un contexte propre.
- **Parallélisme** : les travaux indépendants avancent en même temps.

### b) Le piège n°1 : l'héritage du contexte
Un sous-agent **ne voit pas** la conversation du coordinateur. Tout ce dont il a besoin doit être **dans sa mission** : faits, contraintes, format de sortie.
👉 Comme un appel de service distant : tu passes les paramètres, tu ne partages pas la mémoire.

### c) Le piège n°2 : la décomposition
Des sous-agents excellents ne compensent pas une **mauvaise découpe** du coordinateur (dossier §3.2) :
- périmètres **complémentaires**, pas redondants ;
- **rien d'oublié** du besoin initial ;
- un format de retour **commun** pour pouvoir agréger.

### d) Séquentiel ou adaptatif ?
| Structure | Quand |
|---|---|
| **Pipeline séquentiel** (étapes fixes) | le processus est connu et stable (extraction → validation → rapport) |
| **Décomposition adaptative** (le coordinateur décide) | la tâche est ouverte, on ne sait pas d'avance quoi explorer |
Commencer par le plus simple : un pipeline codé est plus prévisible qu'un agent.

### e) Reprise et contexte périmé
Sessions reprises ou embranchées (`resume`, `fork_session` dans le SDK) : les **faits** peuvent avoir changé depuis. Revalider ce qui est critique au lieu de supposer.

## 4. Exemple commenté : `recherche_multiagent.py`
- Deux `AgentDefinition` aux périmètres **disjoints** (replatform / refactor).
- Le coordinateur **recopie les faits** (120 000 lignes, WebSphere 8.5, DB2, MQ, équipe de 6) dans la consigne de délégation.
- `FORMAT_PREUVE` commun → agrégation et provenance (M7).

## 5. Exercice guidé
Mission confiée à un sous-agent : « Analyse l'option dont on a parlé. » → Il ne sait pas de quoi on a parlé.
Réécriture : « Analyse l'option *replatform WebSphere 8.5 → Liberty sur OpenShift* pour l'application GestSin (120 000 lignes Java EE, DB2, 3 interfaces MQ). Rends `{affirmation, extrait, source, date_source}` et `lacunes`. »

## 6. Exercice à toi
- **E1.** Propose une décomposition en 3 sous-agents pour « préparer le dossier de migration de GestSin vers OpenShift ». Vérifie qu'ils sont complémentaires et que rien ne manque.
- **E2.** Séquentiel ou adaptatif : (a) traitement mensuel des factures ; (b) enquête sur un incident de production inconnu.
- **E3.** Le rapport final ignore totalement le volet sécurité alors que les sous-agents sont bons. Où est probablement le problème ?

## 7. Correction
<details><summary>Voir la correction</summary>

- **E1.** Exemple : (1) **inventaire technique** (WebSphere, JVM, dépendances, configuration) ; (2) **plateforme cible** (images, ressources, réseau, stockage, observabilité sur OpenShift) ; (3) **risques et conformité** (sécurité, données, exploitation, plan de retour arrière). Vérifier la couverture : coût/planning et tests peuvent manquer → les ajouter au coordinateur ou à un 4ᵉ sous-agent.
- **E2.** (a) **Séquentiel** : étapes connues et stables. (b) **Adaptatif** : on ne sait pas d'avance quoi explorer.
- **E3.** Chez le **coordinateur** : la décomposition n'a pas prévu le volet sécurité, ou la synthèse l'a perdu. Les sous-agents ne font que ce qu'on leur confie.

</details>
## 8. À retenir pour l'examen
<details><summary>Voir le résumé</summary>

- Le sous-agent ne reçoit **que** ce qu'on lui transmet : contexte explicite.
- Périmètres **complémentaires**, format de retour **commun**.
- Pipeline séquentiel si stable ; décomposition adaptative si inconnu.
- Outil de délégation : « Task » dans le guide, « Agent » dans le SDK actuel.

</details>
