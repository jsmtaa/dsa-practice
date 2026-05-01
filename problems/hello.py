"""
PROBLEM   : Pangram Check (exploratory)
DIFFICULTY: easy
PATTERN   : hashing, sets
TRIGGER   : contains every letter of the alphabet, pangram
INTUITION : Convert the sentence to a set of lowercase characters. If the set contains
            all 26 letters, it is a pangram.
"""

s = "We promptly judged antique ivory buckles for the next prize"

alphabet = {chr(i) for i in range(ord('a'), ord('z')+1)}


s = set(s)
s.remove(' ')
print(alphabet)
print(set(s))
for c in s:
    if c not in alphabet:
        print(False)
        exit()


for i in range(len(s)):
    