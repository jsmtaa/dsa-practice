"""
PROBLEM   : Valid Parentheses (stack exploration)
DIFFICULTY: easy
PATTERN   : stack
TRIGGER   : matching brackets, balanced pairs, LIFO, closing must match top
INTUITION : Push open brackets onto the stack. On a closing bracket, check if it
            matches the top element and pop. Stack must be empty for a valid string.
"""

s = "([])"
stack = []

pairs = {
    ")": "(",
    "]": "[",
    "}": "{"
}
for c in s:
    if c in "([":
        stack.append(c)
    else:
        # Here goes when c is not an opening parenthesis
        # so we check if it's a closing, and it belongs in the stack
        if len(stack) != 0 and pairs[c] in stack[-1]:
            print(pairs[c]) 
            stack.pop() 

print(stack)