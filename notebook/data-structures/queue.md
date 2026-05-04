---
status: core
---

# Queue

## Definition
FIFO (First In, First Out) data structure. First element added is the first to be removed. Used for BFS, scheduling, buffering.

## Operations & Complexity
- Enqueue (add): O(1)
- Dequeue (remove): O(1)
- Peek (front): O(1)
- IsEmpty: O(1)

## Python Idiom
```python
from collections import deque

# Using deque (preferred for queues)
queue = deque()
queue.append(1)  # Enqueue (add to back)
queue.popleft()  # Dequeue (remove from front), returns 1
front = queue[0] if queue else None  # Peek

# Using list (less efficient — O(n) popleft)
queue = []
queue.append(1)  # Append to back
queue.pop(0)  # Pop from front (slow!)
```

## Linked Techniques
- [[bfs|BFS]]
- [[topological-sort|Topological Sort]]

## When to Use
- Breadth-first search
- Level-order tree traversal
- Job scheduling (FIFO)
- Producer-consumer problems
