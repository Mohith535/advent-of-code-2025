"""
Advent of Code 2025
Day 1 - Part 2: Secret Entrance

Author: Mohith Kannan K
Answer: 5963

Counts the number of times the dial points at 0,
including during rotations.
"""

from pathlib import Path


def solve():
    # Update path if your input file is elsewhere
    input_file = Path(r"E:\advent of code 2025 december\AOC\day one puzzle input.txt")
    instructions = input_file.read_text().splitlines()

    position = 50  # Dial starts at 50
    zero_count = 0

    for instr in instructions:
        direction = instr[0]
        distance = int(instr[1:])

        step = -1 if direction == "L" else 1

        for _ in range(distance):
            position = (position + step) % 100
            if position == 0:
                zero_count += 1

    print(zero_count)


if __name__ == "__main__":
    solve()
