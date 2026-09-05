"""Reference implementation of the lesson's row-based quality metric."""
from __future__ import annotations

import pandas as pd


def implausible_fraction(flagged_rows: pd.DataFrame, n_input: int) -> float:
    """Count excluded input rows with either exact reason token, once per row.

    The flagged-row contract contains one row per excluded input measurement.
    The denominator includes every input measurement, including retained rows.
    """
    if n_input == 0:
        return 0.0
    relevant = {"implausible_height", "implausible_weight"}
    count = sum(bool(relevant.intersection(reasons.split(";")))
                for reasons in flagged_rows["reasons"])
    return count / n_input
