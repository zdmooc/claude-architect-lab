# M4 · Leçon 1 — MCP : le protocole, ses rôles, ses primitives (D2)

## 1. Objectif et utilité
Comprendre **à quoi sert MCP**, qui parle à qui, et la différence entre **outil**, **ressource** et **prompt**.
D2 (18 %, selon le dossier) inclut « distinguer ressources MCP et outils d'action ».

## 2. Prérequis
M3 (tool use : Claude demande, le code exécute).

## 3. Cours
### a) Le problème résolu
Sans MCP, chaque application IA réimplémente ses connecteurs (GED, CRM, référentiel…). Avec MCP, on écrit **un serveur** par système, et **tout client compatible** (Claude Code, claude.ai, ton agent) peut l'utiliser.
👉 Analogie : JCA / JDBC — un contrat standard, des implémentations interchangeables.

### b) Les rôles
- **Hôte** : l'application où l'utilisateur travaille (Claude Code, claude.ai…).
- **Client MCP** : le composant de l'hôte qui parle à **un** serveur.
- **Serveur MCP** : ton programme qui expose des capacités.
- **Transport** : `stdio` (le serveur est un processus local lancé par l'hôte) ou HTTP (serveur distant).

### c) Les trois primitives
| Primitive | Qui décide de l'utiliser | Nature | Exemple |
|---|---|---|---|
| **Tool** (outil) | le **modèle** | une **action** ou requête paramétrée | `consulter_contrat(numero)` |
| **Resource** (ressource) | l'**application / l'utilisateur** | un **contenu** à lire, identifié par URI | `doc://procedures/franchise` |
| **Prompt** | l'**utilisateur** | un modèle de consigne réutilisable | « Résumer un dossier sinistre » |

Règle pratique : *ça agit ou ça dépend de paramètres variables* → outil ; *c'est un document de référence stable* → ressource.

### d) Ce qui ne change pas
Tout ce qu'on a vu en M3 reste vrai : descriptions distinctives, erreurs structurées, vide ≠ échec, moindre privilège. MCP **transporte** les outils ; il ne les rend pas bons par magie.

### e) Hors périmètre
Selon le dossier (§3.8), l'**orchestration de conteneurs pour héberger MCP** et les détails **OAuth** sont hors programme Foundations. Ton expérience OpenShift servira en Professional, pas ici.

## 4. Exemple commenté
Un assistant sinistres a besoin : de lire le contrat d'un client, de connaître la procédure franchise, et de lancer un résumé type.
- `consulter_contrat` → **tool** (paramètre variable, le modèle décide).
- Procédure franchise → **resource** (document stable, attaché par l'utilisateur ou l'application).
- « Résumé de dossier » → **prompt** (gabarit choisi par l'utilisateur).

## 5. Exercice guidé
« Faut-il exposer le **catalogue des garanties** (200 pages, change 2 fois par an) comme outil ou comme ressource ? »
→ Contenu stable, de référence → **ressource**. Si le besoin devient « trouve la garantie qui couvre X » → ajouter un **outil de recherche** dans ce catalogue. Les deux peuvent coexister.

## 6. Exercice à toi
Classe en tool / resource / prompt, avec une justification d'une ligne :
- **A.** Le schéma de la base « sinistres » (documentation des tables).
- **B.** Créer un ticket d'escalade.
- **C.** Un gabarit « courrier de refus de prise en charge ».
- **D.** Obtenir le solde d'un compte client à une date donnée.

## 7. Correction
*Après ta réponse.*
## 8. À retenir pour l'examen
*Avec la correction.*
