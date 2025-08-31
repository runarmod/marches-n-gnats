import sys
from collections.abc import Generator
from pathlib import Path

sys.path.append(Path(__file__).parent.parent.as_posix())
from testlogicmill import TestLogicMill


def generate_test_cases() -> Generator[tuple[str, str]]:
    for a in range(1, 100):
        for b in range(1, 100):
            yield "|" * a + "+" + "|" * b, "|" * (a + b)


TestLogicMill(Path(__file__).parent / "main.mng").run_tests(generate_test_cases())
