# Bracket Balance Validator

### Description
You are given a string containing various types of brackets: `()`, `[]`, `{}`. Your task is to determine if the brackets are properly balanced and nested. Additionally, calculate the maximum nesting depth of the brackets.

A string is balanced if:
- Every opening bracket has a corresponding closing bracket
- Brackets are properly nested (no interleaving)
- Brackets close in the correct order

### Input
- A single string S (1 ≤ length ≤ 1000) containing brackets and other characters

### Output
- First line: "Valid" if brackets are balanced, "Invalid" otherwise
- Second line: "Max Depth: X" where X is the maximum nesting depth (only if valid)

### Sample Test Cases

#### Sample 1
```
Input:
{[()]}

Output:
Valid
Max Depth: 3
```

#### Sample 2
```
Input:
{[(])}

Output:
Invalid
```

#### Sample 3
```
Input:
((()))[]{}

Output:
Valid
Max Depth: 3
```

#### Sample 4
```
Input:
abc(def[ghi]jkl)mno

Output:
Valid
Max Depth: 2
```