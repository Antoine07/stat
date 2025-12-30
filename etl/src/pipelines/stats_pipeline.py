from __future__ import annotations

import argparse
import json
from pathlib import Path

from src.extract.json_reader import read_json_records
from src.load.descriptive_stats import describe_dataset
from src.load.inferential_stats import compare_group_means
from src.transform.clean_data import clean_records


def run(input_path: Path) -> dict:
    """
    Pipeline responsibility: orchestrate extract -> transform -> describe -> infer.
    No computation logic lives here; it is delegated to layer modules.
    """
    raw = read_json_records(input_path)
    cleaned, cleaning_report = clean_records(raw)

    descriptive = describe_dataset(cleaned)
    inference = compare_group_means(cleaned, value_field="score")

    return {
        "input_path": str(input_path),
        "cleaning_report": cleaning_report,
        "descriptive": descriptive,
        "inferential": inference,
        "limitations": [
            "No causal claims: group differences are descriptive/inferential only.",
            "Assumptions (independence/approximate normality) are not automatically validated.",
            "Small samples can make p-values and effect sizes unstable.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the statistics-first ETL pipeline.")
    parser.add_argument("--input", type=Path, default=Path("data/input.json"), help="Path to JSON input data.")
    args = parser.parse_args()

    result = run(args.input)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
