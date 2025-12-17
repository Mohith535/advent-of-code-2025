"""
Advent of Code 2025
Day 8 - Part 2

Author: Mohith Kannan K
"""

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        self.parent[rb] = ra
        self.count -= 1
        return True


def solve():
    points = []
    with open("day 8 part 2 puzzle input .txt") as f:
        for line in f:
            x, y, z = map(int, line.strip().split(","))
            points.append((x, y, z))

    n = len(points)
    edges = []

    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dist = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
            edges.append((dist, i, j))

    edges.sort()
    dsu = DSU(n)

    for _, a, b in edges:
        if dsu.union(a, b):
            if dsu.count == 1:
                x1 = points[a][0]
                x2 = points[b][0]
                print(x1 * x2)
                return


if __name__ == "__main__":
    solve()
