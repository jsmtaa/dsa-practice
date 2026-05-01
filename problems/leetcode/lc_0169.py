"""
PROBLEM   : Majority Element
DIFFICULTY: easy
PATTERN   : Boyer-Moore voting, hashing
TRIGGER   : majority element, appears more than n/2 times
INTUITION : The majority element cancels all others. Keep a candidate and a count: increment
            on a match, decrement on a mismatch, reset candidate when count reaches zero.
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = set(nums)
        m = 0
        for num in new:
            n = nums.count(num)
            if n > nums.count[m]:
                m
        
        return majority


nums = [0,0,0,1,1,2]
sol = Solution().majorityElement(nums)
print(set(nums))
print(sol)