# Isogram Checker

### Description
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Write a program that checks if a given string is an isogram. The check must be case-insensitive, meaning characters 'A' and 'a' should be treated as the same letter.

For example, "background" is an isogram, but "hello" is not because the letter 'l' is repeated.

### Input
- A single string `s`

### Constraints
- The length of `s` is between 1 and 100 characters
- The string will only contain alphabetic characters (a-z, A-Z)

### Output
Print "Output: Isogram" if the string is an isogram, and "Output: Not an isogram" otherwise.

### Sample Test Cases

#### Sample 1
```
Input:
Enter a string: background

Output:
Output: Isogram
```

#### Sample 2
```
Input:
Enter a string: hello

Output:
Output: Not an isogram
```

#### Sample 3
```
Input:
Enter a string: Alphabet

Output:
Output: Not an isogram
```