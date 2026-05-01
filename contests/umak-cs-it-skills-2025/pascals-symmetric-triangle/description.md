# Pascal's Symmetric Triangle

### Description
Pascal's Triangle is a triangular array of binomial coefficients. It begins with 1 at the top, and each number below is the sum of the two numbers directly above it. If there is only one number above, it's considered 0 on the other side. This results in 1s along the edges of the triangle.

Your task is to generate and print Pascal's Triangle up to N rows. The output should be neatly formatted, with each row centered, and numbers aligned such that the entire triangle forms a symmetric shape. The spacing between numbers and rows should adjust dynamically based on the largest number in the triangle to maintain perfect alignment.

### Example
For N=4:
```
   1
  1 1
 1 2 1
1 3 3 1
```

**Note:** For larger N, the numbers will grow, and the spacing needs to adapt to ensure symmetric output.

### Input
The input will consist of a single integer N (1 ≤ N ≤ 20), representing the number of rows to generate for Pascal's Triangle.

### Output
Print the Pascal's Triangle with N rows, following the symmetric and dynamic spacing requirements as described above. Each number should be followed by a single space, except for the last number in each row, which should be followed by a newline. Ensure that the entire triangle is centered horizontally.

### Sample Test Cases

#### Sample 1
```
Input:
Enter number of rows: 1

Output:
1
```

#### Sample 2
```
Input:
Enter number of rows: 2

Output:
1
1 1
```

#### Sample 3
```
Input:
Enter number of rows: 4

Output:
1
1 1
1 2 1
1 3 3 1
```

---
