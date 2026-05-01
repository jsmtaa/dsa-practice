"""
PROBLEM   : Two Sum (LC #1, exploratory)
DIFFICULTY: easy
PATTERN   : hashing
TRIGGER   : two numbers summing to target, return indices, O(n)
INTUITION : For each number, check if its complement (target - x) is already in the
            hashmap. If yes, return the pair's indices; otherwise, store the index.
"""

seen = {}
target = 0
nums = []

for i, x in enumerate(nums):
  cp = target - x
  if cp in seen:
    print([seen[cp], i])
  seen[x] = i