---
status: core
---

# Stack

## Definition
LIFO (Last In, First Out) data structure. Last element added is the first to be removed. Used for DFS, expression evaluation, undo functionality.

## Operations & Complexity
- Push (add): O(1)
- Pop (remove): O(1)
- Peek (top element): O(1)
- IsEmpty: O(1)

## Python Idiom
```python
# Using list as stack
stack = []
stack.append(1)  # Push
stack.append(2)
top = stack.pop()  # Pop, returns 2
if stack:  # Check if not empty
    peek = stack[-1]  # Peek

# Using deque for better performance
from collections import deque
stack = deque()
stack.append(1)  # Push
stack.pop()  # Pop
stack[-1]  # Peek
```

## Linked Techniques
- [[dfs|DFS]]
- [[recursion-backtracking|Recursion / Backtracking]]
- [[monotonic-stack|Monotonic Stack]]

## When to Use
- Depth-first search
- Expression parsing and evaluation
- Backtracking
- Function call stack simulation
