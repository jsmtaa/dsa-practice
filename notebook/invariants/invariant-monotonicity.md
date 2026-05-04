---
status: core
related_techniques: 2
---

# Monotonicity Invariant

## Definition
A sequence has monotonicity when values change in a predictable direction — always increasing, always decreasing, or increasing then decreasing (or vice versa). When you exploit monotonicity, you can eliminate large search spaces with a single directional scan or binary jump.

## Recognition Signals
- "Sorted array" in the problem statement
- "Find the first/last occurrence of X"
- "Binary search" hint or time complexity requirement (O(log n))
- "Two pointers" or "sliding window" is mentioned or hinted
- Array is "mostly sorted" or "rotated sorted"
- Problem asks for "local maximum/minimum" or extrema

## Techniques That Exploit It
- [[two-pointers|Two Pointers]]
- [[sliding-window|Sliding Window]]
- [[sorting-binary-search|Sorting + Binary Search]]
- [[monotonic-stack|Monotonic Stack]]
- [[binary-search|Binary Search]]

## Common Failure Modes
- Assuming monotonicity when values are random or jumbled
- Confusing "weakly monotonic" (allows duplicates) with "strictly monotonic" (no duplicates)
- Using monotonicity tricks on an unsorted array without sorting first
- Not checking edge cases where monotonicity breaks (e.g., rotated arrays, boundaries)
