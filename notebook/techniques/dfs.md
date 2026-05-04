---
status: unlearned
day: 8
invariants:
  - invariant-state-space-search
---

# DFS (Depth-First Search)

## Core Idea
Explore as far as possible along each branch using **recursion or a stack**. DFS explores one path fully before backtracking. Useful for detecting cycles, topological sort, and finding connected components.

## When to Use
- Detecting cycles in a graph
- Connected components, strongly connected components
- Topological sort
- Path finding (not shortest path unless unweighted)
- All paths, all valid parentheses sequences

## Template Code
```python
from collections import defaultdict

# DFS recursive
def dfs_recursive(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# DFS iterative using stack
def dfs_iterative(graph, start):
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])
    return visited

# DFS cycle detection
def has_cycle(graph):
    visited = set()
    rec_stack = set()
    
    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(node)
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False
```

## Linked Invariants
- [[invariant-state-space-search]]

## Linked Problems
(Day 8: cycle detection, connected components, DFS path finding, etc.)

## Common Pitfalls
- **CRITICAL**: DFS uses **stacks** (LIFO), not queues — using a queue turns it into BFS
- **Common confusion**: BFS uses queues, DFS uses stacks. This is THE critical distinction.
- Forgetting to mark nodes as visited (infinite loops)
- Confusing recursive DFS with iterative DFS implementation
- Cycle detection: forgetting the recursion stack vs. visited set distinction
