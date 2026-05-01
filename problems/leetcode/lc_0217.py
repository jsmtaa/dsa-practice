"""
PROBLEM   : Contains Duplicate
DIFFICULTY: easy
PATTERN   : hashing
TRIGGER   : duplicate values, seen before, O(n)
INTUITION : A set collapses duplicates. If the set is smaller than the original array, a
            duplicate exists.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Having no duplicates in set vs len would produce the same len. Hence:
        return len(nums) != len(set(nums))