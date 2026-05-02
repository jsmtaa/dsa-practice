"""
PROBLEM   : Permutations
DIFFICULTY: medium
PATTERN   : backtracking
TRIGGER   : all permutations, distinct integers, no repeats
INTUITION : Try placing every number at the current slot — but skip any that are already in the
            path. Once all slots are filled, you have a permutation.
"""

def permute(nums: list[int]) -> list[list[int]]:
    result = []
    def backtrack(path):
        # Base case
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        # Permute
        for x in nums:
            # Constraint, x cannot repeat
            if x in path:
                continue
            path.append(x)
            backtrack(path)
            path.pop()
    
    backtrack([])
    return result