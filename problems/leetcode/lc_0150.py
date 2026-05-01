"""
PROBLEM   : Evaluate Reverse Polish Notation
DIFFICULTY: medium
PATTERN   : stack
TRIGGER   : postfix expression, RPN, operators, evaluate
INTUITION : Push numbers onto a stack. When an operator is encountered, pop two operands,
            apply the operator (note operand order: second pop is left operand), and push
            the result back. The final stack element is the answer.
"""

#21+3*

# 4 13 5 / +
# 4 13 5 /

# yung stack will pop 2 values when it encounters an operator

tokens = ["2", "1", "+", "3", "*"]
stack = []
operators = set("+-*/")
for t in tokens:
    if t in operators:
        a = int(stack.pop())
        b = int(stack.pop())
        print(b, a)        
        match t:
            case "+":
                res = b + a
            case "-":
                res = b - a
            case "*":
                res = b * a
            case "/":
                res = int(b / a)
        stack.append(res)
    else:
        stack.append(t)

print(stack)