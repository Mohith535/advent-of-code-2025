"""
Advent of Code 2025
Day 11 - Part 2

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

def count_valid_paths(graph):
    memo = {}

    def dfs(node, seen_dac, seen_fft):
        if node == "dac":
            seen_dac = True
        if node == "fft":
            seen_fft = True

        if node == "out":
            return 1 if seen_dac and seen_fft else 0

        key = (node, seen_dac, seen_fft)
        if key in memo:
            return memo[key]

        total = 0
        for nxt in graph[node]:
            total += dfs(nxt, seen_dac, seen_fft)

        memo[key] = total
        return total

    return dfs("svr", False, False)

if __name__ == "__main__":
    filename = "day 11 part 2 .txt"
    graph = parse_input(filename)
    print("FINAL ANSWER:", count_valid_paths(graph))
