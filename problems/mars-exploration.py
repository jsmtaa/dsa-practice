"""
PROBLEM   : Mars Exploration (HackerRank)
DIFFICULTY: easy
PATTERN   : string traversal
TRIGGER   : SOS pattern, count altered characters in repeated SOS
INTUITION : Split the string into SOS triplets. For each triplet, count characters
            that differ from the expected S-O-S pattern.
"""

def marsExploration(s):
    # Write your code here]
    SOS = "SOS"
    count = 0
    l = 0
    for r in range(3, len(s) + 1, 3):
        for i in range(len(SOS)):
            if SOS[i] != SOS[l:r][i]:
                count += 1
        l += 3
    return count

s = "SOSSOSSOSSOS"

c = marsExploration(s)
print(c)