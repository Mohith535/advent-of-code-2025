"""
Advent of Code 2025
Day 5 - Part 2: Cafeteria

Author: Mohith Kannan K

Counts how many unique ingredient IDs are considered fresh
based only on the fresh ID ranges.
"""

def parse_ranges(file_path):
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    ranges = []
    for line in lines:
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    return ranges


def merge_ranges(ranges):
    """
    Merges overlapping or adjacent ranges.
    """
    ranges.sort()
    merged = [ranges[0]]

    for current_start, current_end in ranges[1:]:
        last_start, last_end = merged[-1]

        if current_start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            merged.append((current_start, current_end))

    return merged


def solve():
    ranges = parse_ranges("day 5 part 2 puzzle input.txt")
    merged_ranges = merge_ranges(ranges)

    total_fresh_ids = 0
    for start, end in merged_ranges:
        total_fresh_ids += (end - start + 1)

    print(total_fresh_ids)


if __name__ == "__main__":
    solve()
