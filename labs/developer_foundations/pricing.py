"""Cost arithmetic for synthetic examples; caller supplies *verified* tariffs.

Tariffs are expressed as EUR or USD / 1,000,000 tokens; choose one unit and
use it consistently. Model tariffs are NOT embedded in this training lab.
"""
from decimal import Decimal, InvalidOperation


def _d(value, label: str) -> Decimal:
    if isinstance(value, bool):
        raise ValueError(f"{label}: boolean is not a number")
    try:
        x = Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise ValueError(f"{label}: invalid decimal") from None
    if not x.is_finite() or x < 0:
        raise ValueError(f"{label}: expected finite non-negative number")
    return x


def estimate_token_cost(*, input_tokens: int, output_tokens: int,
                        input_rate_per_million, output_rate_per_million,
                        review_cost=0) -> Decimal:
    """Return an unrounded monetary estimate (no invented pricing)."""
    if (isinstance(input_tokens, bool) or isinstance(output_tokens, bool)
            or not isinstance(input_tokens, int) or not isinstance(output_tokens, int)
            or input_tokens < 0 or output_tokens < 0):
        raise ValueError("Token counts must be non-negative integers")
    return (Decimal(input_tokens) * _d(input_rate_per_million, "input rate")
            + Decimal(output_tokens) * _d(output_rate_per_million, "output rate")
           ) / Decimal(1_000_000) + _d(review_cost, "review cost")
