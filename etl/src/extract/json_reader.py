from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable


REQUIRED_FIELDS = ("user_id", "group", "score")


def read_json_records(path: Path, required_fields: Iterable[str] = REQUIRED_FIELDS) -> list[dict]:
    """
    Extract layer responsibility: load raw observations (no cleaning, no stats).

    - Reads a JSON file expected to contain a list of objects.
    - Validates presence of minimal required fields (values may still be null/invalid).
    - Returns raw Python objects: list[dict].
    """
    if not path.exists():
        raise FileNotFoundError(path)

    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("Input JSON must be a list of records.")

    required = tuple(required_fields)
    records: list[dict] = []
    for index, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(f"Record {index} must be an object.")
        missing = [field for field in required if field not in item]
        if missing:
            raise ValueError(f"Record {index} missing required field(s): {', '.join(missing)}")
        records.append(item)

    return records
