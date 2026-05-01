# Signal Pattern Analyzer

### Description
You are developing a Signal Pattern Analyzer. The program must process a sequence of integer signals based on a secret key. The transformation rule depends on both the signal's value and its position (index) in the sequence.

### Transformation Logic

**For each signal at an even index (0, 2, 4, ...):**
- If the signal value is even, the transformed value is `signal + key`
- If the signal value is odd, the transformed value is `signal - key`

**For each signal at an odd index (1, 3, 5, ...):**
- If the signal value is divisible by 3, the transformed value is `signal XOR key` (bitwise XOR)
- Otherwise, the signal remains unchanged

After transforming all signals, you need to analyze the results. Your program must count how many of the transformed signals are strictly positive (> 0) and calculate their sum.

### Input
- The first line contains an integer N, the number of signals (1 ≤ N ≤ 100)
- The second line contains N space-separated integers, representing the signals (-1000 ≤ signal[i] ≤ 1000)
- The third line contains an integer key (1 ≤ key ≤ 100)

### Output
- The first line should print `Transformed Signals:` followed by the array of transformed signals, separated by spaces
- The second line should print `Valid Signals Count:` followed by the count of positive transformed signals
- The third line should print `Sum of Valid Signals:` followed by the sum of all positive transformed signals

### Sample Test Cases

#### Sample 1
```
Input:
Enter the number of signals: 5
Enter the signals: 10 21 30 7 50
Enter the key: 10

Output:
Transformed Signals: 20 31 40 7 60
Valid Signals Count: 5
Sum of Valid Signals: 158
```

#### Sample 2
```
Input:
Enter the number of signals: 4
Enter the signals: 5 10 -15 30
Enter the key: 20

Output:
Transformed Signals: -15 10 -35 10
Valid Signals Count: 2
Sum of Valid Signals: 20
```

#### Sample 3
```
Input:
Enter the number of signals: 6
Enter the signals: 1 9 2 12 3 15
Enter the key: 42

Output:
Transformed Signals: -41 35 44 38 -39 37
Valid Signals Count: 4
Sum of Valid Signals: 154
```

---
