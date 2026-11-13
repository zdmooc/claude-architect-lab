"""Labo 4 — Recherche multi-agent avec PROVENANCE (M6, D1/D5).

Vérifié contre `claude-agent-sdk` 0.2.181 (`AgentDefinition`, `ClaudeAgentOptions.agents`). Compilé, NON exécuté.
Les sous-agents sont lancés par le coordinateur via l'outil « Agent » (le guide de juillet 2026 parle de `Task` :
vérifie le nom dans ta version — dans le SDK 0.2.181, la doc interne mentionne « the Agent tool »).

Sujet fictif : moderniser une application Java/WebSphere « GestSin ».
"""
import asyncio

from claude_agent_sdk import AgentDefinition, ClaudeAgentOptions, query

FORMAT_PREUVE = ("Pour CHAQUE affirmation, rends un objet JSON "
                 "{affirmation, extrait, source, date_source}. Si une info manque, dis-le "
                 "dans une liste `lacunes`. Ne présente jamais une couverture complète fictive.")

AGENTS = {
    "analyste-replatform": AgentDefinition(
        description="Évalue l'option « replatform » (WebSphere -> Liberty/OpenShift) de GestSin.",
        prompt="Tu analyses UNIQUEMENT l'option replatform. Coûts, risques, délais. " + FORMAT_PREUVE,
        tools=["Read", "Grep", "Glob", "WebSearch"],
    ),
    "analyste-refactor": AgentDefinition(
        description="Évalue l'option « refactor en microservices » de GestSin.",
        prompt="Tu analyses UNIQUEMENT l'option refactor microservices. Coûts, risques, délais. " + FORMAT_PREUVE,
        tools=["Read", "Grep", "Glob", "WebSearch"],
    ),
}

COORDINATEUR = (
    "Tu coordonnes une étude de modernisation de GestSin.\n"
    "1. Délègue EN PARALLÈLE à analyste-replatform et analyste-refactor. Les sous-agents "
    "n'héritent PAS de ton contexte : donne-leur explicitement les faits ci-dessous.\n"
    "   Faits : 120 000 lignes Java EE, WebSphere 8.5, DB2, 3 interfaces MQ, équipe de 6.\n"
    "2. Si un sous-agent échoue ou expire, garde les résultats partiels et signale la lacune.\n"
    "3. En cas de sources contradictoires, conserve les deux valeurs avec leur source.\n"
    "4. Synthèse finale : tableau comparatif + affirmations sourcées + lacunes."
)


async def main():
    options = ClaudeAgentOptions(system_prompt=COORDINATEUR, agents=AGENTS, max_turns=20)
    async for message in query(prompt="Compare replatform et refactor pour GestSin.", options=options):
        print(type(message).__name__)


if __name__ == "__main__":
    asyncio.run(main())
