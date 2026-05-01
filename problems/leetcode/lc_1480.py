"""
PROBLEM   : Running Sum of 1D Array
DIFFICULTY: easy
PATTERN   : prefix sum
TRIGGER   : running sum, cumulative sum, 1D array, in-place
INTUITION : At each index, the running sum equals the previous running sum plus the current
            element. One pass, O(1) extra space if done in-place.
"""

nums = [12,345,2,6,7896]


print(len([1 for x in nums if x % 2 == 0]))

nums = [1,2,3,4]

res = [0] * len(nums)
ans = 0
for i in range(len(nums)):
    ans += nums[i]
    res[i] = ans
print(res)