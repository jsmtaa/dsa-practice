---
status: unlearned
day: 14
invariants:
  - invariant-optimal-substructure
---

# Tree DP

## Core Idea
Apply DP on tree structures. Process children recursively, combine results at each node. Usually post-order traversal (process children before parent).

## When to Use
- Tree diameter
- Maximum path sum in tree
- House robber on tree
- Subtree problems
- Any optimization problem on a tree

## Template Code
```python
# Tree diameter (longest path between any two nodes)
def tree_diameter(root):
    def dfs(node):
        if not node:
            return 0, 0  # height, diameter
        left_h, left_d = dfs(node.left)
        right_h, right_d = dfs(node.right)
        height = max(left_h, right_h) + 1
        diameter = max(left_d, right_d, left_h + right_h)
        return height, diameter
    
    _, diameter = dfs(root)
    return diameter

# Maximum path sum in binary tree
def max_path_sum(root):
    max_sum = float('-inf')
    
    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0
        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))
        max_sum = max(max_sum, left + right + node.val)
        return max(left, right) + node.val
    
    dfs(root)
    return max_sum
```

## Linked Invariants
- [[invariant-optimal-substructure]]

## Linked Problems
(Day 14: tree diameter, max path sum, house robber on tree, etc.)

## Common Pitfalls
- Confusing post-order (children first) with pre-order (parent first)
- Not handling leaf nodes correctly (return appropriate base value)
- Off-by-one in height calculations
- Not using nonlocal for global result tracking
