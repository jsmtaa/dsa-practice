# MOC — Invariants

Core invariants that unlock competitive programming patterns. Each invariant represents a fundamental property that techniques exploit.

## All Invariants

1. **[[invariant-monotonicity]]** — Values change predictably (always up/down); search space can be eliminated rapidly
2. **[[invariant-optimal-substructure]]** — Optimal solution built from optimal subproblem solutions; enables DP
3. **[[invariant-overlapping-subproblems]]** — Same subproblems solved many times; memoization prevents redundant work
4. **[[invariant-state-space-search]]** — Solution found by traversing states; DFS, BFS, backtracking explore the space
5. **[[invariant-range-queries]]** — Aggregate data (sum, min, max) over intervals; preprocessing enables fast queries
6. **[[invariant-greedy-choice-property]]** — Local greedy choice leads to global optimum; no need for DP

---

## How to Use This MOC

- **For pattern learning**: Pick an invariant, see which techniques exploit it, solve problems
- **For problem solving**: Recognize which invariant the problem exhibits, then apply matching techniques
- **For recall review**: DFS/BFS traverse this graph starting from an invariant, then drill techniques and problems

Next: [[techniques]] to see techniques grouped by invariant
