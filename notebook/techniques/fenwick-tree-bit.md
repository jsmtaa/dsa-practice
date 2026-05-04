---
status: unlearned
day: 15
invariants:
  - invariant-range-queries
---

# Fenwick Tree (Binary Indexed Tree - BIT)

## Core Idea
Use a clever indexing scheme to store partial sums. Enables O(log n) prefix sum queries and point updates with O(n) space (vs. segment tree's 4n).

## When to Use
- Prefix sum queries with point updates (simpler than segment tree)
- Range sum queries on dynamic arrays
- Competitive programming: memory-efficient alternative to segment tree
- Less flexible than segment tree (harder for range updates)

## Template Code
```python
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, idx, delta):
        idx += 1  # 1-indexed
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & (-idx)  # Add last set bit
    
    def prefix_sum(self, idx):
        idx += 1  # 1-indexed
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & (-idx)  # Remove last set bit
        return result
    
    def range_sum(self, l, r):
        if l == 0:
            return self.prefix_sum(r)
        return self.prefix_sum(r) - self.prefix_sum(l - 1)

# Usage:
# ft = FenwickTree(n)
# ft.update(i, val)  # Add val to position i
# ft.range_sum(l, r)  # Get sum from l to r inclusive
```

## Linked Invariants
- [[invariant-range-queries]]

## Linked Problems
(Day 15: range sum updates, inversion count, coordinate compression, etc.)

## Common Pitfalls
- 1-indexed vs. 0-indexed: BIT is 1-indexed internally
- Bit manipulation: `idx & (-idx)` extracts the last set bit
- Updating with delta vs. setting a value (FenwickTree.update uses delta)
- Rebuilding entire tree if needed: O(n log n)
