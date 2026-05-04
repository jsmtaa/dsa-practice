---
status: core
related_techniques: 4
---

# State Space Search Invariant

## Definition
A problem has a state space when solutions can be explored by transitioning between states. Exhaustive or directed search through this space (via recursion, BFS, or DFS) finds a valid solution or proves none exists. The state encodes the current position in the problem.

## Recognition Signals
- "Explore all possibilities" or "find all paths"
- "Connected components" or "reachability"
- "Shortest path" in an unweighted graph (BFS hint)
- "Cycle detection" or "topological order"
- Permutations, combinations, subsets (backtracking)
- Maze or grid traversal problems
- "From X, can I reach Y?"

## Techniques That Exploit It
- [[recursion-backtracking|Recursion / Backtracking]]
- [[bfs|BFS]]
- [[dfs|DFS]]
- [[topological-sort|Topological Sort]]

## Common Failure Modes
- Not tracking visited states, leading to infinite loops or cycles
- Exploring the wrong state space (e.g., all numbers vs. reachable nodes)
- Confusing BFS (shortest unweighted path) with DFS (arbitrary traversal)
- **Mixing up stacks and queues**: BFS uses **queues**, DFS uses **stacks**
- Forgetting to prune branches early in backtracking (exponential blowup)
- State representation too complex, leading to memory/time explosion
