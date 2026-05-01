"""
PROBLEM   : Koko Eating Bananas
DIFFICULTY: medium
PATTERN   : binary search
TRIGGER   : minimum speed, finish within h hours, can-complete predicate
INTUITION : Binary search on eating speed k in range [1, max(piles)]. For each candidate k,
            compute total hours needed (ceil(pile / k) per pile); shrink upper bound if it fits,
            raise lower bound otherwise.
"""

import math

piles = [3,6,7,11]
h = 8
# talking bout piles here
l, r=1,max(piles)

while l < r:
    total = 0
    mid = (l + r) // 2

    for p in piles:
        total += math.ceil(p / mid)
    
    if total <= h:
        r = mid
    else:
        l = mid + 1
    
print(mid)