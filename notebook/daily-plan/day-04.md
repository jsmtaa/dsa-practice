---
status: unlearned
day: 4
topics: Recursion, Backtracking
target-problems: 6-8
---

# Day 04 — Recursion + Backtracking

## Goals
Master exhaustive state space exploration with early pruning.

## Techniques to Practice
- [[recursion-backtracking|Recursion / Backtracking]] — Explore all possibilities; undo choices to try alternatives

## Core Insights
- **Subsets**: Generate all 2^n subsets (include or exclude each element)
- **Permutations**: All orderings of n elements
- **Combinations**: All k-subsets of n elements
- **Pruning**: Cut branches early when constraints violated

## Problem Targets
- Subsets: all subsets of array
- Permutations: all orderings (with duplicates handling)
- Combinations: C(n, k)
- Sudoku solver or simple N-Queens (optional, harder)

## Linked Invariant
[[invariant-state-space-search]]

## Template to Memorize
```python
def backtrack(path, remaining):
    if base_case_reached:
        result.append(path)
        return
    for choice in remaining:
        path.append(choice)
        backtrack(path, remaining - {choice})
        path.pop()  # CRITICAL: undo choice
```

## Status
- [ ] Subsets: all 2^n subsets
- [ ] Permutations: all orderings
- [ ] Combinations: C(n, k)
- [ ] Handle duplicates in permutations
- [ ] 6-8 problems solved
