"""
Advent of Code 2025
Day 4 - Part 2: Printing Department

Author: Mohith Kannan K
Answer: 9194
"""

from pathlib import Path

DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]


def count_neighbors(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for dr, dc in DIRECTIONS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == "@":
                count += 1
    return count


def solve():
    input_file = Path(r"E:\advent of code 2025 december\AOC\day 4 puzzle input.txt")
    grid = [list(row) for row in input_file.read_text().splitlines()]

    rows, cols = len(grid), len(grid[0])
    removed_total = 0

    while True:
        to_remove = []

        # Find all currently removable rolls
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "@":
                    if count_neighbors(grid, r, c) < 4:
                        to_remove.append((r, c))

        if not to_remove:
            break  # no more changes possible

        # Remove them all at once
        for r, c in to_remove:
            grid[r][c] = "."
            removed_total += 1

    print(removed_total)


if __name__ == "__main__":
    solve()
