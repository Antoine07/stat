import json
from pathlib import Path

import pytest

from src.extract.json_reader import read_json_records


def test_read_json_records_valid(tmp_path: Path) -> None:
    path = tmp_path / "input.json"
    path.write_text(
        json.dumps(
            [
                {
                    "user_id": 1,
                    "group": "control",
                    "score": 10,
                }
            ]
        ),
        encoding="utf-8",
    )
    records = read_json_records(path)
    assert isinstance(records, list)
    assert records[0]["user_id"] == 1


def test_read_json_records_missing_field_raises(tmp_path: Path) -> None:
    path = tmp_path / "input.json"
    path.write_text(json.dumps([{"user_id": 1, "group": "control"}]), encoding="utf-8")
    with pytest.raises(ValueError, match="missing required field"):
        read_json_records(path)


def test_read_json_records_non_list_raises(tmp_path: Path) -> None:
    path = tmp_path / "input.json"
    path.write_text(json.dumps({"not": "a list"}), encoding="utf-8")
    with pytest.raises(ValueError, match="must be a list"):
        read_json_records(path)
