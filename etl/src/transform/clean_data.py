from __future__ import annotations

from typing import Iterable


def clean_records(
    records: list[dict],
    *,
    required_fields: Iterable[str] = ("user_id", "group", "score"),
    allowed_groups: set[str] | None = None,
) -> tuple[list[dict], dict]:
    """
    Transform layer responsibility: make data statistically usable.

    Exclusion rules are explicit and deterministic; drops are reported (no silent exclusion).
    """
    if allowed_groups is None:
        allowed_groups = {"control", "variant"}

    required = tuple(required_fields)
    dropped_by_reason: dict[str, int] = {}
    cleaned: list[dict] = []

    def drop(reason: str) -> None:
        dropped_by_reason[reason] = dropped_by_reason.get(reason, 0) + 1

    for record in records:
        missing = [field for field in required if field not in record]
        if missing:
            for field in missing:
                drop(f"missing_field:{field}")
            continue

        group = record.get("group")
        if group not in allowed_groups:
            drop("invalid_group")
            continue

        try:
            user_id = int(record.get("user_id"))
        except (TypeError, ValueError):
            drop("invalid_user_id")
            continue

        session_date = record.get("session_date")
        if not isinstance(session_date, str) or not session_date:
            drop("invalid_session_date")
            continue

        score_raw = record.get("score")
        if score_raw is None:
            drop("missing_score")
            continue
        try:
            score = float(score_raw)
        except (TypeError, ValueError):
            drop("invalid_score_type")
            continue
        if not (0.0 <= score <= 100.0):
            drop("score_out_of_bounds")
            continue

        cleaned.append({"user_id": user_id, "group": group, "score": score})

    report = {
        "total_records": len(records),
        "kept_records": len(cleaned),
        "dropped_records": len(records) - len(cleaned),
        "dropped_by_reason": dropped_by_reason,
    }
    return cleaned, report
