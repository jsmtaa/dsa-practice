---
status: partial
day: 6
invariants:
  - invariant-greedy-choice-property
---

# Greedy Algorithms

## Core Idea
Make locally optimal choices at each step and trust that the sequence of greedy choices leads to a globally optimal solution. No need for dynamic programming if the greedy choice property holds.

## When to Use
- Activity selection: choose non-overlapping events to maximize count
- Interval scheduling: meeting rooms, task scheduling
- Huffman coding: build optimal prefix-free code
- Fractional knapsack: always take highest value-to-weight ratio
- Proving greedy works is harder than implementing it — always verify

## Template Code
```python
# Activity selection (greedy by end time)
def activity_selection(activities):
    # activities = [(start, end), ...]
    activities.sort(key=lambda x: x[1])  # Sort by end time
    selected = [activities[0]]
    for start, end in activities[1:]:
        if start >= selected[-1][1]:  # No overlap
            selected.append((start, end))
    return selected

# Interval scheduling
def erase_overlap_intervals(intervals):
    intervals.sort(key=lambda x: x[1])  # Sort by end time
    count = 0
    end = intervals[0][1]
    for start, cur_end in intervals[1:]:
        if start < end:  # Overlapping
            count += 1
        else:
            end = cur_end
    return count
```

## Linked Invariants
- [[invariant-greedy-choice-property]]

## Linked Problems
(Day 6: activity selection, meeting rooms, interval scheduling, gas station, etc.)

## Common Pitfalls
- Assuming greedy works without proof (many problems *look* greedy but need DP)
- Wrong sorting criterion: ascending vs. descending
- Not handling edge cases: empty input, single interval, fully overlapping
- Confusing with other paradigms: some problems require DP, not greedy
- Forgetting to check the invariant: "does this locally best choice ruin anything globally?"
