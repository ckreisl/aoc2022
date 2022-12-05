from pathlib import Path


# https://www.asciitable.com/


def is_lower_case(value: str) -> bool:
    return value == value.lower()


def priority(value: str) -> int:

    ascii_value = ord(value)

    if is_lower_case(value):
        return ascii_value - 96

    return ascii_value - 38


def solve_part1(lines: list[str]) -> None:

    result: int = 0

    for line in lines:
        s1 = line[:len(line)//2]
        s2 = line[len(line)//2:]

        for c in s1:
            if c in s2:
                # print(c)
                result += priority(c)
                break

    print(f"The piority sum is: {result}")


def solve_part2(lines: list[str]) -> None:

    result: int = 0

    for i in range(0, len(lines), 3):
        rucksack_one = lines[i].replace('\n', '')
        rucksack_two = lines[i+1].replace('\n', '')
        rucksack_three = lines[i+2].replace('\n', '')

        xs = sorted([rucksack_one, rucksack_two, rucksack_three], key=lambda x: len(x), reverse=True)
        
        for item in xs[0]:
            if not item in xs[1]:
                continue
            if not item in xs[2]:
                continue
            # print(item)
            result += priority(item)
            break
        
    print(f"The piority sum is: {result}")


def main() -> int:

    with open(Path(__file__).parent / "input.txt", encoding='utf-8') as f:
        lines = f.readlines()

    solve_part1(lines)
    solve_part2(lines)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())