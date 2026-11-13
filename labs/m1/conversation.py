"""M1 · Leçon 2 — Conversation multi-tours : l'application porte l'état.

Code PROPOSÉ, NON EXÉCUTÉ par le formateur.
Tape 'quit' pour sortir.
"""
import anthropic

MODEL = "claude-opus-5-5"  # ou "claude-haiku-5-5" pour réduire les coûts (ton choix)
SYSTEM = "Tu es un assistant de gestion de sinistres. Réponds en français, brièvement."

client = anthropic.Anthropic()
historique = []  # <- l'ÉTAT de la conversation vit ICI, côté application

while True:
    question = input("Vous > ").strip()
    if question.lower() == "quit":
        break

    historique.append({"role": "user", "content": question})

    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system=SYSTEM,
        messages=historique,  # on renvoie TOUT l'historique à chaque appel
    )

    if response.stop_reason == "refusal":
        print("Claude > (demande refusée)")
        historique.pop()  # on n'enregistre pas un tour refusé
        continue

    # On ajoute la réponse COMPLÈTE (tous les blocs) à l'historique.
    historique.append({"role": "assistant", "content": response.content})

    texte = "".join(b.text for b in response.content if b.type == "text")
    print("Claude >", texte)
    print(f"   [stop_reason={response.stop_reason} | in={response.usage.input_tokens} | out={response.usage.output_tokens}]")
