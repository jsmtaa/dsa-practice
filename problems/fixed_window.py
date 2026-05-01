"""
PROBLEM   : Maximum Sum Subarray of Size K
DIFFICULTY: easy
PATTERN   : sliding window (fixed)
TRIGGER   : maximum sum, fixed window size k, contiguous subarray
INTUITION : Slide a window of size k across the array. Compute the sum for each window
            position and track the maximum.
"""

l = 0
k = 3

nums = [2,1,5,1,3,2]
max_sum = 0
for r in range(k,len(nums)+1):
    print(nums[l:r])
    s = sum(nums[l:r])
    if s > max_sum:
        max_sum = s
    l += 1

print(max_sum)