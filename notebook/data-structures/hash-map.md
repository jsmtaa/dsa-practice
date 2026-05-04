---
status: core
---

# Hash Map (Dictionary)

## Definition
Key-value store using hash function for O(1) average-case lookups. Python dict is the standard implementation.

## Operations & Complexity
- Insert/update: O(1) average
- Delete: O(1) average
- Lookup: O(1) average
- Collision handling: O(n) worst-case (rare)

## Python Idiom
```python
from collections import defaultdict, Counter

# Dictionary
d = {'a': 1, 'b': 2}
d['c'] = 3  # Insert/update
val = d.get('a', default=0)  # Safe lookup
del d['a']  # Delete
'a' in d  # Check membership

# DefaultDict (auto-init missing keys)
dd = defaultdict(int)
dd['count'] += 1  # No KeyError

# Counter (frequency map)
freq = Counter(['a', 'b', 'a', 'c'])
freq['a']  # Returns 2
freq.most_common(2)  # Top 2 frequent items
```

## Linked Techniques
- [[hashing|Hashing]]

## When to Use
- Frequency counting
- Fast lookup tables
- Caching/memoization
- Two-pointer hash-based solutions
