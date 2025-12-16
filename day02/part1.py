"""
Advent of Code 2025
Day 2 - Part 1: Gift Shop

Author: Mohith Kannan K
Answer: 40214376723
"""

from pathlib import Path


def is_repeated_twice(n: int) -> bool:
    """
    Returns True if the number consists of a digit sequence
    repeated exactly twice (e.g., 11, 1212, 123123).
    """
    s = str(n)
    length = len(s)

    # Length must be even to split into two equal parts
    if length % 2 != 0:
        return False

    half = length // 2
    return s[:half] == s[half:]


def solve():
    input_file = Path(r"E:\advent of code 2025 december\AOC\day 2 puzzle input.txt")
    total = 0

    ranges = input_file.read_text().strip().split(",")

    for r in ranges:
        start, end = map(int, r.split("-"))

        for num in range(start, end + 1):
            if is_repeated_twice(num):
                total += num

    print(total)


if __name__ == "__main__":
    solve()
