"""
Advent of Code 2025
Day 6 - Part 1: Trash Compactor

Author: Mohith Kannan K
Answer: 3968933219902
"""

def solve():
    with open(r"E:\advent of code 2025 december\AOC\day 6 part 1 puzzle input.txt") as f:
        lines = [line.rstrip("\n") for line in f]

    height = len(lines)
    width = max(len(line) for line in lines)

    grid = [line.ljust(width) for line in lines]

    total = 0
    c = 0

    while c < width:
        # skip empty separator columns
        if all(grid[r][c] == " " for r in range(height)):
            c += 1
            continue

        # find one problem block
        start = c
        while c < width and not all(grid[r][c] == " " for r in range(height)):
            c += 1
        end = c

        operator = grid[height - 1][start]
        numbers = []

        # READ ROW-WISE (THIS WAS THE BUG)
        for r in range(height - 1):
            digits = []
            for col in range(start, end):
                if grid[r][col].isdigit():
                    digits.append(grid[r][col])
            if digits:
                numbers.append(int("".join(digits)))

        if operator == "+":
            total += sum(numbers)
        else:
            prod = 1
            for n in numbers:
                prod *= n
            total += prod

    print(total)


if __name__ == "__main__":
    solve()
