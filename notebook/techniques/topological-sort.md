---
status: unlearned
day: 9
invariants:
  - invariant-state-space-search
---

# Topological Sort

## Core Idea
Order nodes in a directed acyclic graph (DAG) such that for every directed edge (u, v), u comes before v. Kahn's algorithm (BFS-based) is easier to implement than DFS-based topological sort.

## When to Use
- Course scheduling with prerequisites
- Dependency resolution
- Build system dependency order
- Task scheduling with constraints

## Template Code
```python
from collections import deque, defaultdict

# Kahn's algorithm (BFS-based)
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
    
    return result if len(result) == n else []  # Empty if cycle exists

# DFS-based topological sort (harder)
def topological_sort_dfs(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    
    visited = [False] * n
    rec_stack = [False] * n
    result = []
    
    def dfs(node):
        visited[node] = True
        rec_stack[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if not dfs(neighbor):
                    return False
            elif rec_stack[neighbor]:
                return False  # Cycle detected
        rec_stack[node] = False
        result.append(node)
        return True
    
    for i in range(n):
        if not visited[i]:
            if not dfs(i):
                return []
    return result[::-1]
```

## Linked Invariants
- [[invariant-state-space-search]]

## Linked Problems
(Day 9: course schedule, task scheduling with prerequisites, etc.)

## Common Pitfalls
- Confusing topological order (u before v) with reverse topological order
- Forgetting to check for cycles (if not all nodes in result, cycle exists)
- DFS-based: forgetting to pop from recursion stack
- In-degree vs. out-degree: Kahn uses in-degree
