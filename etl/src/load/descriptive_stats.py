from __future__ import annotations

import math
from typing import Iterable, Sequence


def mean(values: Sequence[float]) -> float:
    if len(values) == 0:
        raise ValueError("mean requires at least 1 value")
    return math.fsum(values) / len(values)


def median(values: Sequence[float]) -> float:
    if len(values) == 0:
        raise ValueError("median requires at least 1 value")
    sorted_values = sorted(values)
    mid = len(sorted_values) // 2
    if len(sorted_values) % 2 == 1:
        return float(sorted_values[mid])
    return (sorted_values[mid - 1] + sorted_values[mid]) / 2.0


def variance(values: Sequence[float], *, ddof: int = 1) -> float:
    if len(values) == 0:
        raise ValueError("variance requires at least 1 value")
    if ddof < 0:
        raise ValueError("ddof must be >= 0")
    if len(values) - ddof <= 0:
        raise ValueError(f"variance requires n > ddof (n={len(values)}, ddof={ddof})")

    mu = mean(values)
    sse = math.fsum((x - mu) ** 2 for x in values)
    return sse / (len(values) - ddof)


def standard_deviation(values: Sequence[float], *, ddof: int = 1) -> float:
    return math.sqrt(variance(values, ddof=ddof))


def describe(values: Sequence[float]) -> dict:
    """
    Descriptive statistics: what is observed (no inference).

    Uses sample variance/std (ddof=1) to align with later inferential steps.
    """
    if len(values) == 0:
        raise ValueError("describe requires at least 1 value")

    stats: dict = {
        "n": len(values),
        "mean": mean(values),
        "median": median(values),
        "min": float(min(values)),
        "max": float(max(values)),
    }

    if len(values) >= 2:
        stats["variance"] = variance(values, ddof=1)
        stats["std_dev"] = standard_deviation(values, ddof=1)
    else:
        stats["variance"] = None
        stats["std_dev"] = None

    return stats


def describe_dataset(
    records: list[dict],
    *,
    value_fields: Iterable[str] = ("score",),
    group_field: str = "group",
) -> dict:
    if not records:
        raise ValueError("No records to describe.")

    fields = tuple(value_fields)
    groups = sorted({r[group_field] for r in records})
    counts_by_group = {g: 0 for g in groups}
    for record in records:
        counts_by_group[record[group_field]] += 1

    global_stats = {field: describe([float(r[field]) for r in records]) for field in fields}
    group_stats = {
        g: {field: describe([float(r[field]) for r in records if r[group_field] == g]) for field in fields}
        for g in groups
    }

    return {
        "counts_by_group": counts_by_group,
        "global": global_stats,
        "by_group": group_stats,
    }
