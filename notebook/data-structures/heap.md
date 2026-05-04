---
status: core
---

# Heap

## Definition
Complete binary tree where parent value is smaller (min-heap) or larger (max-heap) than children. Enables O(log n) insertion and removal of extrema.

## Operations & Complexity
- Insert: O(log n)
- Extract min/max: O(log n)
- Peek min/max: O(1)
- Heapify: O(n)

## Python Idiom
```python
import heapq

# Min-heap (Python default)
min_heap = []
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 7)
smallest = heapq.heappop(min_heap)  # Returns 3
peek = min_heap[0]  # Peek, returns 5

# Max-heap (use negative values)
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
largest = -heapq.heappop(max_heap)  # Returns 5

# Heapify existing list
arr = [5, 3, 7, 1]
heapq.heapify(arr)  # In-place, O(n)

# k smallest/largest
k_smallest = heapq.nsmallest(2, arr)
k_largest = heapq.nlargest(2, arr)
```

## Linked Techniques
- [[dijkstra|Dijkstra]]

## When to Use
- Priority queue
- Finding k largest/smallest elements
- Median-finding (two heaps)
- Heap sort
