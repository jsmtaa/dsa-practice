Cascading Matrix Collapse

### Description
You are given an N × N matrix of non-negative integers and an integer K. Your task is to simulate a process of "cascading collapses" on this matrix.

### The Process

The process occurs in rounds. In each round, the following steps are performed:

**1. Identification:**
Identify all 2×2 blocks of cells within the matrix whose sum is perfectly divisible by K. A 2×2 block is defined by its top-left corner (r, c) and includes cells:
- (r, c)
- (r+1, c)
- (r, c+1)
- (r+1, c+1)

**2. Update Calculation:**
For each identified collapsible block, calculate its average value, which is the sum of its four cells divided by 4 (using integer division).

**3. Matrix Update:**
A new matrix is formed. For each cell (i, j):
- If the cell was not part of any collapsible block, its value remains unchanged
- If the cell was part of one or more collapsible blocks, its new value is the integer average of the averages of all the collapsible blocks it belonged to. For example, if a cell is in two collapsible blocks with averages A1 and A2, its new value is (A1 + A2) / 2

The process repeats until a full round is completed with no changes to any cell values in the matrix. You need to determine the total number of rounds (transformations) that were executed before the matrix stabilized and output the final state of the matrix.

### Input
- The first line of input contains two integers, N and K, separated by a space, where N is the size of the square matrix and K is the divisor
  - 2 ≤ N ≤ 100
  - 1 ≤ K ≤ 1000
- The next N lines each contain N space-separated integers, representing the initial state of the matrix
  - 0 ≤ matrix[i][j] ≤ 1,000,000

### Output
- First, print `Total rounds:` followed by the number of rounds executed
- Then, print `Final matrix:` followed by the N × N matrix in its final state. Each row of the matrix should be on a new line, with elements separated by spaces

### Sample Test Cases

#### Sample 1
```
Input:
Enter N and K: 3 10
Enter the matrix:
4 6 1
6 4 1
1 1 1

Output:
Total rounds: 1
Final matrix:
5 5 1
5 5 1
1 1 1
```

**Explanation:**
- The 2×2 block at (0,0) has sum 4+6+6+4=20, divisible by 10
- Average = 20/4 = 5
- All four cells in this block become 5

#### Sample 2
```
Input:
Enter N and K: 4 4
Enter the matrix:
2 2 2 2
6 6 6 6
1 1 1 1
1 1 1 1

Output:
Total rounds: 1
Final matrix:
4 4 4 4
4 4 4 4
1 1 1 1
1 1 1 1
```

**Explanation:**
- Multiple 2×2 blocks in the top rows are collapsible
- The overlapping cells get averaged values from all blocks they belong to

#### Sample 3
```
Input:
Enter N and K: 3 10
Enter the matrix:
1 1 1
1 19 1
1 9 1

Output:
Total rounds: 1
Final matrix:
1 1 1
7 7 7
7 7 7
```

**Explanation:**
- The 2×2 block at (1,0) has sum 1+19+1+9=30, divisible by 10
- Average = 30/4 = 7 (integer division)
- The 2×2 block at (1,1) has sum 19+1+9+1=30, also divisible by 10
- Cells update based on which blocks they belong to

---