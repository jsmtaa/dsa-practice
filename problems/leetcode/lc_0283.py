"""
PROBLEM   : Move Zeroes
DIFFICULTY: easy
PATTERN   : two pointers
TRIGGER   : move zeroes to end, maintain relative order, in-place
INTUITION : `write` is an anchor that stays still while `read` scans forward. Once `read` finds a non-zero
            value, swap it with the anchor and shift the anchor right by 1. This pushes all non-zero values
            to the front in order while zeroes naturally drift to the end.
"""

def moveZeroes(nums):
  l = 0
  for r in range(len(nums)):
    if nums[r] != 0:
      nums[r], nums[l] = nums[l], nums[r]
      l += 1