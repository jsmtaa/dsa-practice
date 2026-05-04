---
status: core
related_techniques: 1
---

# Greedy Choice Property Invariant

## Definition
A greedy choice property exists when making the locally optimal choice at each step leads to a globally optimal solution. No need to explore alternatives or use dynamic programming — commit to the best available option now.

## Recognition Signals
- "Always choose X because it's best now" and this yields global optimum
- Activity selection, interval scheduling, meeting room problems
- "Maximize the count of non-overlapping events"
- Huffman coding or similar construction problems
- Problem feels solvable by sorting + single pass
- "Does taking the locally best choice ruin anything later?" (if answer is no, greedy works)

## Techniques That Exploit It
- [[greedy-algorithms|Greedy Algorithms]]

## Common Failure Modes
- Greedy *looks* right but doesn't guarantee global optimum (e.g., change-making with arbitrary denominations)
- Not proving that greedy choice property actually holds
- Wrong sorting order (ascending vs. descending)
- Confusing greedy with other paradigms: some hard problems look greedy but need DP
- Not handling tie-breaking or edge cases in the greedy criterion
