"""
Advent of Code 2025
Day 12 - Part 1

Author: Mohith Kannan K
"""

from itertools import combinations

def solve():
    points = []

    # Read puzzle input
    with open("day 9 part 1 puzzle input.txt") as f:
        for line in f:
            if line.strip():
                x, y = map(int, line.strip().split(","))
                points.append((x, y))

    max_area = 0

    # Check all pairs of red tiles
    for (x1, y1), (x2, y2) in combinations(points, 2):
        width = abs(x1 - x2) + 1
        height = abs(y1 - y2) + 1
        area = width * height
        max_area = max(max_area, area)

    print(max_area)


if __name__ == "__main__":
    solve()
