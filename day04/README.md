# Day 4 – Advent of Code 2025
**Puzzle:** Printing Department

This folder contains my solutions for **Day 4** of Advent of Code 2025.

---

## Problem Summary

The input is a 2D grid where:
- `@` represents a roll of paper
- `.` represents empty space

Each roll of paper has **8 neighboring positions**
(up, down, left, right, and diagonals).

---

## Part 1

A roll of paper can be accessed by a forklift if **fewer than 4**
of its 8 neighboring positions also contain a roll of paper (`@`).

**Task:**  
Count how many rolls of paper are initially accessible.

---

## Part 2

Once a roll of paper is accessible, it can be removed.

After removal:
- Neighbor counts change
- New rolls may become accessible
- This process repeats until no more rolls can be removed

**Task:**  
Determine the **total number of rolls removed** after the process stabilizes.

---

## Structure

- `part1.py` – Initial accessibility count
- `part2.py` – Iterative removal simulation

---

## What I Learned

- 2D grid traversal with neighbor checks
- Handling diagonal adjacency
- Simulation with repeated state updates
- Careful boundary checking in grids
- Translating problem rules into precise logic

---

## Results

- **Part 1 Answer:** `1493`
- **Part 2 Answer:** `9194`

> Puzzle inputs are not included as they are unique per user.
