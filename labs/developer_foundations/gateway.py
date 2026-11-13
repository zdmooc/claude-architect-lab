"""Messages API adapter – testable with a fake, no API key required.

The real Anthropic SDK has client.messages.create(...). We accept that interface
by dependency injection and explicitly reject incomplete/non-text responses.
Do not interpret generated text as an authorized business decision.
"""

from typing import Any


class ClaudeResponseError(ValueError):
    """Returned content cannot be consumed as a complete text answer."""


def complete_text(client: Any, *, model: str, prompt: str,
                  max_tokens: int = 256) -> str:
    """Return text only on a *complete* end_turn response.

    This example intentionally does not execute tools or implement streaming.
    A tool_use response is NOT a final user-facing answer.
    """
    if not isinstance(model, str) or not model.strip():
        raise ValueError("A non-empty, configured model ID is required")
    if not isinstance(prompt, str) or not prompt.strip():
        raise ValueError("A non-empty prompt is required")
    if isinstance(max_tokens, bool) or not isinstance(max_tokens, int) or max_tokens <= 0:
        raise ValueError("max_tokens must be a positive integer")

    response = client.messages.create(
        model=model, max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    stop = getattr(response, "stop_reason", None)
    if stop != "end_turn":
        raise ClaudeResponseError(f"Unfinished or unsupported stop_reason: {stop!r}")

    blocks = getattr(response, "content", None)
    if not isinstance(blocks, list) or not blocks:
        raise ClaudeResponseError("Empty or missing response content")

    text = []
    for block in blocks:
        if getattr(block, "type", None) != "text":
            # Deliberately not treating tool_use, thinking or unknown blocks
            # as a final answer. A richer adapter can handle other blocks.
            raise ClaudeResponseError("Non-text block requires dedicated handling")
        value = getattr(block, "text", None)
        if not isinstance(value, str):
            raise ClaudeResponseError("Invalid text block")
        text.append(value)
    output = "".join(text).strip()
    if not output:
        raise ClaudeResponseError("Empty text answer")
    return output
