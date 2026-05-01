"""
PROBLEM   : Defuse the Bomb (LC #1652)
DIFFICULTY: easy
PATTERN   : sliding window (fixed), circular array
TRIGGER   : circular array, sum of k next/previous elements
INTUITION : Maintain a running sum window of size k starting just after each index.
            Slide the window by subtracting the outgoing element and adding the incoming
            one, using modulo for circular wrap-around.
"""

code = [5,7,1,4]
k = 3

dcr = [0] * len(code)

l = 1
r = k + 1
csum = sum(code[l:r])
print(csum)
for i in range(len(code)):
    dcr[i] = csum
    csum -= code[l % len(code)]
    csum += code[r % len(code)]
    l += 1
    r += 1

print(dcr)