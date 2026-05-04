---
status: core
---

# Linked List

## Definition
Linear collection of nodes, each containing data and a reference to the next node. Unlike arrays, no random access but efficient insertion/deletion at known position.

## Operations & Complexity
- Access by index: O(n)
- Insert/delete at head: O(1)
- Insert/delete at position (if known): O(1)
- Insert/delete at tail: O(n) unless tail pointer maintained
- Search: O(n)

## Python Idiom
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create list: 1 -> 2 -> 3
head = ListNode(1, ListNode(2, ListNode(3)))

# Traverse
curr = head
while curr:
    print(curr.val)
    curr = curr.next
```

## Linked Techniques
- [[linked-lists|Linked Lists]]
- [[two-pointers|Two Pointers]]

## When to Use
- Efficient insertion/deletion at known position
- No need for random access
- Memory is fragmented
