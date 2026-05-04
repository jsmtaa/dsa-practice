---
status: unlearned
day: 15
topics: Segment Tree, Fenwick Tree (BIT)
target-problems: 6-8 (Hard/Extreme)
---

# Day 15 — Range Queries: Segment Tree / Fenwick Tree (BIT)

## Goals
Master advanced range query data structures. BIT is simpler; Segment Tree more flexible.

## Techniques to Practice
- [[segment-tree|Segment Tree]] — O(log n) updates + range queries; 4n memory
- [[fenwick-tree-bit|Fenwick Tree (BIT)]] — O(log n) point updates + prefix sums; n memory

## Key Insights
- **Segment Tree**: More flexible (range updates, lazy propagation)
- **Fenwick Tree**: Simpler, less memory; perfect for competitive programming
- **Use cases**: Range sum queries with point updates (static data → prefix sum)

## Problem Targets
- Range sum queries with point updates
- Inversion count in array
- Coordinate compression (when values are large)

## Template: Fenwick Tree
```python
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, idx, delta):
        idx += 1
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & (-idx)
    
    def prefix_sum(self, idx):
        idx += 1
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & (-idx)
        return result
```

## Status
- [ ] Fenwick Tree: point update + prefix sum
- [ ] Segment Tree: range query + point update
- [ ] Inversion count
- [ ] Coordinate compression
- [ ] 6-8 problems solved (Hard/Extreme)
