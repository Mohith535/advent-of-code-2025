"""
Advent of Code 2025
Day 7 - Part 1: Laboratories

Author: Mohith Kannan K
"""

def solve():
    # Load grid
    with open(r"E:\advent of code 2025 december\AOC\day 7 part 1 puzzle input.txt") as f:
        grid = [line.rstrip("\n") for line in f]

    rows = len(grid)
    cols = len(grid[0])

    # Find start column (S is always on row 0)
    start_col = None
    for c in range(cols):
        if grid[0][c] == "S":
            start_col = c
            break

    # Active beam columns at the current row
    beams = {start_col}
    split_count = 0

    # Move downward row by row
    for r in range(1, rows):
        next_beams = set()

        for c in beams:
            if grid[r][c] == "^":
                split_count += 1
                if c - 1 >= 0:
                    next_beams.add(c - 1)
                if c + 1 < cols:
                    next_beams.add(c + 1)
            else:
                next_beams.add(c)

        beams = next_beams

        if not beams:
            break

    print(split_count)


if __name__ == "__main__":
    solve()
