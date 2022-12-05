from pathlib import Path


# A, X Rock (1 pts)
# B, Y Paper (2 pts)
# C, Z Scissor (3 pts)

# (0pts lost, 3pts draw, 6pts win)


def main() -> int:

    with open(Path(__file__).parent / "input.txt", encoding='utf-8') as f:
        lines = f.readlines()

    score: int = 0    
    for line in lines:
        elve, my = line.split()

        # PART 1

        if elve == 'A' and my == 'X':
            score += (1 + 3)
        elif elve == 'B' and my == 'Y':
            score += (2 + 3)
        elif elve == 'C' and my == 'Z':
            score += (3 + 3)
        elif elve == 'A' and my == 'Y':
            score += (2 + 6)
        elif elve == 'A' and my == 'Z':
            score += (3 + 0)
        elif elve == 'B' and my == 'X':
            score += (1 + 0)
        elif elve == 'B' and my == 'Z':
            score += (3 + 6)
        elif elve == 'C' and my == 'X':
            score += (1 + 6)
        elif elve == 'C' and my == 'Y':
            score += (0 + 2)

    print(f"My score: {score}")

    # PART 2

    score = 0
    for line in lines:
        elve, my = line.split()

        if my == 'X': # X (lose)
            if elve == 'A':
                score += (0 + 3)
            elif elve == 'B':
                score += (0 + 1)
            elif elve == 'C':
                score += (0 + 2)
        elif my == 'Y': # Y (draw)
            if elve == 'A':
                score += (3 + 1)
            elif elve == 'B':
                score += (3 + 2)
            elif elve == 'C':
                score += (3 + 3)
        elif my == 'Z': # Z (win)
            if elve == 'A':
                score += (6 + 2)
            elif elve == 'B':
                score += (6 + 3)
            elif elve == 'C':
                score += (6 + 1)
            

    print(f"My score: {score}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
