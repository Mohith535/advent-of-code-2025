"""
Advent of Code 2025
Day 3 - Part 1: Lobby

Author: Mohith Kannan K
Answer: 17301

"""

from pathlib import Path


def max_two_digit_joltage(line: str) -> int:
    """
    Given a string of digits, find the maximum possible
    2-digit number that can be formed by choosing
    two digits in order.
    """
    digits = list(line.strip())
    best = 0

    # Try all valid ordered pairs (i < j)
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            value = int(digits[i] + digits[j])
            best = max(best, value)

    return best


def solve():
    # Update this path if your input file is elsewhere
    input_file = Path(r"E:\advent of code 2025 december\AOC\day 3 part 1 puzzle input.txt")

    total_joltage = 0

    # Read input safely
    for line in input_file.read_text().splitlines():
        if line.strip():  # skip empty lines
            total_joltage += max_two_digit_joltage(line)

    print(total_joltage)


if __name__ == "__main__":
    solve()
