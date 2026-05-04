---
status: core
related_techniques: 2
---

# Overlapping Subproblems Invariant

## Definition
Overlapping subproblems occur when solving a problem requires solving the same smaller subproblems many times. Memoization or tabulation (dynamic programming) caches these solutions to avoid redundant computation.

## Recognition Signals
- Recursive solution repeats the same subproblems (Fibonacci-like)
- Exponential time complexity naive recursion (e.g., 2^n)
- "Can I avoid recalculating the same thing?" is the key insight
- Memoization or caching hint in problem description
- Counting paths, ways, combinations in recursive structures

## Techniques That Exploit It
- [[dynamic-programming-1d|Dynamic Programming (1D)]]
- [[dynamic-programming-2d|Dynamic Programming (2D)]]
- [[dynamic-programming-intro|Dynamic Programming (Intro)]]

## Common Failure Modes
- Using only recursion without memoization on overlapping subproblems (TLE)
- Incorrect memoization key — forgetting to include all state variables
- Confusing memoization (top-down) with tabulation (bottom-up)
- Cache size too large for the constraints
- Forgetting to handle base cases before memoization lookup
