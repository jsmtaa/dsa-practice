"""
PROBLEM    : Minimum Size Subarray Sum
DIFFICULTY : easy 
PATTERN    : sliding window, running sum
TRIGGER    : 
"""

target = 7
nums = [2, 3, 1, 2, 4, 3]

best = float('inf')
for i in range(len(nums)):
  curr = 0
  for j in range(i, len(nums)):
    curr += nums[j]
    if curr >= target:
      best = min(best, j - i + 1)

print(best)