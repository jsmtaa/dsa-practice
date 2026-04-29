# Sliding Window

---

## Flash Info

PATTERN: Sliding Window
TRIGGER: at least, at most, at exactly
ONE-SENTENCE IDEA: To avoid redundant computing, we can pass through the array once and optimize.
VARIANTS: variable, fixed
WHEN IT FAILS:

---

## Review

### Deriving the pattern

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

### Variants

The most common patterns that we see here are `at most`, `at least`, and `at exactly`. This is as straightforward as it gets.

For `at most` problems, we have to simply keep a K-sized window at maximum. Vice versa applies for `at least`, but we usually update values while we shrink, because the result depends on K-sizes greater than K (counter-intuitive, but makes sense).

In contrast, `at exactly` requires us to understand a simple logic:
To find the total count of people exactly aged 65, we just have to remove every count of people aged 64 and below. This means getting `at most` of K and `at most` of K - 1.