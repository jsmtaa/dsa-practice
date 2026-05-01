# Grid Path Sum Max

### Description
You are given a grid (2D array) of positive integers with R rows and C columns. You start at the top-left cell (0, 0) and want to reach the bottom-right cell (R-1, C-1). From any cell (r, c), you can only move to the cell immediately to its right (r, c+1) or to the cell immediately below it (r+1, c).

Your goal is to find a path from the top-left to the bottom-right corner such that the sum of all numbers along this path is maximized. Output this maximum possible sum.

### Example
Consider the following grid:
```
1 2 3
4 5 6
7 8 9
```

A possible path from (0,0) to (2,2) is:
- 1 → 4 → 7 → 8 → 9

with a total sum of:
- 1 + 4 + 7 + 8 + 9 = 29

This is the maximum possible sum for this grid.

### Input
- The first line contains two integers, R and C, representing the number of rows and columns, respectively
- The next R lines each contain C integers, representing the values in the grid

### Constraints
- 1 ≤ R, C ≤ 100
- 1 ≤ grid[i][j] ≤ 1000

### Output
The maximum sum of cell values along any valid path from (0,0) to (R-1, C-1).

### Sample Test Cases

#### Sample 1
```
Input:
Enter R and C: 3 3
Enter the grid:
1 2 3
4 5 6
7 8 9

Output:
Maximum path sum: 29
```

#### Sample 2
```
Input:
Enter R and C: 1 5
Enter the grid:
10 20 30 40 50

Output:
Maximum path sum: 150
```

#### Sample 3
```
Input:
Enter R and C: 5 1
Enter the grid:
10
20
30
40
50

Output:
Maximum path sum: 150
```

---