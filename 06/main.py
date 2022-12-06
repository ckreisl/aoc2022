from pathlib import Path


MARKER_LENGTH_PART_1: int = 4
MARKER_LENGTH_PART_2: int = 14


def solve_part1(content: str, marker_length) -> None:

    lines = content.splitlines()
    marker = marker_length

    for line in lines:
        for i in range(0, len(line) - marker_length):
            seq = set(line[i:i + marker_length])

            if len(seq) == marker_length:
                break

            marker += 1
        
        print(f"Processed: {marker}")
        marker = marker_length
    

def solve_part2(content: str, marker_length) -> None:
    solve_part1(content, marker_length)


def main() -> int:

    with open(Path(__file__).parent / "input.txt", encoding='utf-8') as f:
        content = f.read()

    solve_part1(content, MARKER_LENGTH_PART_1)
    solve_part2(content, MARKER_LENGTH_PART_2)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
