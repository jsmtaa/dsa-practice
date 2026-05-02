"""
PROBLEM   : Combination Sum
DIFFICULTY: medium
PATTERN   : backtracking
TRIGGER   : candidates reusable, sum to target, all combinations
INTUITION : At each index, either reuse the current candidate or advance to the next. Stop when
            the sum hits the target (collect) or exceeds it (prune).
"""


def combinationSum(candidates: list[int], target: int) -> list[list[int]]:

    result = []
    # Similar to the subset problem
    def backtrack(index, path):
        # Base case
        # First: We successfully got a valid sum
        if index > len(candidates):
            return
        elif sum(path) == target:
            result.append(path[:])
            return
        elif sum(path) > target:
            return

        path.append(candidates[index])
        backtrack(index, path) # We choose to extend the current candidate
        path.pop()

        if index < len(candidates) - 1:
            backtrack(index + 1, path) # We choose to move on to the next candidate

    backtrack(0, [])
    return result