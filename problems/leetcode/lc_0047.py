"""
PROBLEM   : Permutations II
DIFFICULTY: medium
PATTERN   : backtracking
TRIGGER   : all permutations, may contain duplicates, unique results only
INTUITION : Sort so duplicates are adjacent, then use a used[] array. At each level, skip
            nums[i] when nums[i] == nums[i-1] and not used[i-1] — this enforces that we
            always pick the first copy of a value before the second, eliminating duplicate
            branches at the source.
"""

def permuteUnique(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    used = [False] * len(nums)
    path = []
    def backtrack():
        if len(path) == len(nums):
            res.append(path.copy())
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False
    
    backtrack()
    return res