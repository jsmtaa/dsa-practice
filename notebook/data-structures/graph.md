---
status: core
---

# Graph

## Definition
Set of nodes (vertices) connected by edges. Can be directed (edges have direction) or undirected. Weighted edges have associated costs.

## Representations
- Adjacency list: O(V + E) space, efficient for sparse graphs
- Adjacency matrix: O(V²) space, efficient for dense graphs
- Edge list: simple but slower for lookups

## Python Idiom
```python
from collections import defaultdict, deque

# Adjacency list (default for competition)
graph = defaultdict(list)
graph[1].append(2)  # Edge from 1 to 2
graph[1].append(3)

# Undirected: add edge both ways
def add_edge(u, v, weight=1):
    graph[u].append((v, weight))
    graph[v].append((u, weight))

# DFS
def dfs(node, visited):
    visited.add(node)
    for neighbor, _ in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)

# BFS
def bfs(start):
    queue = deque([start])
    visited = {start}
    while queue:
        node = queue.popleft()
        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

## Operations & Complexity
- BFS: O(V + E)
- DFS: O(V + E)
- Dijkstra: O((V + E) log V)
- Topological sort: O(V + E)

## Linked Techniques
- [[bfs|BFS]]
- [[dfs|DFS]]
- [[topological-sort|Topological Sort]]
- [[dijkstra|Dijkstra]]
- [[union-find|Union-Find]]

## When to Use
- Social networks, web crawling, recommendation systems
- Map routing, flight connections
- Dependency resolution
