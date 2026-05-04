---
status: unlearned
day: 16
invariants:
  - invariant-state-space-search
---

# Trie

## Core Idea
Tree structure where each node represents a character. Enables O(m) prefix search and auto-complete, where m is the string length. Space efficient for storing many strings with common prefixes.

## When to Use
- Autocomplete / prefix search
- Word dictionary / word break
- IP routing (longest prefix match)
- Spam filter (frequent character patterns)

## Template Code
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
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def startswith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Word break using Trie
def word_break(s, words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        node = trie.root
        for j in range(i - 1, -1, -1):
            if s[j] not in node.children:
                break
            node = node.children[s[j]]
            if node.is_end and dp[j]:
                dp[i] = True
                break
    return dp[n]
```

## Linked Invariants
- [[invariant-state-space-search]]

## Linked Problems
(Day 16: word search, word break, autocomplete, IP routing, etc.)

## Common Pitfalls
- Not marking end-of-word explicitly (is_end flag)
- Confusing startswith (prefix) with search (full word)
- Space complexity can be high for large dictionaries
