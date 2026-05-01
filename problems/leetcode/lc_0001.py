"""
PROBLEM   : Two Sum
DIFFICULTY: easy
PATTERN   : hashing
TRIGGER   : two numbers summing to target, return indices, O(n)
INTUITION : For each number, compute its complement (target - x). If the complement is already
            in the hashmap, we found the pair. Otherwise store x's index for future lookups.
"""

nums = [2, 7, 13, 15]
target = 20
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])


seen = {}
for i, x in enumerate(nums):
    cp = target - x
    if cp in seen:
        print([seen[cp], i])
    seen[x] = i