# Day 8 – Advent of Code 2025
**Puzzle:** Playground

This folder contains my solutions for **Day 8** of Advent of Code 2025.

---

## Problem Summary

Each line of the input represents the **3D coordinates** of a junction box suspended in space.

The Elves connect junction boxes using strings of lights.  
When two boxes are connected, electricity flows between them, forming a **circuit**.

Connections are always made by choosing the **closest pair of junction boxes** based on
**straight-line (Euclidean) distance**.

---

## Part 1

- Repeatedly connect the **closest unconnected pair** of junction boxes
- Perform **exactly 1000 connections**
- Junction boxes already in the same circuit are ignored
- After all connections, determine the **sizes of all circuits**
- Multiply the sizes of the **three largest circuits**

---

## Part 2

- Continue connecting the **closest unconnected pairs**
- Stop when **all junction boxes are in a single circuit**
- Find the **last connection** that caused full connectivity
- Multiply the **X-coordinates** of the two junction boxes in that final connection

---

## Structure

- `part1.py` – Solution for Part 1
- `part2.py` – Solution for Part 2

---

## What I Learned

- Efficient use of **Union-Find (Disjoint Set Union)**
- Avoiding unnecessary distance recalculations
- Applying Kruskal-style logic without building a full MST
- Handling large inputs with performance constraints

---

## Results

- **Part 1 Answer:** `46398`
- **Part 2 Answer:** `8141888143`

> Puzzle inputs are not included as they are unique per user.
