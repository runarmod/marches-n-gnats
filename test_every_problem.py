from pathlib import Path


def test_dir(problem_dir: Path) -> bool:
    print(f"Running tests in {problem_dir.name}")
    __import__(f"{problem_dir.name}.test")
    print()


def main():
    for problem_dir in Path(__file__).parent.iterdir():
        if problem_dir.is_dir() and (problem_dir / "test.py").exists():
            test_dir(problem_dir)


if __name__ == "__main__":
    main()
