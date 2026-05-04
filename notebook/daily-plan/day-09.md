---
status: unlearned
day: 9
topics: Topological Sort, Union-Find
target-problems: 6-8
---

# Day 09 — Graph Intermediate: Topological Sort + Union-Find

## Goals
Master two essential graph algorithms: dependency ordering and connected components.

## Techniques to Practice
- [[topological-sort|Topological Sort]] — Order nodes so dependencies are resolved first
- [[union-find|Union-Find]] — Track connected components; path compression + union by rank

## Core Insights
- **Topological Sort**: Use Kahn's BFS-based algorithm (easier than DFS)
- **Union-Find**: find() with path compression, union() with rank; near O(1) amortized
- **Kahn's algorithm**: Process nodes with in-degree 0; decrement neighbors' in-degrees

## Problem Targets
- Course schedule (dependency ordering)
- Graph cycle detection (Union-Find)
- Connected components count
- Minimum spanning tree (Kruskal's + Union-Find)

## Linked Invariant
[[invariant-state-space-search]]

## Template to Memorize
```python
# Kahn's topological sort
def topological_sort(n, edges):
    graph = defaultdict(list)
    in_degree = [0] * n
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return result if len(result) == n else []

# Union-Find
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True
```

## Status
- [ ] Topological sort: course schedule
- [ ] Union-Find: cycle detection
- [ ] Connected components count
- [ ] Union-Find: path compression + rank
- [ ] 6-8 problems solved
