---
status: unlearned
day: 2
invariants:
  - invariant-range-queries
---

# Prefix Sum

## Core Idea
Precompute cumulative sums so range queries (sum from index L to R) are answered in O(1) instead of O(n). For 2D, use a different formula to handle the overlap.

## When to Use
- "Sum of elements from L to R"
- 2D grid: "sum of rectangle from (r1, c1) to (r2, c2)"
- Subarray sum equals K (combine with hashmap)
- Quick aggregate queries on static (non-updated) data

## Template Code
```python
# 1D prefix sum
def prefix_sum_1d(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    # Query: sum from L to R (inclusive)
    # return prefix[R + 1] - prefix[L]

# 2D prefix sum
def prefix_sum_2d(matrix):
    m, n = len(matrix), len(matrix[0])
    prefix = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            prefix[i][j] = matrix[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]
    # Query: sum of rectangle (r1, c1) to (r2, c2)
    # return prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] - prefix[r2 + 1][c1] + prefix[r1][c1]
```

## Linked Invariants
- [[invariant-range-queries]]

## Linked Problems
(Day 2: subarray sum equals K, 2D matrix sum queries, etc.)

## Common Pitfalls
- Off-by-one errors in indexing prefix array (need `n+1` size for n elements)
- 2D prefix formula: forgetting the `+ prefix[i - 1][j - 1]` term
- Confusing inclusive vs. exclusive ranges
- Using on a dynamic (updated) array without segment tree
