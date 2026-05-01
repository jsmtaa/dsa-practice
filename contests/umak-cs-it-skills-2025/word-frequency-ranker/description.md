# Word Frequency Ranker

### Description
Given a paragraph of text, analyze the word frequencies and generate a report. Consider words case-insensitively and ignore punctuation. Words are separated by spaces.

Generate:
1. Top K most frequent words with their counts
2. Top K longest words with their lengths
3. Words that appear exactly once (hapax legomena)

### Input
- First line: Integer K (1 ≤ K ≤ 20)
- Second line: A string representing the paragraph (1 ≤ length ≤ 5000)

### Output
- First K lines: "word: count" (most frequent words, sorted by count descending, then alphabetically)
- Next K lines: "word: length" (longest words, sorted by length descending, then alphabetically)
- Next line: "Unique words: X" where X is count of words appearing exactly once

### Sample Test Cases

#### Sample 1
```
Input:
3
The quick brown fox jumps over the lazy dog. The dog was very lazy.

Output:
the: 3
lazy: 2
dog: 2
---
quick: 5
brown: 5
jumps: 5
---
Unique words: 5
```

#### Sample 2
```
Input:
2
programming is fun and programming is challenging

Output:
programming: 2
is: 2
---
programming: 11
challenging: 11
---
Unique words: 3
```

---