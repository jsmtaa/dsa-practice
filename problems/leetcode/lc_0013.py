"""
PROBLEM   : Roman to Integer
DIFFICULTY: easy
PATTERN   : greedy, string traversal
TRIGGER   : Roman numeral, convert to integer, subtractive notation (IV, IX)
INTUITION : Check each position for a two-character subtractive pair first; if found, add its
            value and skip two characters. Otherwise add the single character's value.
"""

import sys


roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

roman_pairs = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}

s = sys.argv[1]

i = 0
sum = 0
while i < len(s):
    #print("i:", i, "char:", s[i])

    last_index = len(s) - 1
    # Avoids the last index at all costs to check for pairs, 
    # then performs [1] if no pairs are discovered
    if i != last_index:
        pair = s[i] + s[i+1]
        if pair in roman_pairs:
            #print(f"s[{i}]: {s[i]} + s[{i+1}]: {s[i+1]}")
            sum += roman_pairs.get(pair)
            i += 2
            continue  

    # [1]
    sum += roman.get(s[i])
    i += 1

print(sum)

