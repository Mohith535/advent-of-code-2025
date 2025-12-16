"""
Advent of Code 2025
Day 3 - Part 2: Lobby

Author: Mohith Kannan K
Answer: 172162399742349

Problem Summary:
Each line represents a bank of batteries (digits 1–9).
You must turn on exactly TWELVE batteries (keeping order).
The joltage is the 12-digit number formed by those batteries.
Goal: Maximize the joltage per line and sum across all lines.

Key Idea:
This is a greedy "maximum subsequence of fixed length" problem.
"""

from pathlib import Path


def max_k_digit_joltage(line: str, k: int) -> int:
    """
    Given a string of digits, return the maximum possible
    k-digit number formed by selecting digits in order.

    Uses a greedy stack-based approach.
    """
    digits = list(line.strip())
    stack = []

    # Number of digits we are allowed to remove
    to_remove = len(digits) - k

    for d in digits:
        # Remove smaller digits if we can still remove more
        # and replacing them increases the final number
        while stack and to_remove > 0 and stack[-1] < d:
            stack.pop()
            to_remove -= 1
        stack.append(d)

    # Keep only the first k digits
    return int("".join(stack[:k]))


def solve():
    # Update path if your input file is elsewhere
    input_file = Path(r"E:\advent of code 2025 december\AOC\day 3 part 1 puzzle input.txt")

    total_joltage = 0

    # Read each battery bank
    for line in input_file.read_text().splitlines():
        if line.strip():  # skip empty lines
            total_joltage += max_k_digit_joltage(line, 12)

    print(total_joltage)


if __name__ == "__main__":
    solve()
