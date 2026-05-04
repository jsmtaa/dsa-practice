---
status: partial
day: 3
invariants:
  - invariant-monotonicity
---

# Sorting + Binary Search

## Core Idea
Sort the input to create a monotonic structure, then use binary search to find targets in O(log n). Also apply binary search on the *answer* space itself — guess a value and check if it's feasible.

## When to Use
- Finding a value in a sorted array
- Binary search on answer: "What's the minimum X where property P holds?"
- Merging two sorted arrays
- Counting occurrences of a value efficiently
- Competitive programming: sort + binary search pattern is ubiquitous

## Template Code
```python
import bisect

# Standard binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Using bisect
def find_first(arr, target):
    idx = bisect.bisect_left(arr, target)
    return idx if idx < len(arr) and arr[idx] == target else -1

# Binary search on answer
def min_days_to_eat_bananas(piles, h):
    def can_finish(speed):
        hours_needed = sum((pile + speed - 1) // speed for pile in piles)
        return hours_needed <= h
    
    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        if can_finish(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

## Linked Invariants
- [[invariant-monotonicity]]

## Linked Problems
(Day 3: search rotated array, find first/last occurrence, etc.)

## Common Pitfalls
- Not checking if array is sorted before binary search
- Off-by-one errors: `mid = (left + right) // 2` vs. integer overflow (less issue in Python)
- Confusing `bisect_left` vs. `bisect_right`
- Binary search on answer: not recognizing when the answer space is monotonic
- Missing edge cases: empty array, single element, duplicates
