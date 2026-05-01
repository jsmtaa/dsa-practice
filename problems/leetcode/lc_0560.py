"""
PROBLEM   : Subarray Sum Equals K
DIFFICULTY: medium
PATTERN   : prefix sum, hashing
TRIGGER   : count subarrays, sum equals k, negative numbers possible
INTUITION : For each prefix sum p, if (p - k) has been seen before, there is a subarray ending
            here with sum k. Store prefix sums in a hashmap with their occurrence counts.
"""

nums = [0,0,0]
k = 0

seen = {0: 1}
count = 0
prefix = 0
for x in nums:
    prefix += x
    # since now (prefix) - earlier = k: prefix - k = earlier
    # pag nakita natin yung earlier, ibig sabihin pwede
    # tayo makacreate ng subarray equals k
    # when we get 0, it means from the start up to end, it resulted to K,
    # because k - k = 0, therefore prefix - k = 0
    need = prefix - k
    print(seen)
    if need in seen:
        count += seen[need]
    seen[prefix] = seen.get(prefix, 0) + 1

print(count)