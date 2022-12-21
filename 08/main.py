from __future__ import annotations

from pathlib import Path


class Grid:

    def __init__(self, lines: list[str]) -> None:

        self.grid = []

        for value in lines:
            xs = []
            for c in value:
                if c != '\n':
                    xs.append(int(c))
            self.grid.append(xs)

    def is_visible(self, x: int, y: int) -> bool:
        return self.is_visible_horizontal(x, y) or \
            self.is_visible_vertical(x, y)

    def is_visible_horizontal(self, x: int, y: int) -> bool:
        return self.is_visible_from_left_side(x, y) or \
            self.is_visible_from_right_side(x, y)

    def is_visible_vertical(self, x: int, y: int) -> bool:
        return self.is_visible_from_top(x, y) or \
            self.is_visible_from_bottom(x, y)

    def is_visible_from_left_side(self, x: int, y: int) -> bool:
        height = self.grid[y][x]

        for i in range(0, x):
            if self.grid[y][i] >= height:
                return False

        return True

    def is_visible_from_right_side(self, x: int, y: int) -> bool:
        height = self.grid[y][x]

        for i in range(x+1, len(self.grid[y])):
            if self.grid[y][i] >= height:
                return False

        return True

    def is_visible_from_top(self, x: int, y: int) -> bool:
        height = self.grid[y][x]

        for i in range(0, y):
            if self.grid[i][x] >= height:
                return False

        return True


    def is_visible_from_bottom(self, x: int, y: int) -> bool:
        height = self.grid[y][x]

        for i in range(y+1, len(self.grid[x])):
            if self.grid[i][x] >= height:
                return False

        return True

    def visible_interior(self) -> int:
        visible = 0

        for y in range(1, len(self.grid) - 1):
            for x in range(1, len(self.grid[0]) - 1):
                if self.is_visible(x, y):
                    visible += 1

        return visible

    def visible_outside(self) -> int:
        top_bottom = len(self.grid) * 2
        right_left = (len(self.grid) - 2) * 2
        return top_bottom + right_left

    def visible_amount(self) -> int:
        return self.visible_interior() + \
             self.visible_outside()

    def highest_scenic_score(self) -> int:

        score = -1
        for y in range(1, len(self.grid)):
            for x in range(1, len(self.grid[y])):
                score = max(score, self.scenic_score(x, y))
        
        return score

    def scenic_score(self, x: int, y: int) -> int:
        return self.scenic_score_left(x, y) * self.scenic_score_right(x, y) * \
                self.scenic_score_top(x, y) * self.scenic_score_bottom(x, y)

    def scenic_score_left(self, x: int, y: int) -> int:
        height = self.grid[y][x]
        # print(f"Hight: {height}, Pos: ({x},{y})")

        score = 0
        for i in range(0, x):
            pos = (x-1) - i       
            if self.grid[y][pos] < height:
                score += 1
            else:
                score += 1
                break

        return score

    def scenic_score_right(self, x: int, y: int) -> int:
        height = self.grid[y][x]
        # print(f"Hight: {height}, Pos: ({x},{y})")

        score = 0
        for i in range(x+1, len(self.grid[y])):      
            if self.grid[y][i] < height:
                score += 1
            else:
                score += 1
                break                

        return score

    def scenic_score_top(self, x: int, y: int) -> int:
        height = self.grid[y][x]
        # print(f"Hight: {height}, Pos: ({x},{y})")

        score = 0
        for i in range(0, y):
            pos = (y-1) - i
            if self.grid[pos][x] < height:
                score += 1
            else:
                score += 1
                break                

        return score

    def scenic_score_bottom(self, x: int, y: int) -> int:
        
        height = self.grid[y][x]
        # print(f"Hight: {height}, Pos: ({x},{y})")

        score = 0
        for i in range(y+1, len(self.grid[y])):      
            if self.grid[i][x] < height:
                score += 1
            else:
                score += 1
                break

        return score    


def solve_part1(lines: list[str]) -> None:
    grid = Grid(lines)
    print(f"Visible Outside: {grid.visible_outside()}")
    print(f"Visible Interior: {grid.visible_interior()}")
    print(f"Total: {grid.visible_amount()}")


def solve_part2(lines: list[str]) -> None:
    grid = Grid(lines)
    print(f"Highest senic score: {grid.highest_scenic_score()}")


def main() -> int:

    with open(Path(__file__).parent / "input.txt", encoding='utf-8') as f:
        lines = f.readlines()

    solve_part1(lines)
    solve_part2(lines)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
