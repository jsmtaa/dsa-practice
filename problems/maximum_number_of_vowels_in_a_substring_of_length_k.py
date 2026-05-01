"""
PROBLEM   : Maximum Number of Vowels in a Substring of Given Length (LC #1456)
DIFFICULTY: medium
PATTERN   : sliding window (fixed)
TRIGGER   : fixed window size k, count vowels, maximum count
INTUITION : Initialize vowel count for the first window. Slide right: add 1 if the
            incoming character is a vowel, subtract 1 if the departing character was.
            Track the max.
"""

s = "abciiidef"
k = 3

vow = sum([1 for c in s[:k] if c in "aeiou"])

max_vow = vow

for r in range(k, len(s)):
    vow += 1 if s[r] in "aeiou" else 0
    vow -= 1 if s[r-k] in "aeiou" else 0
    max_vow = max(vow,max_vow)

print(max_vow)