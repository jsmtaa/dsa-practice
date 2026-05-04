---
status: core
related_techniques: 3
---

# Optimal Substructure Invariant

## Definition
A problem has optimal substructure when the optimal solution to the whole problem can be constructed from optimal solutions to its subproblems. This means solving smaller versions of the same problem and combining those solutions yields the best answer.

## Recognition Signals
- "Maximum/minimum sum of a subarray/subset"
- "Longest sequence with property X"
- "How many ways to do Y" (counting problem)
- "Find the best arrangement"
- Problem can be broken into overlapping or independent subproblems
- "House robber" or "coin change" style problems

## Techniques That Exploit It
- [[dynamic-programming-1d|Dynamic Programming (1D)]]
- [[dynamic-programming-2d|Dynamic Programming (2D)]]
- [[tree-dp|Tree DP]]
- [[recursion-backtracking|Recursion / Backtracking]]

## Common Failure Modes
- Assuming every problem has optimal substructure (some are greedy)
- Not correctly defining the subproblem state — choosing wrong variables
- Forgetting the base case, leading to infinite recursion
- Double-counting or missing valid subproblems in DP table
- Confusing "substructure" with "overlapping subproblems" (both exist but are distinct concepts)
