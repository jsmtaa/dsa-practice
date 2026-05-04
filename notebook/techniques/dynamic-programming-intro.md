---
status: learned
day: 10
invariants:
  - invariant-optimal-substructure
  - invariant-overlapping-subproblems
---

# Dynamic Programming (Intro)

## Core Idea
Cache previously computed results to avoid redundant calculations. If a problem has overlapping subproblems and optimal substructure, caching solutions (memoization) turns exponential recursion into polynomial time.

## When to Use
- Fibonacci: naive recursion computes f(2), f(1) many times
- Coin change: "minimum coins to make amount X"
- House robber: "maximum sum without adjacent elements"
- Climbing stairs with variable step sizes

## Template Code
```python
# Memoization (top-down)
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# Tabulation (bottom-up)
def fib_dp(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

## Linked Invariants
- [[invariant-optimal-substructure]]
- [[invariant-overlapping-subproblems]]

## Linked Problems
(Day 10: climbing stairs, house robber, coin change, etc.)

## Common Pitfalls
- Forgetting to define the DP state clearly (what does dp[i] represent?)
- Using memoization on a problem that doesn't have overlapping subproblems (wastes memory)
- Off-by-one errors in DP table indexing
- Not handling base cases correctly
- Confusing time complexity: memoization is not always faster if subproblems don't overlap
