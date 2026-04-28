"""
PROBLEM   : Maximum Average Subarray I
DIFFICULTY: easy 
PATTERN   : sliding window, running sum
TRIGGER   : max sum, k
INTUITION : As the sum of the values increase, it's average values also increases. 
            Therefore, we just find the subarray with max sum with size k then return its average.
"""

def findMaxAverage(nums, k):
  curr = best = sum(nums[:k])
  l = 0
  for r in range(k, len(nums)):
      curr -= nums[l]
      l += 1
      curr += nums[r]
      best = max(best, curr)
  return best / float(k)