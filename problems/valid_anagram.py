"""
PROBLEM   : Valid Anagram (LC #242)
DIFFICULTY: easy
PATTERN   : hashing, frequency count
TRIGGER   : anagram, same characters same frequency, two strings
INTUITION : Compare frequency counts using Counter. Two strings are anagrams iff their
            Counter maps are equal.
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        
        return Counter(s) == Counter(t)        

def main():
    s = "a"
    t = "ab"
    print(Solution().isAnagram(s, t))

if __name__ == "__main__":
    main()
        
        