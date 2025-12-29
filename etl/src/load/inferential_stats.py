from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Sequence

from src.load.descriptive_stats import mean, variance


@dataclass(frozen=True)
class MeanComparison:
    group_a: str
    group_b: str
    n_a: int
    n_b: int
    mean_a: float
    mean_b: float
    var_a: float
    var_b: float
    mean_diff: float
    cohens_d: float | None
    t_stat: float
    df: float
    p_value: float | None


def _values_for(records: list[dict], *, group_field: str, group: str, value_field: str) -> list[float]:
    return [float(r[value_field]) for r in records if r[group_field] == group]


def _cohens_d(a: Sequence[float], b: Sequence[float]) -> float | None:
    if len(a) < 2 or len(b) < 2:
        return None
    var_a = variance(a, ddof=1)
    var_b = variance(b, ddof=1)
    pooled = ((len(a) - 1) * var_a + (len(b) - 1) * var_b) / (len(a) + len(b) - 2)
    if pooled <= 0:
        return None
    return (mean(a) - mean(b)) / math.sqrt(pooled)


def welchs_t_test(a: Sequence[float], b: Sequence[float]) -> tuple[float, float]:
    if len(a) < 2 or len(b) < 2:
        raise ValueError("Welch t-test requires at least 2 observations per group.")

    mean_a = mean(a)
    mean_b = mean(b)
    var_a = variance(a, ddof=1)
    var_b = variance(b, ddof=1)

    se2 = var_a / len(a) + var_b / len(b)
    if se2 <= 0:
        raise ValueError("Standard error is zero; t-test is not defined.")

    t_stat = (mean_a - mean_b) / math.sqrt(se2)
    df_num = se2**2
    df_den = (var_a**2) / (len(a) ** 2 * (len(a) - 1)) + (var_b**2) / (len(b) ** 2 * (len(b) - 1))
    df = df_num / df_den
    return t_stat, df


def _two_sided_p_value(t_stat: float, df: float) -> float | None:
    try:
        from scipy import stats  # type: ignore
    except Exception:
        return None
    return float(2.0 * stats.t.sf(abs(t_stat), df))


def compare_group_means(
    records: list[dict],
    *,
    value_field: str = "score",
    group_field: str = "group",
    group_a: str = "control",
    group_b: str = "variant",
) -> MeanComparison:
    """
    Inferential statistics: what is concluded (under explicit assumptions).

    Assumptions (not automatically verified):
    - independent observations within/across groups
    - approximately continuous outcome
    - for Welch: unequal variances allowed, approximate normality for small n
    """
    a = _values_for(records, group_field=group_field, group=group_a, value_field=value_field)
    b = _values_for(records, group_field=group_field, group=group_b, value_field=value_field)
    if len(a) == 0 or len(b) == 0:
        raise ValueError("Both groups must be present to compare means.")

    t_stat, df = welchs_t_test(a, b)
    p_value = _two_sided_p_value(t_stat, df)

    return MeanComparison(
        group_a=group_a,
        group_b=group_b,
        n_a=len(a),
        n_b=len(b),
        mean_a=mean(a),
        mean_b=mean(b),
        var_a=variance(a, ddof=1) if len(a) >= 2 else float("nan"),
        var_b=variance(b, ddof=1) if len(b) >= 2 else float("nan"),
        mean_diff=mean(a) - mean(b),
        cohens_d=_cohens_d(a, b),
        t_stat=t_stat,
        df=df,
        p_value=p_value,
    )

