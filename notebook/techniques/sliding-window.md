---
status: learned
day: 1
invariants:
  - invariant-monotonicity
---

# Sliding Window

## Core Idea
Maintain a contiguous window of elements and slide it across the array, expanding or contracting based on an invariant. This upgrades two pointers by allowing dynamic window size and is O(n) instead of O(n²).

## When to Use
- "Longest/shortest substring with property X"
- "Maximum sum of contiguous subarray of any size"
- "At most K distinct characters" or similar constraints
- Fixed-size window: "maximum sum of K consecutive elements"

## Template Code
```python
# Variable window
def longest_without_repeating(s):
    char_index = {}
    max_len = 0
    left = 0
    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1
        char_index[s[right]] = right
        max_len = max(max_len, right - left + 1)
    return max_len

# Fixed window
def max_sum_k_consecutive(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    return max_sum
```

## Linked Invariants
- [[invariant-monotonicity]]

## Linked Problems
(Day 1: longest substring without repeating chars, max sum of K consecutive, etc.)

## Common Pitfalls
- Not understanding when to expand vs. contract the window
- Forgetting to update the window state (e.g., character frequency map)
- Using wrong data structure for tracking window state
- Not handling edge cases (empty window, single element, all duplicates)
