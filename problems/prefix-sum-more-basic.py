"""
PROBLEM   : Count Subarrays with Sum K (prefix sum approach)
DIFFICULTY: medium
PATTERN   : prefix sum, hashing
TRIGGER   : count subarrays, sum equals k, negative numbers, O(n)
INTUITION : For each prefix sum p, if (p - k) has been seen before, there is a subarray
            ending here with sum k. Update seen before checking to handle index ordering.
"""

nums = [1, -1, 1, -1]
#       1,  0, 1,  0

# 1st count = [1] = 1
# 2nd count = [1, -1, 1] = 1
k = 1

seen = {0: 1}
count = 0
prefix = 0
for num in nums:
    if prefix - k in seen:
        count += seen[prefix - k]
    prefix += num
    seen[prefix] = seen.get(prefix, 0) + 1
    print(seen)

print(count)