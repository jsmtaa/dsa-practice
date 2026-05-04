---
status: unlearned
day: 7
invariants:
  - invariant-state-space-search
---

# Tree Traversals

## Core Idea
Visit every node in a tree exactly once in a specific order. Three main types: inorder (left-root-right for BST), preorder (root-left-right), postorder (left-right-root). Can be recursive or iterative using a stack.

## When to Use
- Accessing nodes in a specific order (e.g., BST inorder gives sorted sequence)
- Building/modifying tree structure
- Finding properties: height, path sum, etc.
- Both recursive (cleaner) and iterative (stack-based) approaches useful

## Template Code
```python
# Recursive traversals
def inorder(root):
    result = []
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        result.append(node.val)
        traverse(node.right)
    traverse(root)
    return result

def preorder(root):
    result = []
    def traverse(node):
        if not node:
            return
        result.append(node.val)
        traverse(node.left)
        traverse(node.right)
    traverse(root)
    return result

# Iterative inorder using stack
def inorder_iterative(root):
    result = []
    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result
```

## Linked Invariants
- [[invariant-state-space-search]]

## Linked Problems
(Day 7: inorder/preorder/postorder, validate BST, tree path sum, etc.)

## Common Pitfalls
- Confusing the order: "in" = left-root-right, "pre" = root-left-right, "post" = left-right-root
- Iterative inorder: forgetting to process the node after popping (stack doesn't append to result)
- Not handling None nodes correctly (base case in recursion)
- Using wrong traversal for the problem (e.g., needing postorder to process children before parent)
