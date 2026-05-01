# Cyclic String Matcher

### Description
Two strings are considered "cyclic matches" if one string can be obtained by rotating the other string. For example, "abcd" and "cdab" are cyclic matches (rotate left by 2).

Given a string S and a list of N candidate strings, identify:
1. Which candidates are cyclic matches of S
2. The minimum rotation amount needed for each match
3. The total number of unique cyclic forms possible from all strings

### Input
- First line: String S (1 ≤ length ≤ 100)
- Second line: Integer N (1 ≤ N ≤ 50)
- Next N lines: Candidate strings (same length as S)

### Output
- For each candidate (N lines):
  - "Match: rotation X" if cyclic match (where X is minimum rotations needed)
  - "No match" if not a cyclic match
- Last line: "Unique cyclic forms: Y"

### Sample Test Cases

#### Sample 1
```
Input:
abcd
4
cdab
abcd
dcba
bcda

Output:
Match: rotation 2
Match: rotation 0
No match
Match: rotation 1
Unique cyclic forms: 4
```

#### Sample 2
```
Input:
aaa
3
aaa
aaa
bbb

Output:
Match: rotation 0
Match: rotation 0
No match
Unique cyclic forms: 2
```

#### Sample 3
```
Input:
hello
5
elloh
llohe
ohell
lohel
world

Output:
Match: rotation 1
Match: rotation 2
Match: rotation 3
Match: rotation 4
No match
Unique cyclic forms: 3
```