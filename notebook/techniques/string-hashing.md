---
status: unlearned
day: 16
invariants:
  - invariant-monotonicity
---

# String Hashing

## Core Idea
Assign a numerical value to each string using polynomial rolling hash. Enables fast string comparison in O(1) after preprocessing and pattern matching in O(n).

## When to Use
- Fast string comparison
- Pattern matching alternatives to KMP
- Duplicate string detection
- Substring search

## Template Code
```python
def string_hash(s, base=31, mod=10**9 + 7):
    hash_val = 0
    base_pow = 1
    for char in s:
        hash_val = (hash_val + (ord(char) - ord('a') + 1) * base_pow) % mod
        base_pow = (base_pow * base) % mod
    return hash_val

# Rolling hash for substring search
def rolling_hash_search(text, pattern):
    base, mod = 31, 10**9 + 7
    pattern_hash = string_hash(pattern, base, mod)
    
    text_hash = 0
    base_pow = 1
    for i, char in enumerate(pattern):
        text_hash = (text_hash + (ord(char) - ord('a') + 1) * base_pow) % mod
        if i < len(pattern) - 1:
            base_pow = (base_pow * base) % mod
    
    for i in range(len(text) - len(pattern) + 1):
        if text_hash == pattern_hash:
            if text[i:i + len(pattern)] == pattern:
                return i
        if i < len(text) - len(pattern):
            text_hash = (text_hash - (ord(text[i]) - ord('a') + 1)) // base
            text_hash = (text_hash + (ord(text[i + len(pattern)]) - ord('a') + 1) * base_pow) % mod
    return -1
```

## Linked Invariants
- [[invariant-monotonicity]]

## Linked Problems
(Day 16: substring matching, duplicate string detection, etc.)

## Common Pitfalls
- Hash collisions: even with good base and modulo, collisions can occur (verify matches)
- Rolling hash division: be careful with modular arithmetic
- Base and modulo choice: use prime modulo to reduce collisions
