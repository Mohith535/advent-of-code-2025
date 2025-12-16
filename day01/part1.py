"""
Advent of Code 2025
Day 1 - Part 1: Secret Entrance

Author: Mohith Kannan K
Answer: 1043
"""

from pathlib import Path


def solve():
    # Update this path if your input file is elsewhere
    input_file = Path(r"E:\advent of code 2025 december\AOC\day one puzzle input.txt")

    instructions = input_file.read_text().splitlines()

    position = 50  # Dial starts at 50
    zero_count = 0

    for instr in instructions:
        direction = instr[0]
        distance = int(instr[1:])

        if direction == "R":
            position = (position + distance) % 100
        elif direction == "L":
            position = (position - distance) % 100

        # Part 1: count only when rotation ENDS at 0
        if position == 0:
            zero_count += 1

    print(zero_count)


if __name__ == "__main__":
    solve()
