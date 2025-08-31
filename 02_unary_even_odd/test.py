import sys
from collections.abc import Generator
from pathlib import Path

sys.path.append(Path(__file__).parent.parent.as_posix())
from testlogicmill import TestLogicMill


def generate_test_cases() -> Generator[tuple[str, str]]:
    for n in range(1, 100):
        if n % 2 == 0:
            yield "|" * n, "E"
        else:
            yield "|" * n, "O"


TestLogicMill(Path(__file__).parent / "main.mng").run_tests(generate_test_cases())
