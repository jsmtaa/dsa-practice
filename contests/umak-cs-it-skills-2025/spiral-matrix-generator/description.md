# Spiral Matrix Generator

### Description
Generate an N×N matrix filled with integers from 1 to N² in a spiral pattern. The spiral starts from the top-left corner, moves right, then down, then left, then up, and continues spiraling inward.

After generating the matrix, extract specific elements:
- All elements on the outer border
- All elements on diagonals
- The center element (if N is odd)

### Input
- A single integer N (2 ≤ N ≤ 20)

### Output
- First N lines: The spiral matrix
- Next line: "Border sum: X"
- Next line: "Diagonal sum: Y"
- Next line: "Center: Z" (only if N is odd, otherwise "Center: None")

### Sample Test Cases

#### Sample 1
```
Input:
3

Output:
1 2 3
8 9 4
7 6 5
Border sum: 36
Diagonal sum: 25
Center: 9
```

#### Sample 2
```
Input:
4

Output:
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
Border sum: 68
Diagonal sum: 68
Center: None
```

#### Sample 3
```
Input:
5

Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
Border sum: 156
Diagonal sum: 105
Center: 25
```

---