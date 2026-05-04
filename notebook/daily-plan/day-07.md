---
status: partial
day: 7
topics: Linked Lists, Tree Traversals
target-problems: 6-8
---

# Day 07 — Linked Lists + Basic Trees

## Goals
Master pointer manipulation and tree traversal patterns (recursive + iterative).

## Techniques to Practice
- [[linked-lists|Linked Lists]] — O(1) insertion/deletion at known position; no random access
- [[tree-traversals|Tree Traversals]] — Inorder, preorder, postorder (both recursive and iterative)

## Core Insights
- **Linked List**: Save next pointer before updating links
- **Fast/slow pointers**: Slow moves 1, fast moves 2; useful for cycle detection and finding middle
- **Tree order**: IN-order (left-root-right), PRE-order (root-left-right), POST-order (left-right-root)
- **Iterative inorder**: Use stack; process nodes after popping

## Problem Targets
- Reverse linked list
- Cycle detection (fast/slow pointers)
- Merge two sorted lists
- Tree inorder/preorder/postorder traversals
- Validate BST (inorder gives sorted)

## Linked Invariant
[[invariant-state-space-search]] for traversals, [[invariant-monotonicity]] for linked lists

## Template to Memorize
```python
# Reverse linked list
prev, curr = None, head
while curr:
    next_temp = curr.next
    curr.next = prev
    prev = curr
    curr = next_temp
return prev

# Iterative inorder
stack, curr = [], root
while curr or stack:
    while curr:
        stack.append(curr)
        curr = curr.left
    curr = stack.pop()
    result.append(curr.val)
    curr = curr.right
```

## Status
- [ ] Reverse linked list
- [ ] Cycle detection (fast/slow)
- [ ] Find middle of linked list
- [ ] Merge sorted lists
- [ ] Tree traversals (recursive)
- [ ] Tree traversals (iterative)
- [ ] 6-8 problems solved
