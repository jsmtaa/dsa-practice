---
status: unlearned
day: 16
invariants:
  - invariant-monotonicity
---

# KMP (Knuth-Morris-Pratt)

## Core Idea
Build a failure function (LPS array) to skip redundant comparisons during pattern matching. Enables O(n + m) pattern matching instead of O(n * m) with naive approach.

## When to Use
- Pattern matching in strings
- Finding all occurrences of a pattern
- Shortest string with pattern match requirements
- String matching with fewer backtrack comparisons

## Template Code
```python
def build_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = build_lps(pattern)
    results = []
    i = 0  # text index
    j = 0  # pattern index
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            results.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return results
```

## Linked Invariants
- [[invariant-monotonicity]]

## Linked Problems
(Day 16: pattern matching, string matching variants, etc.)

## Common Pitfalls
- LPS array construction: off-by-one errors
- Resetting j to lps[j-1] after mismatch (not to 0)
- Edge cases: empty pattern, pattern longer than text
