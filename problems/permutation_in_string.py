"""
PROBLEM   : Permutation in String (LC #567)
DIFFICULTY: medium
PATTERN   : sliding window (fixed), frequency matching
TRIGGER   : permutation, anagram substring, fixed window of len(s1)
INTUITION : Build frequency arrays for s1 and the first window of s2. Slide the window;
            if both frequency arrays match at any point, s1's permutation exists in s2.
"""

def checkInclusion(s1, s2):
  """
  :type s1: str
  :type s2: str
  :rtype: bool
  """
  if len(s1) > len(s2):
    return False
  s1_freq = [0] * 26
  s2_freq = [0] * 26
  
  k = len(s1)
  
  def char_index(c):
    return ord(c) - ord('a')
  
  for c in s1:
    s1_freq[char_index(c)] += 1
  
  for c in s2[:k]:
    s2_freq[char_index(c)] += 1

  if s1_freq == s2_freq:
    return True
  
  
  for r in range(k, len(s2)):
    l = r - k # pos of the current right - fixed window size
    
    s2_freq[char_index(s2[r])] += 1
    s2_freq[char_index(s2[l])] -= 1
    if s1_freq == s2_freq:
      return True
    
  
  return False

print(checkInclusion("ab", "aab"))