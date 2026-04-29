"""
PROBLEM   : Subarrays with K Different Integers
DIFFICULTY: Hard
PATTERN   : sliding window, frequency counting
TRIGGER   : at most K
INTUITION : Because we can get count of subarrays with AtMost(K), we can get exactly(K) by subtracting it 
            to the rest of counts from AtMost(K - 1).
"""

def subarraysWithKDistinct(nums, k):
  def AtMost(k):
    count = 0
    freq = {}
    l = 0
    for r in range(len(nums)):
      freq[nums[r]] = freq.get(nums[r], 0) + 1
      
      while len(freq) > k:
        freq[nums[l]] -= 1
        if freq[nums[l]] == 0:
          del freq[nums[l]]
        l += 1
      
      count += r - l + 1 # Counts the valid subarrays
    return count

  return AtMost(k) - AtMost(k - 1)