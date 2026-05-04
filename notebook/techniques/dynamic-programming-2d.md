---
status: unlearned
day: 11
invariants:
  - invariant-optimal-substructure
  - invariant-overlapping-subproblems
---

# Dynamic Programming (2D)

## Core Idea
Extend 1D DP to two dimensions. Common patterns: LCS (Longest Common Subsequence), edit distance, knapsack variants, grid path problems. The state usually represents a boundary or subproblem range.

## When to Use
- Edit distance (Levenshtein distance)
- Longest common subsequence
- 0/1 knapsack and variants
- Maximum path sum in a grid
- Distinct ways to reach a cell

## Template Code
```python
# Edit distance
def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]

# Longest common subsequence
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
```

## Linked Invariants
- [[invariant-optimal-substructure]]
- [[invariant-overlapping-subproblems]]

## Linked Problems
(Day 11-12: edit distance, LCS, knapsack, grid paths, etc.)

## Common Pitfalls
- DP table size off by one (need m+1 x n+1 for m and n inputs)
- Incorrect base case initialization
- Off-by-one in string indices (dp[i] corresponds to s[i-1])
- Confusing recurrence: when to take diagonal vs. adjacent cells
- Space optimization: can reduce to O(n) using rolling arrays
