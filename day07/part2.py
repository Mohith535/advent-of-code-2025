"""
Advent of Code 2025
Day 7 - Part 2: Laboratories (Quantum Manifold)

Author: Mohith Kannan K
"""

def solve():
    with open(r"E:\advent of code 2025 december\AOC\day 7 part 2 ppuzle input.txt") as f:
        grid = [list(line.rstrip("\n")) for line in f]

    rows, cols = len(grid), len(grid[0])

    # Find start column
    for c in range(cols):
        if grid[0][c] == "S":
            start_col = c

    # dp[c] = number of timelines reaching column c
    dp = {start_col: 1}

    for r in range(1, rows):
        new_dp = {}

        for c, count in dp.items():
            if grid[r][c] == "^":
                # Split timelines
                if c - 1 >= 0:
                    new_dp[c - 1] = new_dp.get(c - 1, 0) + count
                if c + 1 < cols:
                    new_dp[c + 1] = new_dp.get(c + 1, 0) + count
            else:
                new_dp[c] = new_dp.get(c, 0) + count

        dp = new_dp

    print(sum(dp.values()))


if __name__ == "__main__":
    solve()
