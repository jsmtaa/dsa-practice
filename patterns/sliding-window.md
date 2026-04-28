# Sliding Window

---

## Flash Info
PATTERN: Sliding Window
TRIGGER: max/min window size, max/min value
ONE-SENTENCE IDEA: To avoid redundant computing, we can pass through the array once and optimize.
VARIANTS: variable, fixed
WHEN IT FAILS:

---

## Review

The sliding window technique allows for finding any contiguous values by a specific relation/condition.

The most brute-force inefficient way to utilize a sliding window is to traverse through the array by using `i` as an anchor, and `j` as the traversal pointer, along with another loop with `k` manually calculating the running result.

Let's use `Minimum Size Subarray Sum` as an example.

```py
# Time Complexity: O(N^3)
def get(n, arr):
  init best
  for i in range(n):
    for j in range(i, n):
      curr = 0
      for k in range(i, j + 1):
        curr += arr[k]
      if valid:
        best = max(best, j - i + 1)
  return best
```

However, we can optimize it to an `O(N^2)` by tracking a running sum using curr with one sliding window principle: expand.

```py
# Time Complexity: O(N^2)
def get(n, arr):
  init best
  for i in range(n):
    curr = 0
    for j in range(i, n):
      curr += arr[j] # Expand curr 
      if valid:
        best = max(best, j - i + 1)
  return best
```

We can further optimize this by introducing: shrink. This removes the need for the anchor as we can shrink the value from the left and expanding to the right. This simulates a true sliding window pattern.

```py
# Time Complexity: O(N)
def get(n, arr):
  init best
  curr = 0
  l = 0 # Anchor
  for r in range(n):
    curr += arr[r]
    while invalid:
      curr -= arr[l] # Shrink
      l += 1
    update best
  return best
```