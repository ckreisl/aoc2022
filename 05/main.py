from pathlib import Path


class Stack:

    def __init__(self) -> None:
        self.__xs = []

    def empty(self) -> bool:
        return len(self.__xs) == 0

    def peek(self) -> str:
        return self.__xs[-1]

    def push(self, value: str) -> None:
        self.__xs.append(value)

    def pop(self) -> str:
        return self.__xs.pop()

    def reverse(self) -> None:
        self.__xs.reverse()

    def print(self):
        for item in self.__xs[::-1]:
            print(f"[{item}]")


def read_stacks(stacks: str) -> list[Stack]:    
    rows = stacks.splitlines()[:-1]
    columns = int((len(stacks.splitlines()[-1]) + 1) / 4)

    xs: list[Stack] = [Stack() for i in range(0, columns)]

    for row in rows:
        index = 0
        for i in range(0, columns):
            item: str = row[index:index+3]
            index += 4

            if item.isspace():
                continue
            
            xs[i].push(item)

    for s in xs:
        s.reverse()

    return xs


def do_move_crane9000(stacks: list[Stack], command: str):
    cmd = command.split()
    how_many = int(cmd[1])
    from_stack = int(cmd[3])
    to_stack = int(cmd[5])

    stack = stacks[from_stack - 1]    
    for _ in range(0, how_many):
        stacks[to_stack - 1].push(stack.pop())


def do_move_crane9001(stacks: list[Stack], command: str):
    cmd = command.split()
    how_many = int(cmd[1])
    from_stack = int(cmd[3])
    to_stack = int(cmd[5])

    stack = stacks[from_stack - 1]

    if how_many == 1:
        stacks[to_stack - 1].push(stack.pop())
    else:
        xs = []
        for _ in range(0, how_many):
            xs.append(stack.pop())

        xs.reverse()
        for item in xs:
            stacks[to_stack - 1].push(item)


def solve_part1(content: str) -> None:
    input_stacks, input_moves = content.split("\n\n")    

    stacks = read_stacks(input_stacks)

    for move in input_moves.splitlines():
        do_move_crane9000(stacks, move)

    result: str = ""

    for stack in stacks:
        result += stack.peek()[1]

    print(f"Result: {result}")


def solve_part2(content: str) -> None:
    input_stacks, input_moves = content.split("\n\n")    

    stacks = read_stacks(input_stacks)

    for move in input_moves.splitlines():
        do_move_crane9001(stacks, move)

    result: str = ""

    for stack in stacks:
        result += stack.peek()[1]

    print(f"Result: {result}")


def main() -> int:

    with open(Path(__file__).parent / "input.txt", encoding='utf-8') as f:
        content = f.read()

    solve_part1(content)
    solve_part2(content)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())