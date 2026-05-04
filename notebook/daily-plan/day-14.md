---
status: unlearned
day: 14
topics: Tree DP, LCA
target-problems: 6-8
---

# Day 14 — Trees: Advanced (Tree DP + LCA)

## Goals
Master optimization on tree structures and lowest common ancestor queries.

## Techniques to Practice
- [[tree-dp|Tree DP]] — Post-order traversal; combine children results
- [[lowest-common-ancestor|Lowest Common Ancestor]] — Find deepest shared ancestor

## Key Insights
- **Tree DP**: Process leaves first, combine results upward
- **LCA**: Simple recursion is O(n) per query; binary lifting is O(log n) after O(n log n) preprocessing

## Problem Targets
- Tree diameter (longest path between any two nodes)
- Maximum path sum in tree
- LCA of two nodes
- Distance between two nodes

## Template: Tree Diameter
```python
def treeDiameter(root):
    def dfs(node):
        if not node:
            return 0, 0  # height, diameter
        lh, ld = dfs(node.left)
        rh, rd = dfs(node.right)
        height = max(lh, rh) + 1
        diameter = max(ld, rd, lh + rh)
        return height, diameter
    _, diameter = dfs(root)
    return diameter
```

## Status
- [ ] Tree diameter
- [ ] Maximum path sum (binary tree)
- [ ] LCA (simple recursion)
- [ ] Binary lifting (advanced)
- [ ] 6-8 problems solved
