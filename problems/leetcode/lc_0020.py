"""
PROBLEM   : Valid Parentheses
DIFFICULTY: easy
PATTERN   : stack
TRIGGER   : balanced brackets, parentheses, valid pairs, matching open/close
INTUITION : Push open brackets onto a stack. On a closing bracket, pop the top and check it
            matches. Return True only if the stack is empty at the end.
"""

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    pairs = {
        "(": ")",
        "{": "}",
        "[": "]" 
    }
    stack = []
    for c in s:
        if c in "([{":
            stack.append(c)
        else:
            if not stack and pairs[stack.pop()] != c:
                return False
    return True

s = "()[]{}"
print(isValid(s))