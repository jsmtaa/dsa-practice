"""
PROBLEM   : Intersection of Two Arrays
DIFFICULTY: easy
PATTERN   : hashing, sets
TRIGGER   : intersection, unique elements, two arrays, common values
INTUITION : Convert both arrays to sets and return their intersection — only elements present
            in both sets, without duplicates.
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = []
        
        for num in nums1:
            if num in nums2:
                if num not in intersection:
                    intersection.append(num)

        return intersection