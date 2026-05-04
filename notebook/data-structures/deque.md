---
status: core
---

# Deque (Double-Ended Queue)

## Definition
Double-ended queue allowing insertion and deletion from both ends. More flexible than queue or stack alone.

## Operations & Complexity
- Append (add to back): O(1)
- AppendLeft (add to front): O(1)
- Pop (remove from back): O(1)
- PopLeft (remove from front): O(1)
- Access by index: O(1)

## Python Idiom
```python
from collections import deque

dq = deque([1, 2, 3])
dq.append(4)  # Add to back: [1, 2, 3, 4]
dq.appendleft(0)  # Add to front: [0, 1, 2, 3, 4]
dq.pop()  # Remove from back, returns 4
dq.popleft()  # Remove from front, returns 0
dq[1]  # Access by index, returns 1

# Rotate
dq.rotate(1)  # Rotate right by 1
```

## Linked Techniques
- [[sliding-window|Sliding Window]]
- [[monotonic-stack|Monotonic Stack]]

## When to Use
- Sliding window with decreasing/increasing elements
- LRU cache implementation
- BFS and DFS both (though single-ended structures better)
- Any problem needing both queue and stack operations
