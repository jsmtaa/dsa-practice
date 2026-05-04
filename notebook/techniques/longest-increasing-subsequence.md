---
status: unlearned
day: 11
invariants:
  - invariant-optimal-substructure
  - invariant-monotonicity
---

# Longest Increasing Subsequence (LIS)

## Core Idea
Find the longest subsequence (not necessarily contiguous) where elements are strictly increasing. O(n²) DP is straightforward; O(n log n) with binary search and `bisect` is the competitive programming trick.

## When to Use
- Longest increasing subsequence (obviously)
- Longest decreasing, non-decreasing variants
- Patience sorting problems
- Building increasing sequence problems

## Template Code
```python
from bisect import bisect_left

# O(n^2) DP approach
def lis_dp(arr):
    if not arr:
        return 0
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# O(n log n) approach with bisect
def lis_binary_search(arr):
    tails = []  # tails[i] = smallest tail of all increasing sequences of length i+1
    for num in arr:
        idx = bisect_left(tails, num)
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num
    return len(tails)

# Reconstruct the actual LIS
def lis_reconstruct(arr):
    n = len(arr)
    dp = [1] * n
    parent = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
    max_length = max(dp)
    max_idx = dp.index(max_length)
    result = []
    while max_idx != -1:
        result.append(arr[max_idx])
        max_idx = parent[max_idx]
    return result[::-1]
```

## Linked Invariants
- [[invariant-optimal-substructure]]
- [[invariant-monotonicity]]

## Linked Problems
(Day 11: LIS variants, Russian doll envelopes, patience sorting, etc.)

## Common Pitfalls
- Confusing subsequence (non-contiguous) with subarray (contiguous)
- O(n log n) approach: misunderstanding what tails array represents
- Strict vs. non-strict increasing (< vs. <=)
- Reconstruction: forgetting parent pointers if needed
