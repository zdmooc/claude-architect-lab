"""M1 · Leçon 1 — Premier appel à l'API Messages.

Code PROPOSÉ (vérifié contre la documentation du SDK Python au 13/11/2026),
NON EXÉCUTÉ par le formateur : à lancer par l'apprenant avec sa propre clé.

Prérequis : variable d'environnement ANTHROPIC_API_KEY définie (jamais dans le code).
"""
import anthropic

# Modèle par défaut recommandé par la documentation. Pour réduire les coûts
# pendant l'apprentissage, tu peux choisir "claude-haiku-5-5" : c'est TON choix.
MODEL = "claude-opus-5-5"

client = anthropic.Anthropic()  # lit ANTHROPIC_API_KEY dans l'environnement

response = client.messages.create(
    model=MODEL,
    max_tokens=1024,
    system="Tu es un assistant de gestion de sinistres. Réponds en français, en 3 phrases maximum.",
    messages=[
        {"role": "user", "content": "Qu'est-ce qu'une franchise dans un contrat d'assurance auto ?"}
    ],
)

# response.content est une LISTE de blocs (text, thinking, tool_use...).
# On n'affiche que les blocs de type "text".
for block in response.content:
    if block.type == "text":
        print(block.text)

print("---")
print("stop_reason :", response.stop_reason)
print("tokens envoyés  :", response.usage.input_tokens)
print("tokens générés  :", response.usage.output_tokens)
