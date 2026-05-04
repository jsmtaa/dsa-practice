---
status: partial
day: 7
invariants:
  - invariant-monotonicity
---

# Linked Lists

## Core Idea
Use pointer manipulation instead of index-based access. Inserting/removing at a known node position is O(1), but traversal is O(n). Fast and slow pointers enable cycle detection and finding middle elements.

## When to Use
- Inserting/deleting in the middle without array shifting
- Cycle detection in lists
- Reversing a list
- Merging sorted lists
- Finding the middle element (fast/slow pointers)

## Template Code
```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Reverse a linked list
def reverse(head):
    prev, curr = None, head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

# Find middle element
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Merge two sorted lists
def merge_sorted(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next
```

## Linked Invariants
- [[invariant-monotonicity]]

## Linked Problems
(Day 7: reverse linked list, cycle detection, merge sorted, etc.)

## Common Pitfalls
- Forgetting to save the next node before updating pointers
- Off-by-one errors in fast/slow pointer logic
- Not handling empty list or single-node edge cases
- Using extra space when the problem requires O(1)
- Confusing `.next = None` with proper list termination
