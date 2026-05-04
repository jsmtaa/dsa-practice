---
status: unlearned
day: 5
invariants:
  - invariant-monotonicity
---

# Monotonic Stack

## Core Idea
Maintain a stack where elements are in monotonic order (increasing or decreasing). When a new element violates this order, pop elements and record relationships (e.g., "next greater element"). This solves certain problems in O(n) instead of O(n²).

## When to Use
- Next/previous greater/smaller element
- Stock span problem
- Largest rectangle in histogram
- Trapping rain water

## Template Code
```python
# Next greater element (monotonic stack)
def next_greater(arr):
    result = [-1] * len(arr)
    stack = []  # Store indices
    for i in range(len(arr) - 1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = arr[stack[-1]]
        stack.append(i)
    return result

# Largest rectangle in histogram (monotonic stack)
def largest_rectangle(heights):
    stack = []
    max_area = 0
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            idx = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            area = heights[idx] * width
            max_area = max(max_area, area)
        stack.append(i)
    return max_area
```

## Linked Invariants
- [[invariant-monotonicity]]

## Linked Problems
(Day 5: next greater element, stock span, largest rectangle, trapping rain water)

## Common Pitfalls
- Confusing increasing vs. decreasing monotonic stack
- Storing values vs. indices (indices are usually clearer)
- Off-by-one errors in width calculation for histogram problems
- Not understanding why the invariant guarantees O(n): each element pushed/popped exactly once
