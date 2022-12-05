from __future__ import annotations

from pathlib import Path


class Elve:

    def __init__(self, section: str):
        lower, upper = section.split("-")

        self.lower = int(lower)
        self.upper = int(upper)

    def contains(self, other: Elve) -> bool:
        return self.lower <= other.lower and other.upper <= self.upper

    def overlap(self, other: Elve) -> bool:
        return self.lower <= other.lower <= self.upper or \
            self.lower <= other.upper <= self.upper

    def __repr__(self) -> str:
        return f"{self.lower}-{self.upper}"


def solve_part1(lines: list[str]) -> None:

    result: int = 0

    for line in lines:
        s1, s2 = line.split(",")

        e1 = Elve(s1)
        e2 = Elve(s2)

        if e1.contains(e2) or e2.contains(e1):
            result += 1

    print(f"Pairs fully contains: {result}")


def solve_part2(lines: list[str]) -> None:

    result: int = 0

    for line in lines:
        s1, s2 = line.split(",")

        e1 = Elve(s1)
        e2 = Elve(s2)

        if e1.overlap(e2) or e2.overlap(e1):          
            result += 1

    print(f"Pairs fully overlap: {result}")


def main() -> int:

    with open(Path(__file__).parent / "input.txt", encoding='utf-8') as f:
        lines = f.readlines()

    solve_part1(lines)
    solve_part2(lines)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
