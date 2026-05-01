"""
PROBLEM   : Jump Game (LC #55)
DIFFICULTY: medium
PATTERN   : greedy
TRIGGER   : can reach last index, jump lengths, reachability
INTUITION : Track the farthest index reachable at each step. Update farthest with
            max(farthest, i + nums[i]). If farthest ever reaches the target, return True.
"""

def main():
    nums = [3,2,1,0,4]
    target = 4
    print(jump_game(nums, target))

def jump_game(nums, target):
    farthest = 0
    for i in range(len(nums)):
        if farthest == target:
            return True
        farthest = max(i + nums[i], farthest)
    return False

main()