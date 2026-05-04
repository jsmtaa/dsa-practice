---
status: unlearned
day: 11
topics: DP 2D, LIS
target-problems: 6-8
---

# Day 11–12 — Dynamic Programming Part 2

## Day 11 Goals
Master 2D DP and Longest Increasing Subsequence (LIS) patterns.

## Techniques to Practice
- [[dynamic-programming-2d|Dynamic Programming (2D)]] — Extended DP on two dimensions
- [[longest-increasing-subsequence|Longest Increasing Subsequence]] — O(n²) naive, O(n log n) with bisect

## Core Insights
- **2D DP**: Often represents string ranges or grid problems (edit distance, LCS, knapsack)
- **LCS**: Longest common subsequence between two strings
- **Edit distance**: Levenshtein; how many edits to transform one string to another?
- **LIS**: O(n log n) uses binary search + tails array

## Problem Targets (Day 11)
- LCS: longest common subsequence
- Longest increasing subsequence (both O(n²) and O(n log n))

## Problem Targets (Day 12)
- Edit distance
- 2D knapsack (0/1 knapsack with 2D items)
- Grid path problems

## Linked Invariant
[[invariant-optimal-substructure]], [[invariant-overlapping-subproblems]], [[invariant-monotonicity]] for LIS

## Status
- [ ] LCS implementation
- [ ] LIS O(n²) approach
- [ ] LIS O(n log n) with bisect
- [ ] Edit distance
- [ ] 2D knapsack
- [ ] 6-8 problems per day
