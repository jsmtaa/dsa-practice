---
status: unlearned
day: 13
invariants:
  - invariant-optimal-substructure
---

# Bellman-Ford Algorithm

## Core Idea
Find shortest paths from a source, even with negative edge weights. Relax all edges n-1 times. If distances still improve on iteration n, a negative cycle exists.

## When to Use
- Shortest path with negative weights
- Detecting negative cycles
- Currency arbitrage problems
- More general than Dijkstra, but slower (O(VE) vs. O(E log V))

## Template Code
```python
def bellman_ford(edges, n, start):
    dist = [float('inf')] * n
    dist[start] = 0
    
    # Relax edges n-1 times
    for _ in range(n - 1):
        for u, v, weight in edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
    
    # Check for negative cycle
    for u, v, weight in edges:
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
            return None  # Negative cycle detected
    
    return dist
```

## Linked Invariants
- [[invariant-optimal-substructure]]

## Linked Problems
(Day 13: shortest path with negative weights, negative cycle detection, etc.)

## Common Pitfalls
- Forgetting to check for negative cycles
- Running only n-1 iterations without cycle check
- Including `dist[u] != float('inf')` condition to avoid overflow
- Slower than Dijkstra for non-negative weights
