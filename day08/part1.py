"""
Advent of Code 2025
Day 8 - Part 1

Author: Mohith Kannan K
"""

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True


def solve():
    points = []
    with open("day 8 part 1 puzzle input.txt") as f:
        for line in f:
            x, y, z = map(int, line.strip().split(","))
            points.append((x, y, z))

    n = len(points)
    edges = []

    # Build all pair distances (no sqrt needed)
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dist = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
            edges.append((dist, i, j))

    edges.sort()
    dsu = DSU(n)

    #  IMPORTANT: attempt EXACTLY 1000 edges, not unions
    for i in range(1000):
        _, a, b = edges[i]
        dsu.union(a, b)

    # Count final circuit sizes
    component_sizes = {}
    for i in range(n):
        root = dsu.find(i)
        component_sizes[root] = component_sizes.get(root, 0) + 1

    sizes = sorted(component_sizes.values(), reverse=True)
    print(sizes[0] * sizes[1] * sizes[2])


if __name__ == "__main__":
    solve()
