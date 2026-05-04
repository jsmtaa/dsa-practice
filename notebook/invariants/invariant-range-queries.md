---
status: core
related_techniques: 3
---

# Range Query Invariant

## Definition
Range queries ask about aggregates (sum, min, max, count) over a contiguous subset of data. Preprocessing structures like prefix sums or segment trees enable fast answers to many queries without recalculating from scratch each time.

## Recognition Signals
- "Sum of elements from index L to R" (1D or 2D)
- "Minimum/maximum in a range"
- "How many elements in [L, R] satisfy property X?"
- "Frequent queries on subarrays"
- Time limit suggests O(log n) or O(1) per query (not O(n))
- "Update element at index i" + "query range" (dynamic range queries)

## Techniques That Exploit It
- [[prefix-sum|Prefix Sum]]
- [[segment-tree|Segment Tree]]
- [[fenwick-tree-bit|Fenwick Tree (BIT)]]

## Common Failure Modes
- Confusing 1D prefix sums with 2D (different formula for 2D queries)
- Not handling updates correctly in a segment tree or Fenwick tree
- Off-by-one errors in inclusive/exclusive range boundaries
- Building a prefix sum on an unsorted array when sorted is needed
- Segment tree complexity overkill for static (non-updated) queries
