---
status: unlearned
day: 4
invariants:
  - invariant-state-space-search
  - invariant-optimal-substructure
---

# Recursion / Backtracking

## Core Idea
Recursively explore the solution space by making a choice, recursing deeper, and undoing the choice to try alternatives. Backtracking prunes branches early when constraints are violated.

## When to Use
- Subsets, permutations, combinations
- N-Queens, Sudoku solver
- Word search on a grid
- Partition problems
- Any exhaustive search with early pruning

## Template Code
```python
# Subsets (all 2^n subsets)
def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])  # Add current subset
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()  # Backtrack
    backtrack(0, [])
    return result

# Permutations
def permutations(nums):
    result = []
    def backtrack(path, remaining):
        if not remaining:
            result.append(path)
            return
        for i, num in enumerate(remaining):
            backtrack(path + [num], remaining[:i] + remaining[i + 1:])
    backtrack([], nums)
    return result

# Combinations
def combinations(n, k):
    result = []
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
    backtrack(1, [])
    return result
```

## Linked Invariants
- [[invariant-state-space-search]]
- [[invariant-optimal-substructure]]

## Linked Problems
(Day 4: subsets, permutations, combinations, N-Queens, word search, etc.)

## Common Pitfalls
- Not backtracking (forgetting `.pop()` or undo step) — explores wrong state space
- Not pruning early — exponential blowup even with valid logic
- Duplicate results in permutations — not handling duplicates in input
- Stack overflow from deep recursion (Python has recursion limit)
- Confusing permutations (order matters) with combinations (order doesn't)
