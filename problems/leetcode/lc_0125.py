"""
PROBLEM   : Valid Palindrome
DIFFICULTY: easy
PATTERN   : two pointers
TRIGGER   : palindrome, alphanumeric only, case-insensitive
INTUITION : Strip the string down to lowercase alphanumeric characters, then squeeze `l` and `r`
            inward. If any pair mismatches, it's not a palindrome.
"""

def isPalindrome(s: str) -> bool:
    s = [c.lower() for c in s if c.isalnum()]
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True
