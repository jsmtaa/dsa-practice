---
status: core
---

# Tree

## Definition
Hierarchical data structure with a root node and edges connecting parent to child nodes. Binary tree has at most 2 children per node. BST (binary search tree) maintains sorted order.

## Operations & Complexity
- Insert (BST): O(log n) average, O(n) worst
- Search (BST): O(log n) average, O(n) worst
- Delete (BST): O(log n) average, O(n) worst
- Traversal (inorder, preorder, postorder): O(n)

## Python Idiom
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Create: binary tree with 1 as root, 2 and 3 as children
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Inorder traversal (BST gives sorted order)
def inorder(node):
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)
```

## Linked Techniques
- [[tree-traversals|Tree Traversals]]
- [[tree-dp|Tree DP]]
- [[lowest-common-ancestor|Lowest Common Ancestor]]
- [[bfs|BFS]]
- [[dfs|DFS]]

## When to Use
- Hierarchical data (org charts, filesystems)
- Binary search tree for sorted dynamic data
- Heaps for priority queues
- Expression trees for parsing
