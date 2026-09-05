"""Independent acceptance checks for lessons 2–4; the baseline should fail these.

Run from the repository root after installing the development environment:
    python examples/qc_gate/check_acceptance.py

The expected fractions and fixture outcomes below are specified by hand. This
checker never imports the reference solution or uses cleaning code as its oracle.
"""
from __future__ import annotations

import csv
import hashlib
import importlib
import json
import math
import re
import subprocess
import sys
import tempfile
from collections.abc import Callable
from pathlib import Path

import pandas as pd

EHR_COLUMNS = ["person_id", "encounter_id", "bmi", "height_cm", "weight_kg", "measurement_date"]
DEMO_COLUMNS = [
    "person_id", "date_of_birth", "age", "age_bin", "deceased", "race_clean",
    "ethnicity_clean", "race_ethnicity", "race_ethnicity_harmonized", "sex_gender",
    "marital_status_name", "zip3",
]
ARTIFACTS = {
    "summary.md", "outputs/cleaned_bmi_person.tsv", "outputs/flagged_rows.tsv",
    "outputs/flagged_people.tsv", "outputs/cleaned_bmi_person_data_dictionary.md",
}
# BMI, height, weight and expected reason tokens, independent of the implementation.
ROW_TYPES = {
    "good": (20, 200, 80, set()),
    "height": (20, 90, 80, {"implausible_height", "bmi_mismatch"}),
    "weight": (20, 200, 400, {"implausible_weight", "bmi_mismatch"}),
    "both": (20, 90, 400, {"implausible_height", "implausible_weight", "bmi_mismatch"}),
    "missing": (20, "", 80, {"missing_height"}),
    "mismatch": (25, 200, 80, {"bmi_mismatch"}),
}


def require(condition: bool, message: str) -> None:
    """Raise a useful failure even when Python is run with optimization enabled."""
    if not condition:
        raise AssertionError(message)


def check_fractions(fraction: Callable[[pd.DataFrame, int], float]) -> int:
    cases = [
        ("equality", ["implausible_height", "implausible_weight"], 10, 0.20),
        ("both reasons counted once", ["implausible_height;implausible_weight"], 10, 0.10),
        ("three rows", ["implausible_height", "implausible_weight", "implausible_height"], 10, 0.30),
        ("irrelevant exclusions", ["missing_height", "missing_weight", "bmi_mismatch",
                                   "per_person_iqr_outlier", "implausible_bmi"], 10, 0.0),
        ("exact tokens", ["not_implausible_height", "implausible_weights",
                           "implausible_height_extra", "other;implausible_weight;other"], 10, 0.10),
        ("repeated token counted once", ["implausible_height;implausible_height"], 10, 0.10),
        ("no exclusions", [], 10, 0.0),
        ("empty input", [], 0, 0.0),
    ]
    for name, reasons, n_input, expected in cases:
        frame = pd.DataFrame({"reasons": pd.Series(reasons, dtype=str)})
        before = frame.copy(deep=True)
        actual = fraction(frame, n_input)
        require(math.isfinite(actual) and math.isclose(actual, expected, abs_tol=1e-12),
                f"Fraction case {name!r}: expected {expected}, got {actual}")
        pd.testing.assert_frame_equal(frame, before)
    print(f"PASS: {len(cases)} independent fraction cases")
    return len(cases)


def write_fixture(directory: Path, kinds: list[str]) -> tuple[Path, Path]:
    directory.mkdir(parents=True)
    ehr, demo = directory / "ehr.tsv", directory / "demo.tsv"
    with ehr.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(EHR_COLUMNS)
        for index, kind in enumerate(kinds):
            bmi, height, weight, _ = ROW_TYPES[kind]
            writer.writerow([f"p{index:02}", f"e{index:02}", bmi, height, weight, "2020-01-01"])
    with demo.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=DEMO_COLUMNS, delimiter="\t")
        writer.writeheader()
        for index in range(len(kinds)):
            writer.writerow({"person_id": f"p{index:02}", "date_of_birth": "1980-01-01",
                             "age": 40, "zip3": "012"})
    return ehr, demo


def invoke(inputs: tuple[Path, Path], runs: Path, run_id: str, limit: str | None = None) -> subprocess.CompletedProcess:
    command = [sys.executable, "-m", "pgacg", "demo", "--ehr", str(inputs[0]),
               "--demo", str(inputs[1]), "--runs_dir", str(runs), "--run_id", run_id]
    if limit is not None:
        command.append(f"--max_implausible_fraction={limit}")
    return subprocess.run(command, capture_output=True, text=True, check=False, timeout=30)


def tsv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def check_report(run: Path, kinds: list[str], observed: float, limit: float, outcome: str) -> None:
    for relative in ARTIFACTS | {"manifest.json", "logs/pipeline.log"}:
        require((run / relative).is_file(), f"Missing normal artifact: {run / relative}")
    manifest = json.loads((run / "manifest.json").read_text(encoding="utf-8"))
    qc = manifest.get("qc", {})
    for key, expected in (("observed_fraction", observed), ("max_implausible_fraction", limit)):
        actual = qc.get(key)
        require(isinstance(actual, int | float) and not isinstance(actual, bool),
                f"manifest.qc.{key} must be a JSON number, got {actual!r}")
        require(math.isclose(actual, expected, abs_tol=1e-12),
                f"manifest.qc.{key}: expected {expected}, got {actual}")
    require(qc.get("outcome") == outcome, f"Expected QC outcome {outcome}, got {qc}")
    status = "success" if outcome == "pass" else "qc_failed"
    require(manifest.get("status") == status, f"Expected manifest status {status}")
    require(manifest.get("finished_at") is not None, "QC run must have a finish timestamp")
    require(manifest.get("metrics", {}).get("n_rows_input") == len(kinds), "Wrong input-row count")

    summary = (run / "summary.md").read_text(encoding="utf-8")
    for key, expected in (("observed_fraction", observed), ("max_implausible_fraction", limit)):
        match = re.search(rf"`{key}`:\s*([0-9.eE+-]+)", summary)
        require(match is not None, f"Summary is missing `{key}`: <number>")
        require(math.isclose(float(match.group(1)), expected, abs_tol=1e-12),
                f"Wrong summary value for {key}: {match.group(1)}")
    require(re.search(rf"`outcome`:\s*{outcome}\b", summary) is not None,
            f"Summary must report `outcome`: {outcome}")
    require(f"**Status:** {status}" in summary, "Summary and manifest status must agree")
    require("Category distributions" in summary, "QC must preserve the normal summary")
    require((run / "logs/pipeline.log").stat().st_size > 0, "Run log must not be empty")
    require(ARTIFACTS <= set(manifest.get("artifacts", {})), "Manifest is missing normal artifacts")
    for relative, metadata in manifest["artifacts"].items():
        content = (run / relative).read_bytes()
        require(metadata["sha256"] == hashlib.sha256(content).hexdigest(),
                f"Stale checksum for {relative}; finalize the manifest after writing QC")
        require(metadata["size_bytes"] == len(content), f"Stale size for {relative}")

    cleaned = tsv_rows(run / "outputs/cleaned_bmi_person.tsv")
    flagged = tsv_rows(run / "outputs/flagged_rows.tsv")
    people = tsv_rows(run / "outputs/flagged_people.tsv")
    expected_clean = {f"e{index:02}" for index, kind in enumerate(kinds) if kind == "good"}
    expected_flagged = {f"e{index:02}": ROW_TYPES[kind][3]
                        for index, kind in enumerate(kinds) if kind != "good"}
    require(len(cleaned) == len(expected_clean), "QC changed the number of cleaned rows")
    require({row["encounter_id"] for row in cleaned} == expected_clean, "Wrong retained records")
    require(all(row["zip3"] == "012" for row in cleaned), "Leading-zero ZIP prefixes must survive")
    require(len(flagged) == len(expected_flagged), "Excluded input rows must appear exactly once")
    actual_flags = {row["encounter_id"]: set(row["reasons"].split(";")) for row in flagged}
    require(actual_flags == expected_flagged, f"Unexpected flagged rows/reasons: {actual_flags}")
    require(len(people) == len(expected_flagged), "QC changed flagged-person output")


def check_cli(directory: Path) -> int:
    # Each person has one measurement, so representative selection cannot alter
    # the independently specified gate numerator or denominator.
    equality = ["height", "weight", "missing", "mismatch", *(["good"] * 6)]
    failure = ["height", "weight", "both", "missing", "mismatch", *(["good"] * 5)]
    cases = [
        ("equality", equality, None, 0.20, 0.20, "pass"),
        ("both_once", ["both", "missing", "mismatch", *(["good"] * 7)], None, 0.10, 0.20, "pass"),
        ("failure", failure, None, 0.30, 0.20, "fail"),
        ("irrelevant", ["missing", "mismatch", *(["good"] * 8)], None, 0.0, 0.20, "pass"),
        ("empty", [], None, 0.0, 0.20, "pass"),
        ("custom_equality", failure, "0.30", 0.30, 0.30, "pass"),
        ("custom_fail", equality, "0.10", 0.20, 0.10, "fail"),
        ("zero_boundary", ["good"] * 10, "0", 0.0, 0.0, "pass"),
        ("one_boundary", ["height"] * 10, "1", 1.0, 1.0, "pass"),
    ]
    runs = directory / "runs"
    for name, kinds, argument, fraction, limit, outcome in cases:
        inputs = write_fixture(directory / name, kinds)
        process = invoke(inputs, runs, name, argument)
        expected_code = 0 if outcome == "pass" else 2
        require(process.returncode == expected_code,
                f"CLI case {name}: expected exit {expected_code}, got {process.returncode}\n{process.stderr}")
        check_report(runs / name, kinds, fraction, limit, outcome)
    print(f"PASS: {len(cases)} CLI arithmetic, threshold, output, and provenance cases")

    inputs = write_fixture(directory / "invalid", ["good"])
    invalid_values = ["-0.1", "1.1", "nan", "inf", "-inf", "text"]
    for index, value in enumerate(invalid_values):
        name = f"invalid_{index}"
        process = invoke(inputs, runs, name, value)
        require(process.returncode == 2, f"CLI must reject invalid limit {value!r}")
        require(not (runs / name).exists(), f"Invalid limit {value!r} created a run")
    print(f"PASS: {len(invalid_values)} invalid argument cases")

    inputs[0].write_text("person_id\np00\n", encoding="utf-8")
    process = invoke(inputs, runs, "bad_input")
    require(process.returncode == 1, f"Input errors must return 1, got {process.returncode}")
    failed = runs / "bad_input"
    manifest = json.loads((failed / "manifest.json").read_text(encoding="utf-8"))
    require(manifest["status"] == "failed", "An input error must not be called a QC failure")
    require("Missing required columns" in manifest["error"], "Input error details were lost")
    require((failed / "summary.md").is_file() and (failed / "logs/pipeline.log").is_file(),
            "Input failures must retain summary and log")
    print("PASS: runtime/input errors remain distinct from QC failures")
    return len(cases) + len(invalid_values) + 1


def main() -> int:
    try:
        qc = importlib.import_module("pgacg.qc")
    except ModuleNotFoundError as exc:
        if exc.name in {"pgacg", "pgacg.qc"}:
            print("QC exercise is not implemented in the active package. "
                  "Complete lessons 2–4 and add pgacg.qc.implausible_fraction, then rerun. "
                  "This failure is expected on the published baseline.", file=sys.stderr)
            return 1
        raise
    if not callable(getattr(qc, "implausible_fraction", None)):
        print("QC exercise is incomplete: pgacg.qc.implausible_fraction is missing.", file=sys.stderr)
        return 1
    try:
        count = check_fractions(qc.implausible_fraction)
        with tempfile.TemporaryDirectory(prefix="pgacg-qc-acceptance-") as temporary:
            count += check_cli(Path(temporary))
    except (AssertionError, OSError, ValueError, TypeError, KeyError, subprocess.TimeoutExpired) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print(f"PASS: all {count} QC acceptance cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
