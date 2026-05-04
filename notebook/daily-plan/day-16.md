---
status: unlearned
day: 16
topics: String Algorithms (KMP, Trie, String Hashing)
target-problems: 6-8 (Hard)
---

# Day 16 — String Algorithms: KMP + Trie + Hashing

## Goals
Master string pattern matching and prefix tree data structures.

## Techniques to Practice
- [[kmp|KMP]] — O(n + m) pattern matching; avoid naive O(n * m)
- [[trie|Trie]] — Prefix tree for fast prefix search and word dictionary
- [[string-hashing|String Hashing]] — O(1) string comparison after hashing

## Key Insights
- **KMP**: Build LPS array (longest prefix suffix); skip redundant comparisons
- **Trie**: Each node is a character; useful for autocomplete, word break, IP routing
- **String Hashing**: Hash strings for O(1) comparison; watch for collisions

## Problem Targets
- Pattern matching (KMP)
- Word break, autocomplete (Trie)
- Duplicate string detection (hashing)
- Anagram problems

## Template: Trie
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
```

## Status
- [ ] KMP: pattern matching
- [ ] Trie: basic operations (insert, search, startswith)
- [ ] Word break with Trie
- [ ] String hashing: substring matching
- [ ] 6-8 problems solved
