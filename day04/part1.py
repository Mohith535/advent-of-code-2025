"""
Advent of Code 2025
Day 4 - Part 1: Printing Department

Author: Mohith Kannan K
Answer: 1493
"""

from pathlib import Path

# 8 possible directions (including diagonals)
DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]


def solve():
    input_file = Path(r"E:\advent of code 2025 december\AOC\day 4 puzzle input.txt")
    grid = input_file.read_text().splitlines()

    rows = len(grid)
    cols = len(grid[0])

    accessible = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue

            neighbor_count = 0

            # Count adjacent @
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == "@":
                        neighbor_count += 1

            if neighbor_count < 4:
                accessible += 1

    print(accessible)


if __name__ == "__main__":
    solve()
