"""
PROBLEM   : Product of Array Except Self
DIFFICULTY: medium
PATTERN   : prefix/suffix product
TRIGGER   : product except self, no division, O(n)
INTUITION : For each index, the answer is (prefix product of everything left) × (suffix product
            of everything right). Two passes: left-to-right for prefix, right-to-left for suffix.
"""

nums = [1,2,3,4 ]
#pre = [1,2,6,24]
# [1] * [3, 4]
# [1, 2] * [4]
# [1, 2, 3]

# [1, 2, 6, 24]
total = 1
for x in nums:
    total *= x

print(total)
products = [0] * len(nums)

for i in range(len(nums)):
    products[i] = total / int(nums[i])

print(products)