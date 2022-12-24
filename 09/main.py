from __future__ import annotations

from pathlib import Path


class Point:
    x: int = 0
    y: int = 0

    def __init__(self, _x: int, _y: int) -> None:
        self.x = _x
        self.y = _y

    @property
    def pos(self) -> tuple:
        return (self.x, self.y)


class RopeBridge:

    def __init__(self) -> None:
        self.head = Point(0,0)
        self.tail = Point(0,0)

        # set() does not work here and delivers 6123?
        self.__visited = {self.tail.pos}

    def up(self) -> None:        
        self.head.y += 1
        self.__move_tail("up")

    def down(self) -> None:        
        self.head.y -= 1
        self.__move_tail("down")

    def left(self) -> None:
        self.head.x -= 1        
        self.__move_tail("left")

    def right(self) -> None:
        self.head.x += 1
        self.__move_tail("right")

    def visited(self) -> int:
        return len(self.__visited)

    def print(self) -> None:
        print(f"Head: {self.head.pos}")
        print(f"Tail: {self.tail.pos}")

    def __move_tail(self, direction: str) -> None:

        is_directional_movement = True if (self.head.x != self.tail.x) or (self.head.y != self.tail.y) else False

        if abs(self.head.x - self.tail.x) > 1 or abs(self.head.y - self.tail.y) > 1:
            match direction:
                case "up":
                    if is_directional_movement:
                        self.tail.x = self.head.x
                    self.tail.y += 1
                case "down":
                    if is_directional_movement:
                        self.tail.x = self.head.x
                    self.tail.y -= 1
                case "left":
                    if is_directional_movement:
                        self.tail.y = self.head.y
                    self.tail.x -= 1
                case "right":
                    if is_directional_movement:
                        self.tail.y = self.head.y
                    self.tail.x += 1

            self.__visited.add(self.tail.pos)


def solve_part1(lines: list[str]) -> None:

    rb = RopeBridge()

    for line in lines:
        direction, amount = line.split()
        # print(f"Direction: {direction}")
        # print(f"Amount: {amount}")
        match direction:
            case 'L':
                for _ in range(int(amount)):
                    rb.left()
            case 'R':
                for _ in range(int(amount)):
                    rb.right()
            case 'U':
                for _ in range(int(amount)):
                    rb.up()
            case 'D':
                for _ in range(int(amount)):
                    rb.down()
    
    print(f"Visited: {rb.visited()}")


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
