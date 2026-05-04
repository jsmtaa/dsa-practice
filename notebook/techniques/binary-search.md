---
status: partial
day: 3
invariants:
  - invariant-monotonicity
---

# Binary Search

## Core Idea
Exploit monotonicity to search in O(log n) by repeatedly eliminating half the search space. Works on sorted arrays and monotonic functions.

## When to Use
- Finding a target in a sorted array
- Binary search on answer: guess a value and check if feasible
- Finding first/last occurrence of a value
- Square root, nth root, median of sorted arrays

## Template Code
```python
# Standard binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Find first occurrence
def find_first(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Keep searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

# Binary search on answer
def koko_eating_bananas(piles, h):
    def can_finish(speed):
        hours = sum((pile + speed - 1) // speed for pile in piles)
        return hours <= h
    
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
(Day 3: search sorted array, first/last occurrence, binary search on answer, etc.)

## Common Pitfalls
- Off-by-one errors: `left <= right` vs. `left < right`
- Integer overflow: use `mid = left + (right - left) // 2`
- Not verifying array is sorted before using binary search
- Binary search on answer: forgetting to check feasibility function
