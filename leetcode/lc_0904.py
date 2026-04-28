"""
PROBLEM   : Fruit Into Baskets
DIFFICULTY: Medium
PATTERN   : sliding window, frequency counting
TRIGGER   : 
INTUITION : Since each item of the array represents 1 fruit, and their values represent the type (id),
            we can create a frequency map that keeps the length as 2 (invariance if len >= 3)
"""

def totalFruit(fruits):
    """
    :type fruits: List[int]
    :rtype: int
    """
    baskets = {}
    l = 0
    best = 0
    for r in range(len(fruits)):
        baskets[fruits[r]] = baskets.get(fruits[r], 0) + 1

        while len(baskets) > 2:
            baskets[fruits[l]] -= 1
            if baskets[fruits[l]] == 0:
                del baskets[fruits[l]]
            l += 1
        
        best = max(best, r - l + 1)
    return best
    
