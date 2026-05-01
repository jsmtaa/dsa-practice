String Compression Engine

### Description
Implement a string compression algorithm that replaces consecutive identical characters with the character followed by the count. However, only compress if it saves space. If the compressed version is not shorter than the original, return the original string.

Additionally, implement the decompression algorithm that can reverse this process.

### Input
- First line: Operation type ("compress" or "decompress")
- Second line: String to process (1 ≤ length ≤ 1000)

### Output
- The processed string
- "Compression ratio: X%" (only for compression, where X is percentage saved)

### Sample Test Cases

#### Sample 1
```
Input:
compress
aabcccccaaa

Output:
a2b1c5a3
Compression ratio: 27.27%
```

#### Sample 2
```
Input:
compress
abcdef

Output:
abcdef
Compression ratio: 0.00%
```

#### Sample 3
```
Input:
decompress
a2b1c5a3

Output:
aabcccccaaa
```

#### Sample 4
```
Input:
compress
aaaaaaaaaa

Output:
a10
Compression ratio: 70.00%
```

---