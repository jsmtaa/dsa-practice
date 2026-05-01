"""
PROBLEM   : Valid Anagram
DIFFICULTY: easy
PATTERN   : hashing, frequency count
TRIGGER   : anagram, same characters same frequency, two strings
INTUITION : Build frequency maps for both strings. If both maps are equal (and lengths match),
            the strings are anagrams.
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Case 0: if not equal len
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}
        # dict[key] automatically adds values to a dict
        for i in range(len(s)):
            count_s[t[i]] = count_s.get(t[i], 0) + 1
            count_t[s[i]] = count_t.get(s[i], 0) + 1

        if count_s == count_t:
            return True
        
        return False