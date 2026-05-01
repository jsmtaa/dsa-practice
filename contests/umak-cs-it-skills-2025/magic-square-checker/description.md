# Magic Square Checker

### Description
A magic square is an N×N grid filled with distinct integers such that:
- Each row sums to the same value (magic constant)
- Each column sums to the same value
- Both main diagonals sum to the same value

Given an N×N matrix, determine if it's a magic square. If it is, output the magic constant and verify if it contains consecutive integers starting from 1.

### Input
- First line: Integer N (2 ≤ N ≤ 10)
- Next N lines: N space-separated integers

### Output
- First line: "Magic Square" or "Not a Magic Square"
- If magic square:
  - Second line: "Magic Constant: X"
  - Third line: "Contains 1 to N²: Yes" or "Contains 1 to N²: No"

### Sample Test Cases

#### Sample 1
```
Input:
3
2 7 6
9 5 1
4 3 8

Output:
Magic Square
Magic Constant: 15
Contains 1 to N²: Yes
```

#### Sample 2
```
Input:
3
1 2 3
4 5 6
7 8 9

Output:
Not a Magic Square
```

#### Sample 3
```
Input:
4
16 2 3 13
5 11 10 8
9 7 6 12
4 14 15 1

Output:
Magic Square
Magic Constant: 34
Contains 1 to N²: Yes
```

---
