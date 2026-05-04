---
status: partial
day: 5
topics: Stacks, Queues, Monotonic Stack
target-problems: 8
---

# Day 05 — Stacks + Queues

## Goals
Master LIFO and FIFO structures; unlock monotonic stack patterns.

## Techniques to Practice
- [[stacks-queues|Stacks / Queues]] — Stack for DFS, queue for BFS; monotonic stack for next/prev greater
- [[monotonic-stack|Monotonic Stack]] — Maintain monotonic invariant to solve in O(n)

## Core Insights
- **Stack**: LIFO; for DFS and expression parsing
- **Monotonic Stack**: When new element breaks monotonicity, pop and record relationships
- **Common confusion**: BFS uses **queue**, DFS uses **stack**

## Problem Targets
- Monotonic stack: next greater element
- Stock span problem
- Sliding window maximum with deque
- Basic stack/queue operations

## Linked Invariant
[[invariant-state-space-search]] for stacks/queues, [[invariant-monotonicity]] for monotonic stack

## Template to Memorize
```python
# Monotonic stack: next greater element
result = [-1] * len(arr)
stack = []
for i in range(len(arr) - 1, -1, -1):
    while stack and arr[stack[-1]] <= arr[i]:
        stack.pop()
    if stack:
        result[i] = arr[stack[-1]]
    stack.append(i)
return result
```

## Status
- [ ] Basic stack operations
- [ ] Basic queue operations
- [ ] Next greater element (monotonic stack)
- [ ] Stock span
- [ ] Sliding window maximum (deque)
- [ ] 8 problems solved
