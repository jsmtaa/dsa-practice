---
status: unlearned
day: 14
invariants:
  - invariant-optimal-substructure
---

# Lowest Common Ancestor (LCA)

## Core Idea
Find the deepest node that is an ancestor to both given nodes. Simple recursion works for trees; binary lifting enables fast queries on trees with many LCA requests.

## When to Use
- Finding LCA of two nodes
- Distance between two nodes
- Multiple LCA queries (binary lifting speeds them up)

## Template Code
```python
# Simple recursion (O(n) per query)
def lca(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root
    return left or right

# Binary lifting (O(log n) per query after O(n log n) preprocessing)
def lca_binary_lifting(root, p, q):
    MAX_LOG = 20
    parent = [[None] * MAX_LOG]
    depth = [0]
    
    def dfs(node, par, d):
        if not node:
            return
        parent[node] = [None] * MAX_LOG
        parent[node][0] = par
        depth[node] = d
        for i in range(1, MAX_LOG):
            if parent[node][i - 1]:
                parent[node][i] = parent[parent[node][i - 1]][i - 1]
        dfs(node.left, node, d + 1)
        dfs(node.right, node, d + 1)
    
    dfs(root, None, 0)
    
    if depth[p] < depth[q]:
        p, q = q, p
    
    diff = depth[p] - depth[q]
    for i in range(MAX_LOG):
        if (diff >> i) & 1:
            p = parent[p][i]
    
    if p == q:
        return p
    for i in range(MAX_LOG - 1, -1, -1):
        if parent[p][i] != parent[q][i]:
            p = parent[p][i]
            q = parent[q][i]
    
    return parent[p][0]
```

## Linked Invariants
- [[invariant-optimal-substructure]]

## Linked Problems
(Day 14: LCA queries, distance between nodes, etc.)

## Common Pitfalls
- Forgetting to handle the case where one node is ancestor of the other
- Binary lifting: MAX_LOG too small for large trees
- Using uninitialized parent arrays
