"""
PROBLEM   : Longest Substring Without Repeating Characters (exploratory)
DIFFICULTY: medium
PATTERN   : sliding window (variable)
TRIGGER   : no repeating characters, expand right, shrink left on duplicate
INTUITION : Expand r; track character frequencies. When a character count exceeds 1,
            shrink from l until the duplicate is removed. Track the max window size.
"""

s = "csvpcs"

l = 0
seen = {}

longest = 0
for r in range(len(s)):
    seen[s[r]] = seen.get(s[r],0)+1

    while seen[s[r]] > 1:
        seen[s[l]] -= 1
        l += 1

    longest = max(longest, r - l + 1)

print(longest)