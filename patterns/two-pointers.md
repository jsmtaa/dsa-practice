# Two Pointers
---

## Flash Info

PATTERN: Two Pointers
TRIGGER: sorted array/list, finding pairs/triplets summing to a target, removing duplicates in-place, reversing or      comparing both ends, linked list cycle detection or midpoint
ONE-SENTENCE IDEA: Place two indices at strategic positions and move them toward each other (or same direction) to avoid the O(n²) brute-force nested loop.
VARIANTS:
  - Opposite ends — left at 0, right at n-1, squeeze inward (two-sum on sorted array, container with most water)
  - Same direction (fast/slow) — both start at 0 but advance at different rates; cycle detection (Floyd's), linked list middle, nth node from end
  - Partition — one pointer marks the "write" position, the other scans forward (remove duplicates, move zeroes)
WHEN IT FAILS:
  - Array is unsorted and sorting would destroy original indices you need
  - You need all combinations, not just existence/count — pointers skip pairs
  - Non-contiguous pairs with complex constraints that can't be resolved by a single step
  - Data structure lacks O(1) indexed access (hash map, set)

---

## Review

### Deriving the Pattern

The brute-force approach nests two loops: `i` picks a start position and `j` picks an end position, checking every possible pair. Each iteration also does O(N) work for the slice, making the full cost O(N³).

The most common entry point is `is-palindrome`.

```py
# Time Complexity: O(N^3)
def is_pal(n, s):
  for i in range(n):
    for j in range(n):
      sliced = s[i:j+1]
      if sliced == sliced[::-1]:
        return True
  return False
```

We can cut this down by recognising we only need to compare characters at symmetric positions. Place one pointer at each end and move inward — one pass, O(N).

```py
# Time Complexity: O(N)
def is_pal(s):
  l, r = 0, len(s) - 1
  while l < r:
    if s[l] != s[r]:
      return False
    l += 1
    r -= 1
  return True
```

The key insight: when the structure has symmetry or is sorted, moving pointers inward eliminates all pairs in between without visiting them.

### Variants

**Opposite ends** squeezes `l` and `r` inward based on a condition. Use whenever the problem involves comparing or summing values from both ends of a sorted sequence.

*Two Sum II* is the canonical example. The brute-force checks every pair:

```py
# Time Complexity: O(N²)
def twoSum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i + 1, j + 1]
```

Because the array is sorted, we can eliminate an entire index each step instead of scanning all pairs. `nums[l] + nums[r]` uses the smallest and largest remaining values simultaneously — if the sum is too high, `r` is dead; if too low, `l` is dead:

```py
# Time Complexity: O(N)
def twoSum(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return [l + 1, r + 1]
        elif s > target:
            r -= 1
        else:
            l += 1
```

**Fast / Slow** keeps both pointers moving the same direction but at different speeds. The canonical use is Floyd's cycle detection: if a cycle exists, fast eventually laps slow; if not, fast reaches null first.

```py
def has_cycle(head):
  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True
  return False
```

**Partition** uses one pointer as a write cursor and one as a read cursor, both moving left to right. Elements that pass a condition get written at the write position; everything else is skipped.

```py
# Remove duplicates in-place from sorted array
def remove_dups(nums):
  w = 1
  for r in range(1, len(nums)):
    if nums[r] != nums[r - 1]:
      nums[w] = nums[r]
      w += 1
  return w
```
