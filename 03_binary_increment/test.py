import sys
from collections.abc import Generator
from pathlib import Path

sys.path.append(Path(__file__).parent.parent.as_posix())
from testlogicmill import TestLogicMill


def generate_test_cases() -> Generator[tuple[str, str]]:
    for i in range(2**10):
        binary = bin(i)[2:]
        binary_incremented = bin(i + 1)[2:]
        yield binary, binary_incremented


TestLogicMill(Path(__file__).parent / "main.mng").run_tests(generate_test_cases())
