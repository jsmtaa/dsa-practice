---
status: core
---

# Array

## Definition
Contiguous block of memory storing elements of the same type. Fixed size in traditional arrays; Python lists are dynamic and resizable.

## Operations & Complexity
- Access by index: O(1)
- Insert/delete at end: O(1) amortized
- Insert/delete at middle: O(n)
- Search (linear): O(n)
- Search (binary, sorted): O(log n)

## Python Idiom
```python
# Dynamic array (list)
arr = [1, 2, 3]
arr.append(4)  # O(1) amortized
arr.insert(1, 10)  # O(n)
arr.pop()  # O(1)
arr.pop(0)  # O(n)

# Common operations
arr.extend([5, 6])  # O(k)
sorted_arr = sorted(arr)  # O(n log n)
reversed_arr = arr[::-1]  # O(n)
```

## Linked Techniques
- [[two-pointers|Two Pointers]]
- [[sliding-window|Sliding Window]]
- [[binary-search|Binary Search]]

## When to Use
- When random access is needed
- When you need sequential storage
- Default choice unless specific structure fits better
