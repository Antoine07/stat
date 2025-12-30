import math

import pytest

from src.load.descriptive_stats import describe, mean, median, standard_deviation, variance


def test_mean_median_basic() -> None:
    values = [1.0, 2.0, 3.0, 4.0]
    assert mean(values) == 2.5
    assert median(values) == 2.5


def test_variance_and_std_sample() -> None:
    values = [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]
    assert math.isclose(variance(values, ddof=1), 4.5714285714, rel_tol=1e-9)
    assert math.isclose(standard_deviation(values, ddof=1), math.sqrt(4.5714285714), rel_tol=1e-9)


def test_describe_single_observation_variance_nan() -> None:
    stats = describe([10.0])
    assert stats["n"] == 1
    assert stats["variance"] is None
    assert stats["std_dev"] is None


def test_identical_values_variance_zero() -> None:
    values = [5.0, 5.0, 5.0, 5.0]
    assert variance(values, ddof=1) == 0.0
    assert standard_deviation(values, ddof=1) == 0.0


def test_empty_raises() -> None:
    with pytest.raises(ValueError):
        mean([])
    with pytest.raises(ValueError):
        median([])
    with pytest.raises(ValueError):
        describe([])
    with pytest.raises(ValueError):
        variance([], ddof=1)
