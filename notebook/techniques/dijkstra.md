---
status: unlearned
day: 13
invariants:
  - invariant-monotonicity
---

# Dijkstra's Algorithm

## Core Idea
Find the shortest path from a source to all other nodes in a weighted graph (no negative weights). Use a min-heap to always process the closest unvisited node next.

## When to Use
- Shortest path in weighted graphs (non-negative weights)
- Network routing protocols
- Finding k-th smallest element using Dijkstra trick

## Template Code
```python
import heapq
from collections import defaultdict

def dijkstra(graph, start, n):
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]  # (distance, node)
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    
    return dist

# Example: graph as adjacency list
# graph[u] = [(v, weight), ...]
```

## Linked Invariants
- [[invariant-monotonicity]]

## Linked Problems
(Day 13: shortest path, network delays, etc.)

## Common Pitfalls
- Using on graphs with negative edge weights (use Bellman-Ford instead)
- Not checking `if d > dist[u]` before processing (can process nodes multiple times)
- Using wrong comparison: <= instead of <
- Heap operations: heappush vs. heappop order
