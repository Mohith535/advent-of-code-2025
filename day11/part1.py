"""
Advent of Code 2025
Day 11 - Part 1

Author: Mohith Kannan K
"""

from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

def parse_input(filename):
    graph = defaultdict(list)
    with open(filename) as f:
        for line in f:
            src, rest = line.strip().split(":")
            graph[src].extend(rest.strip().split())
    return graph

def count_paths(graph):
    memo = {}

    def dfs(node):
        if node == "out":
            return 1
        if node in memo:
            return memo[node]

        total = 0
        for nxt in graph[node]:
            total += dfs(nxt)

        memo[node] = total
        return total

    return dfs("you")

if __name__ == "__main__":
    filename = "day 11 part 1.txt"
    graph = parse_input(filename)
    print("FINAL ANSWER:", count_paths(graph))
