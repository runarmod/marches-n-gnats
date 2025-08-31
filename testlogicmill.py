from collections.abc import Iterable
from pathlib import Path

from logic_mill import LogicMill, TransitionType


class TestLogicMill:
    def __init__(self, implementation_file: Path):
        self.transition_list = list(
            TransitionType(line.split(" "))
            for line in implementation_file.read_text().strip().splitlines()
        )

    def run_tests(self, test_cases: Iterable[tuple[str, str]]):
        steps = 0
        for test_case in test_cases:
            input_tape, expected_output = test_case
            out, _steps = LogicMill(self.transition_list).run(input_tape)
            assert out == expected_output, f"Got {out}, expected {expected_output}"
            steps += _steps
        print(f"All tests passed! Total steps: {steps}")
