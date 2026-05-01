"""
PROBLEM   : Daily Temperatures
DIFFICULTY: medium
PATTERN   : monotonic stack
TRIGGER   : next warmer day, days until larger value, wait count
INTUITION : Maintain a stack of indices of "unresolved" temperatures (kept in decreasing order).
            When a warmer temperature arrives, pop every colder index from the stack and record
            the gap as their answer.
"""

temperatures = [40, 0, 40, 30]

stack = []
res = [0] * len(temperatures)

for i in range(len(temperatures)):
    # while stack and current > latest temp
    while stack and temperatures[i] > temperatures[stack[-1]]:
        idx = stack.pop()
        res[idx] = i - idx
    stack.append(i) 
    print(stack)

print(res)