"""
Advent of Code 2025
Day 10 - Part 2

Author: Mohith Kannan K
"""

import re
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpInteger, PULP_CBC_CMD

def parse_input(filename):
    machines = []
    with open(filename, "r") as f:
        for line in f:
            if not line.strip():
                continue

            buttons = [
                tuple(map(int, x.split(",")))
                for x in re.findall(r"\((.*?)\)", line)
            ]

            targets = list(
                map(int, re.search(r"\{(.*?)\}", line).group(1).split(","))
            )

            machines.append((buttons, targets))
    return machines


def solve_machine(buttons, targets):
    prob = LpProblem("Machine", LpMinimize)

    # decision variables
    x = [
        LpVariable(f"x_{j}", lowBound=0, cat=LpInteger)
        for j in range(len(buttons))
    ]

    # minimize total presses
    prob += lpSum(x)

    # exact joltage constraints
    for i in range(len(targets)):
        prob += lpSum(
            x[j] for j in range(len(buttons)) if i in buttons[j]
        ) == targets[i]

    prob.solve(PULP_CBC_CMD(msg=False))

    return int(sum(v.value() for v in x))


def solve_all(filename):
    machines = parse_input(filename)
    total = 0

    for idx, (buttons, targets) in enumerate(machines, start=1):
        presses = solve_machine(buttons, targets)
        total += presses
        print(f"Machine {idx}: {presses}")

    return total


if __name__ == "__main__":
    filename = "day 10 part 2 puzzle input again.txt"

    answer = solve_all(filename)
    print("\nFINAL ANSWER:", answer)
