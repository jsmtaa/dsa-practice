---
status: unlearned
day: 8
topics: BFS, DFS
target-problems: 8
---

# Day 08 — Graph Basics: BFS + DFS

## Goals
Master graph traversal. BFS for shortest paths; DFS for exploring all possibilities.

## Techniques to Practice
- [[bfs|BFS]] — Layer-by-layer exploration with **queue**; finds shortest unweighted path
- [[dfs|DFS]] — Deep exploration with **stack** or recursion; finds all paths and connected components

## Core Insights
- **CRITICAL**: BFS uses **queue**, DFS uses **stack**
- **BFS**: Each level complete before next; O(V + E) time
- **DFS**: Go deep, backtrack; O(V + E) time
- **Visited set**: Essential in both to avoid infinite loops

## Problem Targets
- Connected components (DFS or BFS)
- BFS shortest path in unweighted graph
- Flood fill (either DFS or BFS)
- Cycle detection in undirected graph
- Graph representation: adjacency list with defaultdict

## Linked Invariant
[[invariant-state-space-search]]

## Template to Memorize
```python
# BFS shortest path
def bfs(graph, start, end):
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

# DFS iterative
def dfs(graph, start):
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])
```

## Status
- [ ] Graph representation (adjacency list)
- [ ] BFS: shortest path
- [ ] DFS: all reachable nodes
- [ ] Connected components
- [ ] Flood fill
- [ ] Cycle detection
- [ ] 8 problems solved
