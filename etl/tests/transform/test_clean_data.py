from src.transform.clean_data import clean_records


def test_clean_records_converts_and_drops_with_report() -> None:
    raw = [
        {
            "user_id": "101",
            "group": "control",
            "score": "85",
        },
        {  # missing score
            "user_id": 102,
            "group": "control",
            "score": None,
        },
        {  # invalid group
            "user_id": 103,
            "group": "unknown",
            "score": 10,
        },
        {  # invalid bounds
            "user_id": 104,
            "group": "variant",
            "score": 1000,
        },
    ]

    cleaned, report = clean_records(raw)
    assert report["total_records"] == 4
    assert report["kept_records"] == 1
    assert report["dropped_records"] == 3
    assert report["dropped_by_reason"]["missing_score"] == 1
    assert report["dropped_by_reason"]["invalid_group"] == 1
    assert report["dropped_by_reason"]["score_out_of_bounds"] == 1

    row = cleaned[0]
    assert row["user_id"] == 101
    assert row["group"] == "control"
    assert row["score"] == 85.0
