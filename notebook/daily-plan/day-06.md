---
status: partial
day: 6
topics: Greedy Algorithms
target-problems: 8
---

# Day 06 — Greedy Algorithms

## Goals
Master the greedy choice property; know when local optimum = global optimum.

## Techniques to Practice
- [[greedy-algorithms|Greedy Algorithms]] — Make locally optimal choice and trust it's globally optimal

## Core Insights
- **Key question**: "Does taking the locally best choice now ruin anything later?"
- **If answer is NO**: Greedy works
- **If answer is MAYBE**: Greedy probably doesn't; try DP instead
- **Sorting trick**: Often sort by some criterion first, then greedy pass

## Problem Targets
- Activity selection / interval scheduling
- Meeting rooms (min rooms needed)
- Fractional knapsack
- Gas station (can you complete circuit?)

## Linked Invariant
[[invariant-greedy-choice-property]]

## Template to Memorize
```python
# Greedy by earliest end time (activity selection)
def greedy(activities):
    activities.sort(key=lambda x: x[1])  # Sort by end time
    selected = [activities[0]]
    for start, end in activities[1:]:
        if start >= selected[-1][1]:  # No overlap
            selected.append((start, end))
    return selected
```

## Status
- [ ] Activity selection
- [ ] Meeting rooms (min rooms)
- [ ] Gas station circuit problem
- [ ] Fractional knapsack
- [ ] Recognize when greedy fails
- [ ] 8 problems solved
