# Minimal Transformation Cost

### Description
You are given:
- Two strings, `startWord` and `endWord`, both of equal length
- A list of character transformations, each represented as a tuple (u, v, w), meaning:
  - You can transform character u into character v with a cost of w

These transformations can be chained. For example, if:
- 'A' → 'B' costs 2, and
- 'B' → 'C' costs 3,
- then you can transform 'A' → 'C' at a total cost of 5

### Objective
Transform `startWord` into `endWord`, character by character, such that:
- For each position i, you compute the minimum cost to transform `startWord[i]` into `endWord[i]` using the available transformations
- The total transformation cost is the sum of these individual character transformation costs

### Input
- The first line contains the string `startWord` (1 ≤ length ≤ 1000)
- The second line contains the string `endWord` (same length as `startWord`)
- The third line contains an integer n (1 ≤ n ≤ 500), the number of available transformations
- The next n lines each contain a character u, a character v, and an integer w (1 ≤ w ≤ 1000), representing a transformation from u to v with cost w

### Output
A single integer representing the minimum total cost to transform `startWord` to `endWord`. If the transformation is not possible, print -1.

### Sample Test Cases

#### Sample 1
```
Input:
Enter startWord: A
Enter endWord: B
Enter number of transformations: 1
Enter transformations:
A B 100

Output:
Minimal Transformation Cost: 100
```

#### Sample 2
```
Input:
Enter startWord: ACE
Enter endWord: BDF
Enter number of transformations: 3
Enter transformations:
A B 10
C D 20
E F 30

Output:
Minimal Transformation Cost: 60
```

#### Sample 3
```
Input:
Enter startWord: X
Enter endWord: Z
Enter number of transformations: 3
Enter transformations:
X Y 10
Y Z 10
X Z 25

Output:
Minimal Transformation Cost: 20
```

---