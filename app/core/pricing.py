from typing import Any

# Z.ai GLM Pricing per 1,000,000 tokens (USD)
# Reference: https://docs.z.ai/guides/overview/pricing
GLM_PRICING: dict[str, dict[str, float]] = {
    # Recommended production models
    "glm-4.5-air": {
        "input_usd_per_m": 0.14,
        "output_usd_per_m": 0.14,
        "cache_usd_per_m": 0.03,
    },
    "glm-4-air": {
        "input_usd_per_m": 0.14,
        "output_usd_per_m": 0.14,
        "cache_usd_per_m": 0.03,
    },
    "glm-4-plus": {
        "input_usd_per_m": 1.40,
        "output_usd_per_m": 1.40,
        "cache_usd_per_m": 0.28,
    },
    "glm-4-long": {
        "input_usd_per_m": 0.14,
        "output_usd_per_m": 0.14,
        "cache_usd_per_m": 0.03,
    },
    # Free tier models (for reference)
    "glm-4.5-flash": {
        "input_usd_per_m": 0.0,
        "output_usd_per_m": 0.0,
        "cache_usd_per_m": 0.0,
    },
    "glm-4.7-flash": {
        "input_usd_per_m": 0.0,
        "output_usd_per_m": 0.0,
        "cache_usd_per_m": 0.0,
    },
}

DEFAULT_PRICING = {
    "input_usd_per_m": 0.14,
    "output_usd_per_m": 0.14,
    "cache_usd_per_m": 0.03,
}

USD_TO_VND_EXCHANGE_RATE = 25400.0


def calculate_token_cost(
    model: str,
    tokens_in: int,
    tokens_out: int,
    tokens_cached: int = 0,
) -> dict[str, Any]:
    """
    Calculates estimated cost in USD and VND for a given token usage and model.
    """
    model_key = model.lower().strip()
    rate = GLM_PRICING.get(model_key, DEFAULT_PRICING)

    uncached_tokens_in = max(0, tokens_in - tokens_cached)
    cost_input = (uncached_tokens_in / 1_000_000.0) * rate["input_usd_per_m"]
    cost_cache = (tokens_cached / 1_000_000.0) * rate.get("cache_usd_per_m", 0.0)
    cost_output = (tokens_out / 1_000_000.0) * rate["output_usd_per_m"]

    cost_usd = cost_input + cost_cache + cost_output
    cost_vnd = cost_usd * USD_TO_VND_EXCHANGE_RATE

    return {
        "cost_usd": round(cost_usd, 6),
        "cost_vnd": round(cost_vnd, 2),
        "pricing_rate": {
            "input_per_m": rate["input_usd_per_m"],
            "output_per_m": rate["output_usd_per_m"],
            "cache_per_m": rate.get("cache_usd_per_m", 0.0),
        },
    }
