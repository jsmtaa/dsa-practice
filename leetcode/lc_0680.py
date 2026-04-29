"""
PROBLEM   : Valid Palindrome II
DIFFICULTY: easy
PATTERN   : two pointers
TRIGGER   : palindrome, delete at most one character
INTUITION : Same squeeze as lc_0125. On a mismatch, try skipping either character by checking the
            inner window without it. If either sub-window is a palindrome, one deletion is enough.
MISTAKES  : isPal(s) creates a new string slice on every call. O(n) extra space each time.
            Pass indices instead: isPal(l, r) and check against the original string in-place.
"""

# SIMULATION
# abc → l=0,r=2: a!=c, mismatch
#         skip l: isPal(1,2) → b!=c → False
#         skip r: isPal(0,1) → a!=b → False
#       → return False
def validPalindrome(s: str) -> bool:
  def isPal(l, r):
    while l <= r:
      if s[l] != s[r]:
        return False
      l += 1
      r -= 1
    return True
  
  l, r = 0, len(s) - 1
  while l < r:
    if s[l] != s[r]:
      return isPal(l + 1, r) or isPal(l, r - 1)
    l += 1
    r -= 1
  return True