from __future__ import annotations

from pathlib import Path
from dataclasses import dataclass


@dataclass
class Elve:
    index: int = -1
    carries: int = 0

    def max(self, other: Elve) -> Elve:
        if self.carries > other.carries:
            return self
        return other

    def to_string(self) -> str:
        return f"Elve: {self.index} \n" \
               f"Carries: {self.carries}"


def main() -> int:

    result = Elve()
    
    with open(Path(__file__).parent / 'input.txt', encoding='utf-8') as f:
        lines = f.readlines()
        
    index = 1
    carries = 0

    elves: list[Elve] = []

    # PART 1

    for line in lines:
        if line != '\n':
            carries += int(line)
            continue
            
        elve = Elve(index, carries)
        elves.append(elve)
        result = result.max(elve)
        index += 1
        carries = 0

    elve = Elve(index, carries)
    elves.append(elve)
    result = result.max(elve)

    print(result.to_string())

    # PART 2

    elves = sorted(elves, key=lambda elve: elve.carries, reverse=True)

    # print(elves)

    best_three_result: int = 0
    for e in elves[:3]:
        best_three_result += e.carries

    print(f"Best three max: {best_three_result}")

    return 0


if __name__ == '__main__':
    raise SystemExit(main())