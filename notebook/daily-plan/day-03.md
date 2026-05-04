---
status: partial
day: 3
topics: Sorting, Binary Search
target-problems: 8-10
---

# Day 03 — Sorting + Binary Search

## Goals
Master fast lookup and "binary search on answer" trick for competitive programming.

## Techniques to Practice
- [[sorting-binary-search|Sorting + Binary Search]] — Sort then binary search, or search on answer space
- [[binary-search|Binary Search]] — O(log n) search in sorted arrays and monotonic functions

## Core Insights
- **Standard binary search**: Works on sorted arrays; watch for off-by-one
- **Binary search on answer**: Guess a value, check if feasible, binary search the feasibility space
- **Bisect module**: Python's `bisect_left`, `bisect_right`, `insort` are competition gold

## Problem Targets
- Find value in sorted array (standard binary search)
- Find first/last occurrence
- Binary search on answer: minimum time to eat bananas, capacity to ship packages
- Rotated sorted array

## Linked Invariant
[[invariant-monotonicity]]

## Template to Memorize
```python
# Standard binary search
left, right = 0, len(arr) - 1
while left <= right:
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return -1

# Binary search on answer
left, right = 1, max_possible
while left < right:
    mid = (left + right) // 2
    if can_achieve(mid):
        right = mid
    else:
        left = mid + 1
return left
```

## Status
- [ ] Standard binary search: find value
- [ ] Find first/last occurrence
- [ ] Binary search on answer (1 problem)
- [ ] Rotated sorted array search
- [ ] 8-10 problems solved
