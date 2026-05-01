"""
PROBLEM   : Jump Game II
DIFFICULTY: medium
PATTERN   : greedy
TRIGGER   : minimum jumps, reach last index, farthest reachable
INTUITION : Track the farthest index reachable from the current jump zone. When you step past
            the zone boundary, take another jump and expand the zone. Count jumps taken.
"""

nums = [2, 3, 1, 1, 4]
target = len(nums) - 1 # last index

farthest = 0
for i in range(len(nums)):
    #print(i + nums[i])
    if i + nums[i] >= target:
        # print("You reached with: i =", i, f"because {i=} + {nums[i]=} = {farthest}")
        print(f"Possible: {i=} + {nums[i]=} = {i + nums[i]}")
print()
