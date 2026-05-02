# Backtracking

---

## Flash Info

PATTERN: Backtracking
TRIGGER: all subsets / power set, all combinations, all permutations, all orderings, generate all valid X
ONE-SENTENCE IDEA: Build a solution incrementally — pick a choice, recurse into it, then undo it to explore the next branch.
VARIANTS:
  - Subsets — binary include/exclude decision at each element
  - Combinations — pick forward with an index, never go backwards
  - Permutations — no index; every slot tries every unused element
  - Branching over fixed structure — input defines slots and their option sets
WHEN IT FAILS:
  - Overlapping subproblems exist — DP will be orders of magnitude faster
  - You only need one valid path — plain DFS without undo is simpler
  - No pruning is possible — exponential blowup with nothing to cut early

---

## Review

### Deriving the pattern

The brute-force approach to generating all subsets uses a bitmask: iterate all 2^N integers and decode which bits are set.

```py
# Time Complexity: O(N * 2^N)
def subsets(nums):
    res = []
    for mask in range(1 << len(nums)):
        path = []
        for i in range(len(nums)):
            if mask & (1 << i):
                path.append(nums[i])
        res.append(path)
    return res
```

This works for subsets but doesn't generalize to permutations or combinations — there's no bitmask encoding for those. The underlying structure across all three is the same: you're exploring a tree of decisions.

A naive recursive version creates a new list at every node:

```py
# Correct but allocates a new list at every call
def backtrack(index, path):
    result.append(path)
    for i in range(index, len(nums)):
        backtrack(i + 1, path + [nums[i]])
```

The key optimization: mutate a shared path and undo the mutation after each recursive call. One list, O(N) space, no mid-tree copies.

```
pick → recurse → undo
```

```py
def backtrack(index, path):
    result.append(path[:])      # snapshot only at the leaf
    for i in range(index, len(nums)):
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()              # undo
```

Every variant below is this same structure — shaped by what counts as a valid leaf and what counts as a dead end.

---

### Variants

**Subsets (lc_0078, lc_0090)**

At every element, make a binary decision: include or skip. Both branches run to the end.

```python
def backtrack(index, path):
    if index == len(nums):
        result.append(path[:])
        return
    path.append(nums[index])
    backtrack(index + 1, path)   # include
    path.pop()
    backtrack(index + 1, path)   # skip
```

**With duplicates (lc_0090):** on the skip branch, jump past all duplicates so two "skip" branches at the same depth never start with the same value.

```python
next_index = index + 1
while next_index < len(nums) and nums[next_index] == nums[index]:
    next_index += 1
backtrack(next_index, path)
```

---

**Combinations (lc_0039)**

Choose elements that meet a constraint. Pass an index so you never go backwards.

```python
def backtrack(index, path):
    if sum(path) == target:
        result.append(path[:])
        return
    if index >= len(candidates) or sum(path) > target:
        return
    path.append(candidates[index])
    backtrack(index, path)       # reuse the same element
    path.pop()
    backtrack(index + 1, path)   # advance
```

---

**Permutations (lc_0046, lc_0047)**

Every slot tries every unused element — so no index is passed; instead, skip anything already in the path.

```python
def backtrack(path):
    if len(path) == len(nums):
        result.append(path[:])
        return
    for x in nums:
        if x in path:
            continue
        path.append(x)
        backtrack(path)
        path.pop()
```

**With duplicates (lc_0047):** sort, add `used[]`, and skip `nums[i]` when `nums[i] == nums[i-1] and not used[i-1]`. The rule forces us to always pick the first copy of a value before the second, so duplicate branches never form.

---

**Branching over a fixed structure (lc_0017)**

When the input defines a fixed number of slots and each slot has a discrete set of options, loop over those options at each depth level.

```python
def backtrack(index, path):
    if len(path) == len(digits):
        result.append("".join(path))
        return
    for letter in letters[digits[index]]:
        path.append(letter)
        backtrack(index + 1, path)
        path.pop()
```

---

## Decision framework

| Trigger phrase                              | Shape                      |
|---------------------------------------------|----------------------------|
| "all subsets" / "power set"                 | Subsets                    |
| "combinations that sum to" / "add up to"   | Combinations               |
| "all permutations" / "all orderings"        | Permutations               |
| "all strings of length N from a given map"  | Branching over structure   |
| duplicates in input, unique results required | Add dedup (sort + skip)   |

---

## Deduplication

Two styles of traversal → two dedup techniques:

**For-loop (permutations):** `used[]` array + skip rule.
```python
if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
    continue
```

**Binary (subsets/combinations):** skip ahead on the exclude branch.
```python
while next_index < len(nums) and nums[next_index] == nums[index]:
    next_index += 1
```

Both require sorting first so duplicates are adjacent.

---

## Pruning

Cut the branch before it reaches the base case:
- Sum exceeds target → `return`
- Index out of bounds → `return`
- Element already used → `continue`

The earlier you prune, the shallower the tree.
