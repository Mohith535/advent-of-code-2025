# Day 5 – Advent of Code 2025
**Puzzle:** Cafeteria

This folder contains my solutions for **Day 5** of Advent of Code 2025.

---

## Problem Summary

The input file contains:
1. A list of **fresh ingredient ID ranges**
2. A blank line
3. A list of **available ingredient IDs**

An ingredient ID is **fresh** if it falls inside **any** of the given ranges.

Ranges:
- Are inclusive
- Can overlap

---

## Part 1

Determine how many of the **available ingredient IDs** are fresh.

---

## Part 2

Ignore the available ingredient IDs.

Determine **how many unique ingredient IDs** are considered fresh based **only** on the given ranges.

Because the ranges can be extremely large, the solution must:
- Merge overlapping ranges
- Count efficiently without enumerating every ID

---

## Structure

- `part1.py` – Solution for Part 1
- `part2.py` – Solution for Part 2

---

## What I Learned

- Parsing structured input with multiple sections
- Interval overlap and merging logic
- Efficient counting of large numeric ranges
- Avoiding brute-force solutions for massive datasets

---

## Results

- **Part 1 Answer:** `798`
- **Part 2 Answer:** `366181852921027`

> Puzzle inputs are not included as they are unique per user.
