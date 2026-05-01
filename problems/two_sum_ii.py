"""
PROBLEM   : Contains Duplicate (LC #217)
DIFFICULTY: easy
PATTERN   : hashing
TRIGGER   : duplicate values, O(n), seen before
INTUITION : A set collapses duplicates. If the set length differs from the array length,
            a duplicate exists.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)
        
        

def main():
    nums = [1,2,3,1]
    print(Solution().containsDuplicate(nums))

if __name__ == "__main__":
    main()
        
        