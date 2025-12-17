# Day 10 – Advent of Code 2025
**Puzzle:** Factory

This folder contains my solutions for **Day 10** of Advent of Code 2025.

---

## Problem Summary

Each line of the input describes a **factory machine**, consisting of:

- An **indicator light diagram** `[ ]`
- Multiple **button wiring schematics** `( )`
- A set of **joltage requirements** `{ }`

Each machine is solved independently.  
The final answer is the **sum of the minimum button presses** required for all machines.

---

## Part 1 – Indicator Lights

- All lights start **OFF**
- `#` means the light must be **ON**
- Pressing a button **toggles** the listed lights
- Buttons can be pressed **any number of times**
- Goal: **minimum total presses**

### Key Insight

This is a **linear system over GF(2)**:
- Order of presses doesn’t matter
- Each press flips bits
- The goal is the **minimum Hamming-weight solution**

---

## Part 2 – Joltage Counters

- Indicator lights are ignored
- Each counter starts at `0`
- Pressing a button **adds +1** to listed counters
- Goal is to reach **exact joltage values**
- Must minimize total button presses

### Key Insight

This is an **integer linear optimization problem**, solved using
**Integer Linear Programming (ILP)**.

---

## Structure

- `part1.py` – Indicator light configuration (binary system)
- `part2.py` – Joltage counter configuration (ILP)
- `README.md` – Explanation and results

---

## What I Learned

- Modeling puzzles as **linear algebra problems**
- Difference between **GF(2)** systems and **integer systems**
- When brute force is valid and when optimization is required
- Practical use of **ILP solvers (PuLP)**

---

## Results

- **Part 1 Answer:** `502`
- **Part 2 Answer:** `21467`

> Puzzle inputs are not included as they are unique per user.
