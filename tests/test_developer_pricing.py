"""Pure Decimal arithmetic using example tariffs, NOT live Anthropic rates."""
import sys
from decimal import Decimal
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "labs" / "developer_foundations"))
from pricing import estimate_token_cost


def test_cost_formula_uses_million_token_unit():
    # Synthetic prices: 2 per million input, 10 per million output.
    out = estimate_token_cost(input_tokens=1000, output_tokens=200,
                              input_rate_per_million="2", output_rate_per_million="10")
    assert out == Decimal("0.004")


def test_review_cost_included():
    out = estimate_token_cost(input_tokens=0, output_tokens=0,
                              input_rate_per_million=2, output_rate_per_million=10,
                              review_cost="0.50")
    assert out == Decimal("0.50")


@pytest.mark.parametrize("input_tokens,output_tokens", [
    (-1, 2), (1, -1), (True, 1), (1, 1.5),
])
def test_invalid_token_counts(input_tokens, output_tokens):
    with pytest.raises(ValueError):
        estimate_token_cost(input_tokens=input_tokens, output_tokens=output_tokens,
                            input_rate_per_million=2, output_rate_per_million=10)


@pytest.mark.parametrize("rate", ["NaN", "Infinity", "-1", None, "not a rate", True])
def test_invalid_rates(rate):
    with pytest.raises(ValueError):
        estimate_token_cost(input_tokens=100, output_tokens=100,
                            input_rate_per_million=rate, output_rate_per_million=10)


def test_zero_tokens_zero_cost():
    assert estimate_token_cost(input_tokens=0, output_tokens=0,
                               input_rate_per_million=0, output_rate_per_million=0
                               ) == Decimal("0")
