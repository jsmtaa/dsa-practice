"""
PROBLEM   : Prefix Sum Range Queries (1D)
DIFFICULTY: easy
PATTERN   : prefix sum
TRIGGER   : range sum queries, O(1) query after O(n) build, cumulative sum
INTUITION : Build prefix[i] = sum of nums[0..i]. Answer range [l, r] as
            prefix[r] - prefix[l-1] in O(1).
"""

nums = [1,2,3,4,5]
prefix = [0] * len(nums)

prefix[0] = nums[0]
for i in range(1, len(nums)):
    prefix[i] = nums[i] + prefix[i-1]

query = [
    (1, 3),
    (3, 4),
    (2, 3),
    (0, 0)
]

for q in query:
    print(prefix[q[1]] - prefix[q[0] - 1])