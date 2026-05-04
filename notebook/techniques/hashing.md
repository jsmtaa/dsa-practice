---
status: unlearned
day: 2
invariants:
  - invariant-range-queries
---

# Hashing

## Core Idea
Use hash maps (dictionaries) to count frequencies, track visited elements, or build lookup tables. Enables O(1) average-case lookups and O(1) frequency updates in a single pass.

## When to Use
- Frequency counting: "does every element appear exactly once?"
- Subarray sum equals K: store prefix sums in a map
- Two sum: store complements
- Detecting duplicates or unique elements
- Building character/word frequency tables

## Template Code
```python
from collections import Counter, defaultdict

# Frequency counting
def frequency_map(arr):
    freq = Counter(arr)
    # or: freq = defaultdict(int); [freq[x] += 1 for x in arr]
    return freq

# Two sum with hashmap
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Subarray sum equals K
def subarray_sum(nums, k):
    prefix_sum = 0
    count = 0
    prefix_map = {0: 1}
    for num in nums:
        prefix_sum += num
        if prefix_sum - k in prefix_map:
            count += prefix_map[prefix_sum - k]
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
    return count
```

## Linked Invariants
- [[invariant-range-queries]]

## Linked Problems
(Day 2: two sum, subarray sum equals K, group anagrams, etc.)

## Common Pitfalls
- Hash collisions (rare in Python, but understanding them helps)
- Using unhashable types (list, dict) as keys
- Forgetting to initialize counters with `defaultdict` to avoid KeyError
- Not clearing or managing map state across multiple queries
- Assuming O(1) lookup always holds (it's average-case, worst-case is O(n))
