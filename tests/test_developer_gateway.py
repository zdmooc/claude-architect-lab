"""Offline fake of the Anthropic Messages interface. No API call or key."""
import sys
from pathlib import Path
from types import SimpleNamespace
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "labs" / "developer_foundations"))
from gateway import ClaudeResponseError, complete_text


class FakeMessages:
    def __init__(self, response):
        self.response = response
        self.calls = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        return self.response


class FakeClient:
    def __init__(self, response):
        self.messages = FakeMessages(response)


def answer(stop="end_turn", content=None):
    if content is None:
        content = [SimpleNamespace(type="text", text="Résumé fictif.")]
    return SimpleNamespace(stop_reason=stop, content=content)


def test_messages_happy_path():
    client = FakeClient(answer())
    out = complete_text(client, model="model-configure", prompt="Bonjour", max_tokens=80)
    assert out == "Résumé fictif."
    assert client.messages.calls == [
        {"model": "model-configure", "max_tokens": 80,
         "messages": [{"role": "user", "content": "Bonjour"}]}
    ]


@pytest.mark.parametrize("stop", ["max_tokens", "tool_use", "stop_sequence", None])
def test_non_final_stop_rejected(stop):
    with pytest.raises(ClaudeResponseError):
        complete_text(FakeClient(answer(stop=stop)), model="model-x", prompt="p")


def test_tool_use_block_rejected_even_with_end_turn():
    r = answer(content=[SimpleNamespace(type="tool_use", id="tool_01", name="payer")])
    with pytest.raises(ClaudeResponseError, match="Non-text"):
        complete_text(FakeClient(r), model="model-x", prompt="p")


def test_empty_content_rejected():
    with pytest.raises(ClaudeResponseError, match="Empty"):
        complete_text(FakeClient(answer(content=[])), model="model-x", prompt="p")


def test_multiple_text_blocks_joined():
    r = answer(content=[SimpleNamespace(type="text", text="Une"),
                        SimpleNamespace(type="text", text=" réponse")])
    assert complete_text(FakeClient(r), model="model-x", prompt="p") == "Une réponse"


@pytest.mark.parametrize("model,prompt,tokens", [
    ("", "ok", 10), ("model", "", 10), ("model", "ok", 0),
    ("model", "ok", -1), ("model", "ok", True),
])
def test_bad_request_is_rejected_before_api_call(model, prompt, tokens):
    client = FakeClient(answer())
    with pytest.raises(ValueError):
        complete_text(client, model=model, prompt=prompt, max_tokens=tokens)
    assert client.messages.calls == []
