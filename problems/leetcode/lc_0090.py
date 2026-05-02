"""
PROBLEM   : Subsets II
DIFFICULTY: medium
PATTERN   : backtracking
TRIGGER   : all subsets, may contain duplicates, unique subsets only
INTUITION : Use the include/exclude binary split from Subsets, but on the exclude branch
            skip past all duplicates of the current element — so two "skip" branches at
            the same depth never start with the same value.
"""

def subsetsWithDup(nums: list[int]) -> list[list[int]]:
    nums.sort()
    # Duplicates matter not on depth, but current path
    # Two choices: Choose or not choose

    res, path = [], []
    def backtrack(index, path):
        # Base case
        if index == len(nums):
            res.append(path.copy())
            return

        # Constraints
        
        path.append(nums[index])
        # Choose
        backtrack(index + 1, path)
        path.pop()

        next_index = index + 1
        # Not choose
        while next_index < len(nums) and nums[next_index] == nums[index]:
            next_index += 1
        
        backtrack(next_index, path)

    backtrack(0, [])
    return res