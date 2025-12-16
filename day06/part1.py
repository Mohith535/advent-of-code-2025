"""
Advent of Code 2025
Day 6 - Part 1

Author: Mohith Kannan K
"""

def solve():
    with open("day6_input.txt", "r") as f:
        lines = [line.rstrip("\n") for line in f]

    height = len(lines)
    width = max(len(line) for line in lines)

    # Pad all lines to equal width
    grid = [line.ljust(width) for line in lines]

    total = 0
    col = 0

    while col < width:
        # Skip empty separator columns
        if all(grid[row][col] == " " for row in range(height)):
            col += 1
            continue

        numbers = []
        operator = None

        for row in range(height):
            char = grid[row][col]
            if char in "+*":
                operator = char
                break
            if char.isdigit():
                numbers.append(int(char))

        if operator == "+":
            value = sum(numbers)
        else:
            value = 1
            for n in numbers:
                value *= n

        total += value
        col += 1

    print(total)


if __name__ == "__main__":
    solve()
