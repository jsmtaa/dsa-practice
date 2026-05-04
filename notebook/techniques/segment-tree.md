---
status: unlearned
day: 15
invariants:
  - invariant-range-queries
---

# Segment Tree

## Core Idea
Build a binary tree where each node represents a range and stores an aggregate (sum, min, max). Enables O(log n) range queries and point updates on dynamic data.

## When to Use
- Range sum/min/max queries with point updates
- Range update with point queries
- Lazy propagation for range updates
- More flexible than Fenwick Tree but uses more memory

## Template Code
```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(arr, left_child, start, mid)
            self.build(arr, right_child, mid + 1, end)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]
    
    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            if idx <= mid:
                self.update(left_child, start, mid, idx, val)
            else:
                self.update(right_child, mid + 1, end, idx, val)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]
    
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        p1 = self.query(left_child, start, mid, l, r)
        p2 = self.query(right_child, mid + 1, end, l, r)
        return p1 + p2
```

## Linked Invariants
- [[invariant-range-queries]]

## Linked Problems
(Day 15: range sum queries, segment tree variants, etc.)

## Common Pitfalls
- Tree size: 4*n is safe but exact size can be calculated
- Index calculations: left = 2*node+1, right = 2*node+2
- Lazy propagation adds complexity; start with simple segment tree
