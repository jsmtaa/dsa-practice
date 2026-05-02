"""
PROBLEM   : Letter Combinations of a Phone Number
DIFFICULTY: medium
PATTERN   : backtracking
TRIGGER   : digit string, all letter combinations, phone keypad
INTUITION : For each digit, try every letter it maps to, then move on to the next digit. Once
            you've picked a letter for every digit, you've built a valid combination.
"""

def letterCombinations(digits: str) -> list[str]:

    result = []
    letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz", 
    } 

    def backtrack(index, path):
        # Base case
        if len(path) == len(digits):
            result.append("".join(path[:]))
            return
        
        # Subset
        # Choose the digit or not
        for letter in letters[digits[index]]: # "digit": "letters"
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result