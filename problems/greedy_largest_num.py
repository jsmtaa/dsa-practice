"""
PROBLEM   : Largest Sum of N Elements (greedy)
DIFFICULTY: easy
PATTERN   : greedy
TRIGGER   : select top-n elements, maximize sum, pick greedily
INTUITION : Greedily pick the largest available element n times. Their sum is the maximum
            possible, since any smaller element would only reduce the total.
"""

# select the n number of elements that results into the largest sum
# GREEDY each Step, not index (not always btw)
nums = [3, 4, -1, 2, -3, 1]
n = 4
total = 0
for i in range(n):
    largest = max(nums)
    total += largest
    nums.remove(largest)

print(total)
