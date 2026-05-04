---
status: partial
day: 10
invariants:
  - invariant-optimal-substructure
  - invariant-overlapping-subproblems
---

# Dynamic Programming (1D)

## Core Idea
Extend intro DP to problems where the state is a single dimension (e.g., dp[i] represents the best solution up to index i). Build the DP table iteratively, where each entry depends only on previous entries.

## When to Use
- Climbing stairs, house robber, max subarray sum
- Longest increasing subsequence (LIS)
- Coin change, unbounded knapsack
- Jump game, word break
- Any problem where the current state depends on a few previous states

## Template Code
```python
# House robber: max sum without adjacent elements
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp[-1]

# Coin change: minimum coins
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
```

## Linked Invariants
- [[invariant-optimal-substructure]]
- [[invariant-overlapping-subproblems]]

## Linked Problems
(Day 10: climbing stairs, house robber, coin change variants)

## Common Pitfalls
- DP table size off by one (need `n+1` if indexing from 1)
- Initial state dp[0] set incorrectly (base case)
- Iteration order matters: forward vs. backward (unbounded vs. 0/1 knapsack)
- Confusing the transition: which previous states feed into current?
- Space optimization: can you reduce to O(1) using rolling variables?
