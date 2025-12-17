# Day 12 – Advent of Code 2025
**Puzzle:** Christmas Tree Farm

This folder contains my solution for **Day 12** of Advent of Code 2025.

---

## Problem Summary

The puzzle describes a set of **irregular present shapes** and a set of
**rectangular regions under Christmas trees**.

Each region specifies how many presents of each shape must be placed.

Rules:
- Presents are placed on a **2D grid**
- Shapes may be **rotated and flipped**
- Presents **cannot overlap**
- All required presents must fit completely inside the region

The task is to determine **how many regions can successfully fit all required presents**.

---

## Part 1

For each region:
- Generate all rotations and flips of each present shape
- Attempt to place the required presents using **backtracking**
- Reject regions where total present area exceeds region area
- Count regions where a valid placement exists

---

## Part 2

Part 2 is a **story-only conclusion** and does not introduce any new computational problem.
No additional code is required.

---

## Structure

- `part1.py` – Solution for Part 1

---

## What I Learned

- Backtracking with pruning for packing problems
- Shape normalization and rotation handling
- Constraint-based search optimization
- Writing efficient solvers for NP-style placement problems

---

## Results

- **Part 1 Answer:** `481`
- **Part 2:** Story completion ⭐

> Puzzle inputs are not included as they are unique per user.
