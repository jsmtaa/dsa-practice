---
status: unlearned
day: 17
topics: Bitmask DP, Combinatorics
target-problems: 6-8 (Hard/Extreme)
---

# Day 17 — Bitmask DP + Combinatorics

## Goals
Master subset enumeration and combinatorial counting.

## Techniques to Practice
- [[bitmask-dp|Bitmask DP]] — Use bitmask to represent subset; DP on subsets
- [[combinatorics|Combinatorics]] — Count arrangements using C(n, k) and modular arithmetic

## Key Insights
- **Bitmask DP**: n ≤ 20 (2^20 = 1M subsets); TSP, steiner tree
- **Combinatorics**: Use math.comb() for C(n, k); modular arithmetic for large answers
- **Fermat's Little Theorem**: a^(-1) ≡ a^(p-2) (mod p) for prime p

## Problem Targets
- Traveling salesman (TSP) with bitmask DP
- Subset enumeration problems
- Counting problems with large answers (use modulo)
- Catalan numbers, factorials mod p

## Template: TSP Bitmask DP
```python
def tsp(dist, n):
    INF = float('inf')
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0
    for mask in range(1 << n):
        for last in range(n):
            if dp[mask][last] == INF:
                continue
            for next_node in range(n):
                if (mask & (1 << next_node)) == 0:
                    new_mask = mask | (1 << next_node)
                    dp[new_mask][next_node] = min(
                        dp[new_mask][next_node],
                        dp[mask][last] + dist[last][next_node]
                    )
    return min(dp[(1 << n) - 1]) + dist[...][0]
```

## Status
- [ ] Bitmask DP: subset enumeration
- [ ] TSP with bitmask
- [ ] Combinatorics: C(n, k) with math.comb
- [ ] Modular arithmetic for large answers
- [ ] 6-8 problems solved
