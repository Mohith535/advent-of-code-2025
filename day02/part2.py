"""
Advent of Code 2025
Day 2 - Part 2: Gift Shop

Author: Mohith Kannan K
Answer: 50793864718

Rule:
An ID is invalid if it is made of a digit sequence
repeated at least twice.
"""

from pathlib import Path


def is_repeated_pattern(num: int) -> bool:
    """
    Returns True if the number consists of
    a smaller digit sequence repeated >= 2 times.
    """
    s = str(num)
    n = len(s)

    # Try all possible substring lengths
    for size in range(1, n // 2 + 1):
        if n % size == 0:
            pattern = s[:size]
            if pattern * (n // size) == s:
                return True

    return False


def solve():
    # Update path if needed
    input_file = Path(r"E:\advent of code 2025 december\AOC\day 2 puzzle input.txt")

    total_sum = 0

    # Input is a single long line of ranges
    ranges = input_file.read_text().strip().split(",")

    for r in ranges:
        start, end = map(int, r.split("-"))

        for num in range(start, end + 1):
            if is_repeated_pattern(num):
                total_sum += num

    print(total_sum)


if __name__ == "__main__":
    solve()
