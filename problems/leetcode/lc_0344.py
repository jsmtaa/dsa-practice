"""
PROBLEM   : Reverse String
DIFFICULTY: easy
PATTERN   : two pointers
TRIGGER   : reverse in-place, array of characters, no extra space
INTUITION : Swap the outermost characters and advance both pointers inward until they meet.
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s.reverse()