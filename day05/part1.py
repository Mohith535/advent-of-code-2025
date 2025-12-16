"""
Advent of Code 2025
Day 5 - Part 1: Cafeteria

Author: Mohith Kannan K

Counts how many available ingredient IDs are fresh
based on the given fresh ID ranges.
"""

def parse_input(file_path):
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f]

    blank_index = lines.index("")
    range_lines = lines[:blank_index]
    id_lines = lines[blank_index + 1:]

    ranges = []
    for r in range_lines:
        start, end = map(int, r.split("-"))
        ranges.append((start, end))

    ids = list(map(int, id_lines))
    return ranges, ids


def is_fresh(ingredient_id, ranges):
    """
    Checks whether a single ingredient ID
    falls within any fresh range.
    """
    for start, end in ranges:
        if start <= ingredient_id <= end:
            return True
    return False


def solve():
    ranges, ids = parse_input("day 5 part 1 puzzle input.txt")

    fresh_count = 0
    for ingredient_id in ids:
        if is_fresh(ingredient_id, ranges):
            fresh_count += 1

    print(fresh_count)


if __name__ == "__main__":
    solve()
