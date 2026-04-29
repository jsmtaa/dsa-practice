"""
PROBLEM    : Minimum Size Subarray Sum
DIFFICULTY : easy 
PATTERN    : sliding window, running sum
TRIGGER    : at least K
"""

def minSubArrayLen(target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """ 
    l = 0
    best = float('inf')
    curr = 0
    for r in range(len(nums)):
        curr += nums[r]

        while curr >= target:
            best = min(best, r - l + 1)
            curr -= nums[l]
            l += 1
        
    return 0 if best == float('inf') else best