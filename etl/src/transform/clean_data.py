from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class CleaningReport:
    total_records: int
    kept_records: int
    dropped_records: int
    dropped_by_reason: dict[str, int]


def _bump(counter: dict[str, int], key: str) -> None:
    counter[key] = counter.get(key, 0) + 1


def clean_records(
    records: list[dict],
    *,
    required_fields: Iterable[str] = ("user_id", "group", "score", "time_spent", "errors", "session_date"),
    allowed_groups: set[str] | None = None,
) -> tuple[list[dict], CleaningReport]:
    """
    Transform layer responsibility: make data statistically usable.

    Exclusion rules are explicit and deterministic; drops are reported (no silent exclusion).
    """
    if allowed_groups is None:
        allowed_groups = {"control", "variant"}

    required = tuple(required_fields)
    dropped_by_reason: dict[str, int] = {}
    cleaned: list[dict] = []

    for record in records:
        missing = [field for field in required if field not in record]
        if missing:
            for field in missing:
                _bump(dropped_by_reason, f"missing_field:{field}")
            continue

        group = record.get("group")
        if group not in allowed_groups:
            _bump(dropped_by_reason, "invalid_group")
            continue

        try:
            user_id = int(record.get("user_id"))
        except (TypeError, ValueError):
            _bump(dropped_by_reason, "invalid_user_id")
            continue

        session_date = record.get("session_date")
        if not isinstance(session_date, str) or not session_date:
            _bump(dropped_by_reason, "invalid_session_date")
            continue

        score_raw = record.get("score")
        if score_raw is None:
            _bump(dropped_by_reason, "missing_score")
            continue
        try:
            score = float(score_raw)
        except (TypeError, ValueError):
            _bump(dropped_by_reason, "invalid_score_type")
            continue
        if not (0.0 <= score <= 100.0):
            _bump(dropped_by_reason, "score_out_of_bounds")
            continue

        time_spent_raw = record.get("time_spent")
        if time_spent_raw is None:
            _bump(dropped_by_reason, "missing_time_spent")
            continue
        try:
            time_spent = float(time_spent_raw)
        except (TypeError, ValueError):
            _bump(dropped_by_reason, "invalid_time_spent_type")
            continue
        if time_spent <= 0:
            _bump(dropped_by_reason, "time_spent_out_of_bounds")
            continue

        errors_raw = record.get("errors")
        if errors_raw is None:
            _bump(dropped_by_reason, "missing_errors")
            continue
        try:
            errors = int(errors_raw)
        except (TypeError, ValueError):
            _bump(dropped_by_reason, "invalid_errors_type")
            continue
        if errors < 0:
            _bump(dropped_by_reason, "errors_out_of_bounds")
            continue

        cleaned.append(
            {
                "user_id": user_id,
                "group": group,
                "score": score,
                "time_spent": time_spent,
                "errors": errors,
                "session_date": session_date,
            }
        )

    report = CleaningReport(
        total_records=len(records),
        kept_records=len(cleaned),
        dropped_records=len(records) - len(cleaned),
        dropped_by_reason=dropped_by_reason,
    )
    return cleaned, report

