# Binary Grid Path Counter

### Description
You are given an N×M binary grid (containing only 0s and 1s). You start at the top-left corner (0,0) and want to reach the bottom-right corner (N-1, M-1). You can only move right or down, and you can only step on cells containing 1.

Count the total number of valid paths from start to finish. If no path exists, output 0.

Additionally, find the path with the maximum sum if cells contain values instead of just 0s and 1s.

### Input
- First line: Two integers N and M (2 ≤ N, M ≤ 15)
- Next N lines: M space-separated integers (0 or positive integers up to 100)

### Output
- First line: "Valid paths: X" where X is the number of valid paths
- Second line: "Maximum path sum: Y" (sum of values along the best path)

### Sample Test Cases

#### Sample 1
```
Input:
3 3
1 1 1
1 0 1
1 1 1

Output:
Valid paths: 2
Maximum path sum: 7
```

#### Sample 2
```
Input:
3 4
1 1 1 1
1 0 0 1
1 1 1 1

Output:
Valid paths: 1
Maximum path sum: 9
```

#### Sample 3
```
Input:
2 2
1 0
0 1

Output:
Valid paths: 0
Maximum path sum: 0
```

---