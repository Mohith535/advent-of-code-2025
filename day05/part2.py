"""
Advent of Code 2025
Day 5 - Part 2: Cafeteria

Author: Mohith Kannan K

Counts how many unique ingredient IDs are considered fresh
based only on the fresh ID ranges.
"""

def parse_ranges(file_path):
    ranges = []

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if "-" not in line:
                continue

            start, end = map(int, line.split("-"))
            ranges.append((start, end))

    return ranges


def merge_ranges(ranges):
    ranges.sort()
    merged = [ranges[0]]

    for curr_start, curr_end in ranges[1:]:
        last_start, last_end = merged[-1]

        if curr_start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, curr_end))
        else:
            merged.append((curr_start, curr_end))

    return merged


def solve():
    ranges = parse_ranges(
        r"E:\advent of code 2025 december\AOC\day 5 part 2 puzzle input.txt"
    )

    merged = merge_ranges(ranges)

    total = 0
    for start, end in merged:
        total += (end - start + 1)

    print(total)


if __name__ == "__main__":
    solve()
