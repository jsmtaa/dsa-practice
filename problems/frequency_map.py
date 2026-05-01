"""
PROBLEM   : Frequency Map (concept)
DIFFICULTY: easy
PATTERN   : hashing, frequency count
TRIGGER   : count occurrences, how many times does each element appear
INTUITION : Iterate and increment a dict counter per element. Counter() from collections
            does this in one call.
"""

nums = [1, 2, 3, 4, 5]

freq = {}
for x in nums:
  freq[x] = freq.get(x, 0) + 1
  
print(freq)

from collections import Counter

print(dict(Counter(nums)))