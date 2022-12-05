from pathlib import Path


def solve_part1(lines: list[str]) -> None:
    pass


def solve_part2(lines: list[str]) -> None:
    pass


def main() -> int:

    with open(Path(__file__).parent / "input.txt", encoding='utf-8') as f:
        lines = f.readlines()

    solve_part1(lines)
    solve_part2(lines)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
