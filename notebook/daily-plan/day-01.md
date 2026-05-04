---
status: unlearned
day: 1
topics: Two Pointers, Sliding Window
target-problems: 8-10 Easy/Medium
---

# Day 01 — Two Pointers + Sliding Window

## Goals
Rebuild these core patterns you already learned. Re-learning is 3x faster than first-time learning.

## Techniques to Practice
- [[two-pointers|Two Pointers]] — Use when traversing an array to find two values
- [[sliding-window|Sliding Window]] — Expand/shrink a window based on an invariant; upgrade to two pointers

## Core Insights
- **Two Pointers**: When you need to find a pair in a sorted array, start from opposite ends and move inward
- **Sliding Window**: Maintain a dynamic window; expand when condition allows, shrink when needed

## Problem Targets
- Fixed window: maximum sum of K consecutive elements
- Variable window: longest substring without repeating characters
- Two pointers: pair sum, container with most water

## Linked Invariant
[[invariant-monotonicity]]

## Template to Memorize
```python
# Two pointers
left, right = 0, len(arr) - 1
while left < right:
    if condition:
        left += 1
    else:
        right -= 1

# Sliding window
left = 0
for right in range(len(arr)):
    # Update window state
    while window_invalid:
        left += 1
    # Process window
```

## Status
- [ ] Fixed window: max K sum
- [ ] Variable window: longest without repeating
- [ ] Two pointers: pair sum
- [ ] Two pointers: container with most water
- [ ] 8-10 problems solved
