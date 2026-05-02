"""
PROBLEM   : Longest Palindromic Substring
DIFFICULTY: medium
PATTERN   : expand around center
TRIGGER   : longest palindrome, substring, expand from each character
INTUITION : A palindrome reads the same from both ends, so try growing outward from every
            character (odd-length) and every adjacent pair (even-length). Track the longest
            symmetric window seen.
"""

def longestPalindrome(s: str) -> str:
    res = ""

    def expand(l, r) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]  # l and r stepped one past the valid palindrome

    for i in range(len(s)):
        odd  = expand(i, i)
        even = expand(i, i + 1)
        if len(odd)  > len(res): res = odd
        if len(even) > len(res): res = even

    return res
