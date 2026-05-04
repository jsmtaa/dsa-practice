---
status: unlearned
day: 17
invariants:
  - invariant-optimal-substructure
---

# Bitmask DP

## Core Idea
Use bitmask to represent a subset of elements (each bit = whether element is in subset). Enables DP on subsets where the state is a bitmask instead of traditional array indices.

## When to Use
- Traveling salesman problem (TSP)
- Subset enumeration problems
- Steiner tree on small graphs
- Covering problems (set cover, exact cover)

## Template Code
```python
# TSP with bitmask DP
def traveling_salesman(dist, n):
    INF = float('inf')
    dp = [[INF] * n for _ in range(1 << n)]
    
    # Base case: start at node 0
    dp[1][0] = 0
    
    # Iterate over all subsets
    for mask in range(1 << n):
        for last in range(n):
            if dp[mask][last] == INF:
                continue
            # Try extending to unvisited nodes
            for next_node in range(n):
                if (mask & (1 << next_node)) == 0:  # next_node not visited
                    new_mask = mask | (1 << next_node)
                    dp[new_mask][next_node] = min(
                        dp[new_mask][next_node],
                        dp[mask][last] + dist[last][next_node]
                    )
    
    # Find minimum cost to visit all nodes and return to start
    full_mask = (1 << n) - 1
    ans = INF
    for last in range(1, n):
        ans = min(ans, dp[full_mask][last] + dist[last][0])
    return ans

# Bit manipulation tricks
# (mask & (1 << i)) != 0  # Check if i-th bit is set
# mask | (1 << i)  # Set i-th bit
# mask & ~(1 << i)  # Unset i-th bit
# 1 << n  # 2^n (all subsets)
```

## Linked Invariants
- [[invariant-optimal-substructure]]

## Linked Problems
(Day 17: TSP, subset enumeration, steiner tree, etc.)

## Common Pitfalls
- Bitmask size: (1 << n) subsets, so n <= 20 for practical DP
- Off-by-one in bit indexing
- Confusing (mask & (1 << i)) with (mask >> i) & 1
- State explosion: large n leads to TLE and MLE
