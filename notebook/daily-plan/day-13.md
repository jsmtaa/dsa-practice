---
status: unlearned
day: 13
topics: Dijkstra, Bellman-Ford
target-problems: 6-8
---

# Day 13 — Advanced Graphs: Dijkstra + Shortest Paths

## Goals
Master shortest path algorithms. Dijkstra for non-negative weights; Bellman-Ford for negative weights.

## Techniques to Practice
- [[dijkstra|Dijkstra]] — O((V + E) log V) with min-heap; non-negative weights
- [[bellman-ford|Bellman-Ford]] — O(VE); detects negative cycles

## Key Differences
- **Dijkstra**: Greedy; faster but fails on negative edges
- **Bellman-Ford**: DP-like; slower but handles negatives + detects cycles

## Problem Targets
- Shortest path in weighted graph (Dijkstra)
- Network delay time
- Cheapest flights with K stops (Bellman-Ford variant)

## Template: Dijkstra
```python
import heapq
def dijkstra(graph, start, n):
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist
```

## Status
- [ ] Dijkstra implementation
- [ ] Shortest path queries
- [ ] Network delay time
- [ ] Bellman-Ford (negative cycles)
- [ ] 6-8 problems solved
