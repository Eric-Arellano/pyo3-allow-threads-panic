#!/usr/bin/env python3.9

import os
import subprocess
import sys
import shutil
from pathlib import Path


def main() -> None:
    build_extension()
    run_python_app()


def build_extension() -> None:
    subprocess.run(["./cargo", "build"], check=True)

    dest = Path("src/python/allow_threads/allow_threads.so")
    if dest.exists():
        dest.unlink()

    extension = "so" if sys.platform == "linux" else "dylib"
    shutil.copy(
        f"src/rust/allow_threads/target/debug/liballow_threads.{extension}",
        "src/python/allow_threads/allow_threads.so",
    )


def run_python_app() -> None:
    result = subprocess.run(
        [sys.executable, "src/python/allow_threads/main.py"],
        env={**os.environ, "PYTHONPATH": "src/python"},
    )
    if result.returncode != 0:
        sys.exit(result.returncode)


if __name__ == "__main__":
    main()
