# Day 3 – Advent of Code 2025
**Puzzle:** Lobby

This folder contains my solutions for **Day 3** of Advent of Code 2025.

---

## Problem Summary

Each input line represents a **bank of batteries**, where each digit (1–9) is a battery’s joltage.

The batteries must be selected **in order** (no rearranging).

The joltage output of a bank is the **number formed by the selected digits**.

---

### Part 1
Turn on **exactly two batteries** in each bank.

The goal is to form the **largest possible two-digit number** from each line and sum the results across all banks.

---

### Part 2
Turn on **exactly twelve batteries** in each bank.

The goal is to form the **largest possible twelve-digit number** from each line and sum the results across all banks.

---

## Structure

- `part1.py` – Solution for Part 1  
- `part2.py` – Solution for Part 2  

---

## What I Learned

- Using **greedy strategies** to maximize values under ordering constraints
- Modeling numeric problems using **string-based logic**
- Efficiently selecting optimal subsequences without brute force
- How increasing constraints (2 digits → 12 digits) change the algorithmic approach

---

## Results

- **Part 1 Answer:** `17301`
- **Part 2 Answer:** `172162399742349`

> Puzzle inputs are not included as they are unique per user.
