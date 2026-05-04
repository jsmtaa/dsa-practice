---
status: partial
day: 5
invariants:
  - invariant-state-space-search
---

# Stacks / Queues

## Core Idea
Stacks (LIFO) and queues (FIFO) are fundamental data structures. Stacks enable DFS and recursion simulation; queues enable BFS. Monotonic stacks and deques handle special problems like "next greater element."

## When to Use
- DFS simulation: use stack
- BFS traversal: use queue
- Matching parentheses or expression parsing: stack
- Sliding window with decreasing elements: deque
- Next/previous greater/smaller element: monotonic stack

## Template Code
```python
from collections import deque

# Stack for DFS
def dfs_iterative(graph, start):
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])
    return visited

# Queue for BFS
def bfs(graph, start):
    queue = deque([start])
    visited = {start}
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

# Monotonic stack: next greater element
def next_greater(arr):
    result = [-1] * len(arr)
    stack = []
    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result
```

## Linked Invariants
- [[invariant-state-space-search]]

## Linked Problems
(Day 5: monotonic stack, stock span, next greater element, sliding window max with deque)

## Common Pitfalls
- **CRITICAL**: BFS uses **queues**, DFS uses **stacks** — mixing them up causes wrong traversal
- Not tracking visited nodes in BFS/DFS, causing infinite loops
- Monotonic stack: understanding the invariant (increasing or decreasing?)
- Deque operations: `append()`, `pop()`, `popleft()` vs. `appendleft()`
- Using wrong data structure for the problem
