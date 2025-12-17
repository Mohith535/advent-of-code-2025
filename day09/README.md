# Day 9 – Advent of Code 2025
**Puzzle:** Movie Theater

This folder contains my solutions for **Day 9** of Advent of Code 2025.

---

## Problem Summary

The puzzle provides the **coordinates of red tiles** placed on a large 2D grid.

Using these red tiles, the task is to form the **largest possible axis-aligned rectangle**
where **two opposite corners are red tiles**.

The rectangle must align to the grid, and its area is measured in grid units.

---

## Part 1

- Any two red tiles may be chosen as opposite corners
- Rectangle sides must be parallel to the grid
- Tiles inside the rectangle may be anything
- Rectangle area is calculated using **inclusive grid coordinates**

The goal is to find the **maximum possible rectangle area**.

---

## Part 2

Additional constraints are introduced:

- Each red tile is connected to the next by **green tiles**, forming a closed loop
- All tiles **inside the loop** are also green
- Remaining tiles are neither red nor green

The rectangle:
- Must still use **red tiles as opposite corners**
- Must be **fully contained** within the red + green region
- Must **not cross or exit** the polygon boundary

This turns the problem into a **computational geometry challenge**.

---

## Structure

- `part1.py` – Solution for Part 1
- `part2.py` – Solution for Part 2

---

## What I Learned

- Brute-force rectangle enumeration using combinations
- Point-in-polygon testing (ray casting method)
- Detecting rectangle–polygon edge intersections
- Why geometric constraints dramatically increase complexity
- Optimizing by checking rectangles in descending area order

---

## Results

- **Part 1 Answer:** `4748769124`
- **Part 2 Answer:** `1525991432`

> Puzzle inputs are not included as they are unique per user.
