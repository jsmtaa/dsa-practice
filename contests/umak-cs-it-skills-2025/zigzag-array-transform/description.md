Zigzag Array Transform

### Description
Given an array of integers, transform it into a "zigzag" array where elements alternate between being larger and smaller than their neighbors. Specifically, for indices 0, 2, 4, ... (even indices), the element should be greater than its neighbors. For indices 1, 3, 5, ... (odd indices), the element should be less than its neighbors.

You can achieve this by swapping adjacent elements. Count the minimum number of swaps needed and output the transformed array.

**Example:**
```
Input: [4, 3, 7, 8, 6, 2, 1]
Process: Want pattern: arr[0] > arr[1] < arr[2] > arr[3] < arr[4] > arr[5] < arr[6]
Output: [4, 3, 8, 6, 7, 1, 2]
Swaps: 2
```

### Input
- First line: integer N (3 ≤ N ≤ 100), the number of elements
- Second line: N space-separated integers (-1000 ≤ arr[i] ≤ 1000)

### Output
- First line: "Swaps needed: X" where X is the minimum number of swaps
- Second line: The transformed zigzag array, space-separated

### Sample Test Cases

#### Sample 1
```
Input:
5
1 2 3 4 5

Output:
Swaps needed: 2
2 1 4 3 5
```

#### Sample 2
```
Input:
7
4 3 7 8 6 2 1

Output:
Swaps needed: 2
4 3 8 6 7 1 2
```

#### Sample 3
```
Input:
4
10 10 10 10

Output:
Swaps needed: 0
10 10 10 10
```

---