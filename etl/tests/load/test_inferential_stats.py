import math

import pytest

from src.load.inferential_stats import compare_group_means, welchs_t_test


def test_welchs_t_test_statistic_sign() -> None:
    a = [1.0, 2.0, 3.0, 4.0]
    b = [10.0, 11.0, 12.0, 13.0]
    t_stat, df = welchs_t_test(a, b)
    assert t_stat < 0
    assert df > 0


def test_compare_group_means_returns_effect_size_and_optional_p_value() -> None:
    records = [
        {"group": "control", "score": 1.0},
        {"group": "control", "score": 2.0},
        {"group": "variant", "score": 10.0},
        {"group": "variant", "score": 11.0},
    ]
    result = compare_group_means(records, value_field="score", group_a="control", group_b="variant")
    assert result["n_a"] == 2
    assert result["n_b"] == 2
    assert math.isfinite(result["t_stat"])
    assert math.isfinite(result["df"])


def test_compare_group_means_requires_both_groups() -> None:
    with pytest.raises(ValueError):
        compare_group_means([{"group": "control", "score": 1.0}], value_field="score")


def test_welchs_t_test_requires_two_per_group() -> None:
    with pytest.raises(ValueError):
        welchs_t_test([1.0], [2.0, 3.0])
