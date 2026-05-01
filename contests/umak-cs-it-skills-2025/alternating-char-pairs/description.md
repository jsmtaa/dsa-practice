# Alternating Char Pairs

### Description
You are given a string S consisting of lowercase English letters. Your task is to count the number of pairs of adjacent characters in the string where one character is a vowel and the other is a consonant. 

For example, in the string "apple":
- 'a' (vowel) is followed by 'p' (consonant), which is a valid pair
- 'p' (consonant) is followed by 'p' (consonant), which is not
- 'p' (consonant) is followed by 'l' (consonant), which is not
- 'l' (consonant) is followed by 'e' (vowel), which is a valid pair

A vowel is defined as one of 'a', 'e', 'i', 'o', 'u'. All other lowercase English letters are consonants.

### Input
The input will consist of a single line containing the string S.

### Constraints
- The length of S will be between 1 and 1000, inclusive
- Each character in S will be a lowercase English letter ('a'-'z')

### Output
Print a single integer representing the total count of alternating vowel-consonant or consonant-vowel pairs.

### Sample Test Cases

#### Sample 1
```
Input:
Enter the string: apple

Output:
Alternating pairs: 2
```

#### Sample 2
```
Input:
Enter the string: rhythm

Output:
Alternating pairs: 0
```

#### Sample 3
```
Input:
Enter the string: hello

Output:
Alternating pairs: 3
```