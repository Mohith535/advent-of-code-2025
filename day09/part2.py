"""
Advent of Code 2025
Day 9 - Part 2

Author: Mohith Kannan K
"""

from itertools import combinations

def parse_input(filename):
    pos = []
    with open(filename) as f:
        for line in f:
            if line.strip():
                x, y = map(int, line.strip().split(","))
                pos.append((x, y))
    return pos


def point_is_inside(px, py, pos):
    n = len(pos)
    cross = 0
    j = n - 1

    for i in range(n):
        xi, yi = pos[i]
        xj, yj = pos[j]

        # Point on edge
        if min(xi, xj) <= px <= max(xi, xj) and min(yi, yj) <= py <= max(yi, yj):
            return True

        # Ray casting (vertical edges)
        if xi == xj and min(yi, yj) <= py < max(yi, yj) and xi > px:
            cross += 1

        j = i

    return cross % 2 == 1


def edge_is_intersect(side, edge):
    (a, b) = side
    (c, d) = edge

    # Parallel edges can't intersect
    if (a[0] == b[0] and c[0] == d[0]) or (a[1] == b[1] and c[1] == d[1]):
        return False

    if a[0] == b[0]:  # vertical side
        return (
            min(c[0], d[0]) < a[0] < max(c[0], d[0]) and
            min(a[1], b[1]) < c[1] < max(a[1], b[1])
        )
    else:  # horizontal side
        return (
            min(c[1], d[1]) < a[1] < max(c[1], d[1]) and
            min(a[0], b[0]) < c[0] < max(a[0], b[0])
        )


def is_inside_shape(a, b, pos, edges):
    x1, y1 = a
    x2, y2 = b

    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    # Check all four rectangle corners
    for px in (min_x, max_x):
        for py in (min_y, max_y):
            if not point_is_inside(px, py, pos):
                return False

    # Rectangle edges
    sides = [
        ((min_x, min_y), (min_x, max_y)),
        ((min_x, max_y), (max_x, max_y)),
        ((max_x, max_y), (max_x, min_y)),
        ((max_x, min_y), (min_x, min_y)),
    ]

    # Ensure rectangle edges don't cross polygon edges
    for side in sides:
        for edge in edges:
            if edge_is_intersect(side, edge):
                return False

    return True


def solve(filename):
    pos = parse_input(filename)
    edges = [(pos[i], pos[(i + 1) % len(pos)]) for i in range(len(pos))]

    rects = []
    for a, b in combinations(pos, 2):
        w = abs(a[0] - b[0]) + 1
        h = abs(a[1] - b[1]) + 1
        rects.append((w * h, a, b))

    rects.sort(reverse=True)

    for area, a, b in rects:
        if is_inside_shape(a, b, pos, edges):
            return area


if __name__ == "__main__":
    filename = r"E:\advent of code 2025 december\AOC\day 9 part 2 puzzle input .txt"
    print("FINAL ANSWER:", solve(filename))

