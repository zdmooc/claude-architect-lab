"""M3 · L3 — Même assistant avec le TOOL RUNNER du SDK (beta).

Code PROPOSÉ, suit la documentation du SDK (`beta_tool`, `client.beta.messages.tool_runner`),
compilé, NON EXÉCUTÉ contre l'API par le formateur.
Le SDK écrit la boucle ; les outils restent les nôtres.
"""
import anthropic
from anthropic import beta_tool

from outils_contrats import executer

client = anthropic.Anthropic()


@beta_tool
def consulter_contrat(numero: str) -> str:
    """Lit le détail d'UN contrat à partir de son numéro exact (ex. 'AUTO-4471').

    Args:
        numero: Numéro de contrat exact.
    """
    r = executer("consulter_contrat", {"numero": numero})
    return r["content"]


@beta_tool
def lister_sinistres(numero: str) -> str:
    """Liste les sinistres d'UN contrat. Une liste vide = aucun sinistre déclaré.

    Args:
        numero: Numéro de contrat exact.
    """
    return executer("lister_sinistres", {"numero": numero})["content"]


runner = client.beta.messages.tool_runner(
    model="claude-opus-5-5",
    max_tokens=4000,
    tools=[consulter_contrat, lister_sinistres],
    messages=[{"role": "user", "content": "Quelle est la franchise et les sinistres du contrat AUTO-4471 ?"}],
)
for message in runner:            # chaque itération = une réponse du modèle
    for b in message.content:
        if b.type == "text":
            print(b.text)
