# Subarrays with K Different Integers;

# Intuition: at exactly K. Which is basically AtMostK - AtMostK - 1
def subarraysWithKDistinct(nums, k):
  """
  :type nums: List[int]
  :type k: int
  :rtype: int
  """
          
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
        
      count += r - l + 1
    return count

  return AtMost(k) - AtMost(k - 1)

print(subarraysWithKDistinct([1,2,1,2,3], 2))