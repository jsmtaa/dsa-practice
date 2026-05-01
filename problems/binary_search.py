"""
PROBLEM   : Binary Search (exploratory)
DIFFICULTY: easy
PATTERN   : binary search
TRIGGER   : sorted array, find target, O(log n)
INTUITION : Start at the middle. If target < mid move left; if target > mid move right.
            Halve the step size each iteration until the target is found.
"""

nums = [0,1,2,3,4,5,6,7,8]
n = i = steps = len(nums) # 9
target = 1
# this works for a sorted array

#
# start tayo sa gitna

steps //= 2
i = steps
while True:
    if nums[i] == target:
        print("Found!")
        break;
    elif nums[i] > target:
        # move left
        i -= steps // 2
        print("Move to the left")
    elif nums[i] < target:
        # move right
        i += steps // 2
        print("Move to the right")
    steps //= 2

print(i)