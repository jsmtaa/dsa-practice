"""
PROBLEM   : Caesar Cipher (exploratory)
DIFFICULTY: easy
PATTERN   : string transformation
TRIGGER   : shift letters by k, modulo wrapping, preserve case, non-alpha pass-through
INTUITION : For each alpha character, shift its alphabet position by k using modulo 26.
            Preserve original case; pass non-alpha characters through unchanged.
"""

s = "abcdefghijklmnop-qrstuvwxyz"
k = 3
# map to the letter of the alphabet
# convert the map to char
o = "".join(c if not c.isalpha() else
            (chr((ord(c) - ord('a' if c.lower()==c else 'A') + k) % 26 
             + ord('a' if c.lower()==c else 'A')))
            for c in s)

print(o)