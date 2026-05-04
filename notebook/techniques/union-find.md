---
status: unlearned
day: 9
invariants:
  - invariant-state-space-search
---

# Union-Find (Disjoint Set Union - DSU)

## Core Idea
Efficiently track which elements belong to the same group (connected component) using a parent array. Path compression and union by rank make operations nearly O(1) amortized.

## When to Use
- Connected components in a graph
- Detecting cycles in an undirected graph
- Kruskal's minimum spanning tree algorithm
- Equivalent elements / group membership

## Template Code
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False  # Already in same set
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

# Cycle detection
def has_cycle(n, edges):
    uf = UnionFind(n)
    for u, v in edges:
        if not uf.union(u, v):
            return True
    return False

# Connected components
def count_components(n, edges):
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return len(set(uf.find(i) for i in range(n)))
```

## Linked Invariants
- [[invariant-state-space-search]]

## Linked Problems
(Day 9: connected components, cycle detection, MST with Kruskal's, etc.)

## Common Pitfalls
- Not using path compression in find() (slower queries)
- Not using union by rank (slower unions)
- Confusing union (return True only on first union) with simple merge
- Off-by-one in initialization (parent should be list(range(n)))
