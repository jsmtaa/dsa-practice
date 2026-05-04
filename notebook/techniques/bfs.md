---
status: unlearned
day: 8
invariants:
  - invariant-state-space-search
---

# BFS (Breadth-First Search)

## Core Idea
Explore nodes layer by layer using a **queue**. BFS finds the shortest path in an unweighted graph and is useful for level-order traversal.

## When to Use
- Shortest path in unweighted graph
- Level-order tree traversal
- Detecting cycles in undirected graph
- Island count, connected components
- Multi-source shortest path

## Template Code
```python
from collections import deque, defaultdict

# BFS on graph
def bfs_graph(graph, start):
    queue = deque([start])
    visited = {start}
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

# BFS shortest path
def shortest_path(graph, start, end):
    queue = deque([(start, 0)])  # (node, distance)
    visited = {start}
    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1

# Level-order tree traversal
def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

## Linked Invariants
- [[invariant-state-space-search]]

## Linked Problems
(Day 8: shortest path, level-order traversal, connected components, etc.)

## Common Pitfalls
- **CRITICAL**: BFS uses **queues** (FIFO), not stacks — using a stack turns it into DFS
- Not marking nodes as visited before adding to queue (infinite loop)
- Confusing with Dijkstra (BFS is unweighted only; Dijkstra handles weights)
- Not checking if neighbor is already visited before queueing
