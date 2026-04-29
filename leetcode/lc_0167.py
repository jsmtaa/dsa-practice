"""
PROBLEM   : Two Sum II: Input Array is Sorted
DIFFICULTY: Medium
PATTERN   : two pointers
TRIGGER   : sorted array, find pair summing to target
INTUITION : Pairing nums[l] (smallest) with nums[r] (largest) gives full information each step —
            if sum is too high, nums[r] is dead (no smaller partner can save it); if too low,
            nums[l] is dead (no larger partner can save it). Each move eliminates one index for good.
"""

def twoSum(nums: list[int], target: int) -> list[int]:
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return [l + 1, r + 1]
        elif s > target:
            r -= 1
        else:
            l += 1
