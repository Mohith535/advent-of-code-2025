# Day 1 – Advent of Code 2025  
**Puzzle:** Secret Entrance

This folder contains my solutions for **Day 1** of Advent of Code 2025.

---

##  Problem Overview

The puzzle simulates a circular dial numbered from **0 to 99**, starting at position **50**.

Each instruction rotates the dial:
- `L<number>` → rotate left
- `R<number>` → rotate right

The dial wraps around circularly (modulo 100).

### Part 1  
Count how many times the dial **ends at position 0 after a rotation**.

### Part 2  
Count how many times the dial **points at position 0 at any moment**,  
including *during* rotations.

---

##  Structure

- `part1.py` – Solution for Part 1  
- `part2.py` – Solution for Part 2  

---

##  What I Learned

- Using **modulo arithmetic** to model circular systems
- Parsing directional instructions efficiently
- Understanding subtle problem differences between Part 1 and Part 2
- Writing clean, readable logic instead of brute-force simulation

---

##  Puzzle Input

Puzzle inputs are **not included** in this repository  
as they are **unique per user**, per Advent of Code rules.

---

## My Results

- **Part 1 Answer:** `1043`
- **Part 2 Answer:** `5963`
