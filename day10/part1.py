"""
Advent of Code 2025
Day 10 - Part 1

Author: Mohith Kannan K
"""

import re
from itertools import product


def parse_line(line):
    # indicator lights
    lights = line[line.index("[")+1 : line.index("]")]
    n = len(lights)
    target = [1 if c == "#" else 0 for c in lights]

    # button definitions
    buttons = [
        tuple(map(int, b.split(",")))
        for b in re.findall(r"\((.*?)\)", line)
    ]

    return n, buttons, target


def min_presses(n, buttons, target):
    m = len(buttons)

    # build toggle matrix (buttons → lights)
    A = [[0]*m for _ in range(n)]
    for j, btn in enumerate(buttons):
        for i in btn:
            A[i][j] ^= 1

    best = float("inf")

    # brute-force free variables (system size is small enough)
    for mask in product([0, 1], repeat=m):
        state = [0]*n

        for j in range(m):
            if mask[j]:
                for i in buttons[j]:
                    state[i] ^= 1

        if state == target:
            best = min(best, sum(mask))

    return best


def solve(filename):
    total = 0
    with open(filename) as f:
        for line in f:
            if line.strip():
                n, buttons, target = parse_line(line)
                total += min_presses(n, buttons, target)

    print(total)


if __name__ == "__main__":
    solve("day 10 part 1 puzzle input.txt")
