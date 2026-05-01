"""
PROBLEM   : Maximum Number of Vowels in a Substring of Given Length
DIFFICULTY: medium
PATTERN   : sliding window (fixed)
TRIGGER   : fixed window size k, count vowels, maximum count
INTUITION : Initialize vowel count for the first window. Slide right: add 1 if the incoming
            character is a vowel, subtract 1 if the departing character was. Track the max.
"""

s = "abciiidef"
k = 3

v = set("aeiou")
vow = sum(1 for c in s[:k] if c in "aeiou")


max_vow = vow

for r in range(k, len(s)):
    vow += s[r] in v
    vow -= s[r-k] in v
    max_vow = max(vow,max_vow)

print(max_vow)