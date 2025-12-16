"""
Advent of Code 2025
Day 6 - Part 2: Trash Compactor

Author: Mohith Kannan K
Answer: 6019576291014
"""

from pathlib import Path


def solve():
    lines = Path(
        r"E:\advent of code 2025 december\AOC\day 6 part 2 puzzle input.txt"
    ).read_text().splitlines()

    height = len(lines)
    width = max(len(line) for line in lines)

    grid = [line.ljust(width) for line in lines]

    total = 0
    col = width - 1

    while col >= 0:
        if all(grid[row][col] == " " for row in range(height)):
            col -= 1
            continue

        end = col
        while col >= 0 and not all(grid[row][col] == " " for row in range(height)):
            col -= 1
        start = col + 1

        numbers = []
        operator = None

        for c in range(end, start - 1, -1):
            digits = []
            for r in range(height):
                ch = grid[r][c]
                if ch in "+*":
                    operator = ch
                    break
                if ch.isdigit():
                    digits.append(ch)
            if digits:
                numbers.append(int("".join(digits)))

        if operator == "+":
            value = sum(numbers)
        else:
            value = 1
            for n in numbers:
                value *= n

        total += value

    print(total)


if __name__ == "__main__":
    solve()
