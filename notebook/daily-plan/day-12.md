---
status: unlearned
day: 12
topics: DP 2D Continued
target-problems: 6-8
---

# Day 12 — DP Part 2 Continued

See [[day-11|Daily Plan - Day 11]] for full goals.

## Focus Today
- Edit distance (Levenshtein): transform one string to another
- DP on grids: paths with constraints
- Knapsack variants

## Template
```python
# Edit distance
def editDistance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]
```

## Status
- [ ] Edit distance
- [ ] LCS (continued from Day 11)
- [ ] Grid path DP
- [ ] 6-8 problems solved
