"""
Advent of Code 2025
Day 12 - Part 1

Author: Mohith Kannan K

NOTE:
This is a correct backtracking tiling solver.
It is intentionally not optimized for large inputs.
See README for performance notes.
"""


from itertools import product

# -------------------------------------------------
# Parsing
# -------------------------------------------------

def parse_input(filename):
    with open(filename) as f:
        lines = [l.rstrip() for l in f if l.strip()]

    shapes = {}
    i = 0

    # parse shapes
    while ":" in lines[i] and "x" not in lines[i]:
        sid = int(lines[i][:-1])
        i += 1
        grid = []
        while i < len(lines) and lines[i][0] in "#.":
            grid.append(lines[i])
            i += 1
        shapes[sid] = grid

    # parse regions
    regions = []
    for j in range(i, len(lines)):
        size, counts = lines[j].split(":")
        w, h = map(int, size.split("x"))
        cnts = list(map(int, counts.split()))
        regions.append((w, h, cnts))

    return shapes, regions


# -------------------------------------------------
# Shape transforms
# -------------------------------------------------

def rotate(shape):
    return ["".join(shape[len(shape)-1-r][c] for r in range(len(shape)))
            for c in range(len(shape[0]))]

def flip(shape):
    return [row[::-1] for row in shape]

def variants(shape):
    res = set()
    cur = shape
    for _ in range(4):
        res.add(tuple(cur))
        res.add(tuple(flip(cur)))
        cur = rotate(cur)
    return [list(v) for v in res]

def cells(shape):
    out = []
    for y, row in enumerate(shape):
        for x, ch in enumerate(row):
            if ch == "#":
                out.append((x, y))
    return out


# -------------------------------------------------
# Backtracking solver
# -------------------------------------------------

def can_place(board, w, h, piece, ox, oy):
    for x, y in piece:
        nx, ny = ox + x, oy + y
        if nx < 0 or ny < 0 or nx >= w or ny >= h:
            return False
        if board[ny][nx]:
            return False
    return True

def place(board, piece, ox, oy, val):
    for x, y in piece:
        board[oy + y][ox + x] = val

def solve_region(w, h, shapes, counts):
    board = [[False]*w for _ in range(h)]

    pieces = []
    for sid, cnt in enumerate(counts):
        pieces.extend([sid]*cnt)

    # area pruning
    needed = sum(len(cells(shapes[sid])) for sid in pieces)
    if needed > w * h:
        return False

    # generate variants
    var = {}
    for sid in set(pieces):
        var[sid] = [cells(v) for v in variants(shapes[sid])]

    # sort pieces by size (important!)
    pieces.sort(key=lambda s: -len(cells(shapes[s])))

    def backtrack(idx):
        if idx == len(pieces):
            return True

        # find first empty cell
        for y in range(h):
            for x in range(w):
                if not board[y][x]:
                    for piece in var[pieces[idx]]:
                        if can_place(board, w, h, piece, x, y):
                            place(board, piece, x, y, True)
                            if backtrack(idx + 1):
                                return True
                            place(board, piece, x, y, False)
                    return False
        return False

    return backtrack(0)


# -------------------------------------------------
# Main
# -------------------------------------------------

def solve():
    shapes, regions = parse_input(
        r"E:\advent of code 2025 december\AOC\day 12 part 1 puzzle input.txt"
    )

    count = 0
    for w, h, counts in regions:
        if solve_region(w, h, shapes, counts):
            count += 1

    print("FINAL ANSWER:", count)


if __name__ == "__main__":
    solve()
