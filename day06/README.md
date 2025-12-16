# Day 6 – Advent of Code 2025
**Puzzle:** Trash Compactor

This folder contains my solutions for **Day 6** of Advent of Code 2025.

---

## Problem Summary

The input represents a very wide **worksheet of math problems** arranged horizontally.

Each problem:
- Contains numbers written vertically
- Ends with an operator (`+` or `*`)
- Is separated from other problems by a column of spaces

The goal is to evaluate each problem correctly and then **sum all results**.

---

## Part 1

- Each problem spans multiple adjacent columns
- Numbers are constructed **row-wise** by reading digits left to right
- The operator at the bottom applies to all numbers in that problem
- The final answer is the **sum of all problem results**

---

## Part 2

- Cephalopod math is read **right-to-left**
- Each column forms a number (top digit = most significant)
- Problems are still separated by blank columns
- The operator remains at the bottom
- The final answer is again the **sum of all results**

---

## Structure

- `part1.py` – Solution for Part 1
- `part2.py` – Solution for Part 2

---

## What I Learned

- Parsing irregular grid-based inputs
- Column-wise vs row-wise number construction
- Careful handling of spacing-based separation
- Translating problem descriptions into robust logic

---

## Results

- **Part 1 Answer:** `3968933219902`
- **Part 2 Answer:** `6019576291014`

> Puzzle inputs are not included as they are unique per user.
