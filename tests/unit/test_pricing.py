from app.core.pricing import GLM_PRICING, calculate_token_cost


def test_pricing_known_model():
    # glm-4.5-air: $0.14/M input, $0.14/M output
    cost = calculate_token_cost(
        model="glm-4.5-air",
        tokens_in=1_000_000,
        tokens_out=1_000_000,
        tokens_cached=0,
    )
    assert isinstance(cost, dict)
    assert round(cost["cost_usd"], 4) == 0.2800
    assert cost["cost_vnd"] == round(0.28 * 25400, 2)
    assert cost["pricing_rate"] == {
        "input_per_m": GLM_PRICING["glm-4.5-air"]["input_usd_per_m"],
        "output_per_m": GLM_PRICING["glm-4.5-air"]["output_usd_per_m"],
        "cache_per_m": GLM_PRICING["glm-4.5-air"]["cache_usd_per_m"],
    }


def test_pricing_cached_tokens():
    # glm-4.5-air cache: $0.03/M tokens
    cost = calculate_token_cost(
        model="glm-4.5-air",
        tokens_in=1_000_000,
        tokens_out=0,
        tokens_cached=1_000_000,
    )
    # When tokens_in == tokens_cached, uncached_tokens_in is 0
    assert round(cost["cost_usd"], 4) == 0.0300
    assert cost["cost_vnd"] == round(0.03 * 25400, 2)


def test_pricing_free_model():
    # glm-4.7-flash is free: $0
    cost = calculate_token_cost(
        model="glm-4.7-flash",
        tokens_in=500_000,
        tokens_out=200_000,
        tokens_cached=100_000,
    )
    assert cost["cost_usd"] == 0.0
    assert cost["cost_vnd"] == 0.0


def test_pricing_unknown_model_fallback():
    # Unknown model name should fall back safely to DEFAULT_PRICING without raising
    cost = calculate_token_cost(
        model="unknown-custom-llm",
        tokens_in=1_000_000,
        tokens_out=1_000_000,
    )
    assert cost["cost_usd"] > 0
    assert cost["cost_vnd"] > 0
