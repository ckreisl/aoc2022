from __future__ import annotations

from pathlib import Path


class Point:
    x: int = 0
    y: int = 0

    @property
    def tpl(self) -> tuple:
        return (self.x, self.y)

    def update(self, tpl: tuple) -> None:
        self.x = tpl[0]
        self.y = tpl[1]


class RopeBridge:

    def __init__(self) -> None:
        self.head = Point()
        self.tail = Point()

        self.__visited = set(self.tail.tpl)
        self.__last_pos_head = self.head.tpl

    def up(self) -> None:
        self.__last_pos_head = self.head.tpl        
        self.head.y += 1
        self.__move_tail()

    def down(self) -> None:
        self.__last_pos_head = self.head.tpl        
        self.head.y -= 1
        self.__move_tail()

    def left(self) -> None:
        self.__last_pos_head = self.head.tpl
        self.head.x -= 1        
        self.__move_tail()

    def right(self) -> None:
        self.__last_pos_head = self.head.tpl
        self.head.x += 1
        self.__move_tail()

    def visited(self) -> int:
        return len(self.__visited)

    def print(self) -> None:
        print(f"Head: {self.head.tpl}")
        print(f"Tail: {self.tail.tpl}")

    def __move_tail(self):
        if abs(self.head.x - self.tail.x) > 1 or abs(self.head.y - self.tail.y) > 1:
            self.tail.update(self.__last_pos_head)
            self.__visited.add(self.tail.tpl)


def solve_part1(lines: list[str]) -> None:

    rb = RopeBridge()

    for line in lines:
        direction, amount = line.split()
        # print(f"Direction: {direction}")
        # print(f"Amount: {amount}")
        match direction:
            case 'L':
                for _ in range(0, int(amount)):
                    rb.left()
                    rb.print()
            case 'R':
                for _ in range(0, int(amount)):
                    rb.right()
                    rb.print()
            case 'U':
                for _ in range(0, int(amount)):
                    rb.up()
                    rb.print()
            case 'D':
                for _ in range(0, int(amount)):
                    rb.down()
                    rb.print()
        print("")
        # rb.print()
    
    print(f"Visited: {rb.visited()}")


def solve_part2(lines: list[str]) -> None:
    pass


def main() -> int:

    with open(Path(__file__).parent / "test.txt", encoding='utf-8') as f:
        lines = f.readlines()

    solve_part1(lines)
    solve_part2(lines)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
