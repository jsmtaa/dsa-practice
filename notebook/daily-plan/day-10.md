---
status: partial
day: 10
topics: Dynamic Programming (1D)
target-problems: 6-8
---

# Day 10 — Dynamic Programming Part 1

## Goals
Master 1D DP: memoization and tabulation. This unlocks Mediums.

## Techniques to Practice
- [[dynamic-programming-intro|Dynamic Programming (Intro)]]
- [[dynamic-programming-1d|Dynamic Programming (1D)]]

## Core Insights
- **Memoization**: Top-down; call @lru_cache and let recursion build the solution
- **Tabulation**: Bottom-up; build dp array iteratively
- **DP state**: Define clearly — what does dp[i] represent?
- **Transition**: How does dp[i] depend on previous dp values?
- **Base case**: dp[0], dp[1] — must be correct

## Problem Targets
- Climbing stairs (variationswith step sizes)
- House robber (can't rob adjacent houses)
- Coin change (minimum coins)
- Unbounded knapsack (any number of each item)
- Memoization with @lru_cache

## Linked Invariant
[[invariant-optimal-substructure]], [[invariant-overlapping-subproblems]]

## Template to Memorize
```python
# Memoization
@lru_cache(maxsize=None)
def dp(i):
    if i <= 1:
        return i
    return dp(i - 1) + dp(i - 2)

# Tabulation
dp = [0] * (n + 1)
dp[1] = 1
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
return dp[n]
```

## Status
- [ ] Climbing stairs
- [ ] House robber
- [ ] Coin change (minimum coins)
- [ ] Memoization with @lru_cache
- [ ] Tabulation (bottom-up)
- [ ] Space optimization (rolling array)
- [ ] 6-8 problems solved
