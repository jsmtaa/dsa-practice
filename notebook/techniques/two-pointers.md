---
status: learned
day: 1
invariants:
  - invariant-monotonicity
---

# Two Pointers

## Core Idea
Use two indices (left and right) to traverse an array from opposite ends or at different speeds. When both pointers move toward each other or one chases the other, you can solve problems in O(n) time that would otherwise require O(n²) nested loops.

## When to Use
- Pair sum problems: "Find two numbers that sum to target"
- Container with most water: maximize area between two lines
- Sorted array operations
- Remove duplicates, partition problems
- Fast and slow pointers on linked lists (cycle detection, middle element)

## Template Code
```python
# Two pointers from opposite ends
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

# Fast and slow pointers
def find_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

## Linked Invariants
- [[invariant-monotonicity]]

## Linked Problems
(Examples from Day 1: pair sum, container with most water, longest substring without repeating)

## Common Pitfalls
- Forgetting that the array must be sorted for two pointers (left/right approach) to work
- Confusing pointer movement directions — not advancing when needed
- Off-by-one errors in boundary conditions
- Fast and slow pointers: forgetting to check for None in linked lists
