---
status: unlearned
day: 2
topics: Prefix Sum, Hashing
target-problems: 8-10
---

# Day 02 — Prefix Sum + Hashing

## Goals
Learn preprocessing techniques for fast queries and frequency-based problems.

## Techniques to Practice
- [[prefix-sum|Prefix Sum]] — Precompute cumulative sums for O(1) range queries
- [[hashing|Hashing]] — Use HashMap for O(1) frequency counting and lookups

## Core Insights
- **Prefix Sum**: Build array prefix[i] = sum of arr[0..i-1]; query [l, r] is prefix[r+1] - prefix[l]
- **Hashing**: Store complements/frequencies in a map to solve in one pass instead of nested loops

## Problem Targets
- 1D prefix sums: subarray sum equals K
- 2D prefix sums: rectangle sum in matrix
- HashMap: two sum variants, group anagrams, subarray sum equals K

## Linked Invariant
[[invariant-range-queries]]

## Template to Memorize
```python
# Prefix sum
prefix = [0] * (len(arr) + 1)
for i in range(len(arr)):
    prefix[i + 1] = prefix[i] + arr[i]
# Query [l, r]: prefix[r + 1] - prefix[l]

# Hashing
seen = {}
for num in arr:
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```

## Status
- [ ] 1D prefix sum: basic range query
- [ ] 2D prefix sum: matrix sum
- [ ] Subarray sum equals K (with prefix + hashmap)
- [ ] Two sum variants
- [ ] 8-10 problems solved
