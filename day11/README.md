# Day 11 – Advent of Code 2025
**Puzzle:** Reactor

This folder contains my solutions for **Day 11** of Advent of Code 2025.

---

## Problem Summary

The puzzle input describes a **directed acyclic graph (DAG)** of devices.

- Each line defines a device and the devices it outputs to
- Data can only flow **forward**, never backward
- Paths are sequences of connected devices

---

## Part 1

- Start from the device labeled `you`
- End at the device labeled `out`
- Count **all distinct paths** from `you` to `out`
- Paths may branch but never loop

---

## Part 2

- Start from the device labeled `svr`
- End at the device labeled `out`
- Only count paths that pass through **both**
  - `dac`
  - `fft`
- These two devices may appear in **any order**
- Count all valid paths

---

## Structure

- `part1.py` – Counts all paths from `you` to `out`
- `part2.py` – Counts paths from `svr` to `out` that visit both `dac` and `fft`

---

## What I Learned

- Graph traversal using **DFS + memoization**
- Efficient path counting in DAGs
- State-based DP for path constraints
- Handling extremely large counts safely

---

## Results

- **Part 1 Answer:** `497`
- **Part 2 Answer:** `358564784931864`

> Puzzle inputs are not included as they are unique per user.
