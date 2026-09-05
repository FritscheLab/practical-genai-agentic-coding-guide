"""Verify the instructor solution without changing the working package."""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    solution = Path(__file__).resolve().parent / "solution"
    with tempfile.TemporaryDirectory(prefix="pgacg-qc-solution-") as temporary:
        sandbox = Path(temporary)
        # Copy tests too: subprocess integration tests derive their src and data
        # paths from the test file, so all invocations exercise the overlay.
        for relative in ("src/pgacg", "tests", "data/example"):
            shutil.copytree(root / relative, sandbox / relative,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "*.egg-info"))
        shutil.copyfile(root / "pyproject.toml", sandbox / "pyproject.toml")
        for name in ("qc.py", "cli.py"):
            shutil.copyfile(solution / name, sandbox / "src/pgacg" / name)
        checker = sandbox / "check_acceptance.py"
        shutil.copyfile(root / "examples/qc_gate/check_acceptance.py", checker)
        environment = {**os.environ, "PYTHONPATH": str(sandbox / "src"), "PYTHONNOUSERSITE": "1"}
        commands = [
            [sys.executable, "-m", "pytest", "-q", "tests"],
            [sys.executable, str(checker)],
        ]
        for command in commands:
            print(f"Running isolated solution check: {' '.join(command)}", flush=True)
            result = subprocess.run(command, cwd=sandbox, env=environment, check=False)
            if result.returncode != 0:
                return result.returncode
    print("Reference solution passed baseline regression tests and QC acceptance checks. "
          "The working package was not modified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
