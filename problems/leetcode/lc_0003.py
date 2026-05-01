"""
PROBLEM   : Longest Substring Without Repeating Characters
DIFFICULTY: medium
PATTERN   : sliding window
TRIGGER   : longest substring, no repeating characters, unique chars
INTUITION : Maintain a set of seen characters. Expand r; if s[r] is already in the set,
            shrink from l until the duplicate is removed. Track the max window length.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ml = 0
        seen = set()
        l=0
        for r in range(len(s)):
          if s[r] not in seen:
            seen.add(s[r])
            l =
        
        
def main():
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))

if __name__ == "__main__":
    main()
        
        
