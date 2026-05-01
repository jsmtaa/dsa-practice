"""
PROBLEM   : Valid Palindrome (LC #125)
DIFFICULTY: easy
PATTERN   : two pointers, string manipulation
TRIGGER   : palindrome, alphanumeric only, case-insensitive
INTUITION : Strip to lowercase alphanumeric characters, then compare the cleaned string
            with its reverse.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join(c.lower() for c in s if c.isalnum())
        return s == s[::-1] 



def main():
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))

if __name__ == "__main__":
    main()
        
        