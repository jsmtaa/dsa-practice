"""
PROBLEM   : Subsets
DIFFICULTY: medium
PATTERN   : backtracking
TRIGGER   : all subsets, power set, include or skip
INTUITION : At each element, split into two paths: one that takes it, one that doesn't. Follow
            both all the way to the end, collecting every result you land on.
"""

def subsets(nums: list[int]) -> list[list[int]]:
    result = []
    def backtrack(index, path):
        if index == len(nums):
            result.append(path[:])
            return
        
        path.append(nums[index])
        backtrack(index + 1, path)
        path.pop()

        backtrack(index + 1, path)
    
    backtrack(0, [])
    return result