"""
PROBLEM   : Making Anagrams (HackerRank)
DIFFICULTY: easy
PATTERN   : hashing, frequency count
TRIGGER   : minimum deletions to make two strings anagrams
INTUITION : Count character frequencies. Characters not shared between the two strings
            must be deleted. Result = len(s1) + len(s2) - 2 * shared_count.
"""

def makingAnagrams(s1, s2):
    # Write your code here
    f = {}
    for c in s1:
        f[c] = f.get(c, 0) + 1
    
    count = 0
    for v in f:
        if v in s2 and f[v] > 0:
            f[v] -= 1
            count += 1
    print(f)
    return len(s1) + len(s2) - (count * 2)

c = makingAnagrams("absdjkvuahdakejfnfauhdsaavasdlkj", "djfladfhiawasdkjvalskufhafablsdkashlahdfa")
print(c)