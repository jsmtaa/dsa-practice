"""
PROBLEM   : 2D Prefix Sum Construction
DIFFICULTY: medium
PATTERN   : prefix sum (2D)
TRIGGER   : 2D grid, rectangular sum, precompute, avoid recomputing
INTUITION : prefix[r][c] = matrix[r][c] + prefix[r-1][c] + prefix[r][c-1] - prefix[r-1][c-1].
            The subtraction removes the doubly-counted top-left overlap.
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
"""
prefix = [
    [1,  3, 6],
    [5,  0, 0],
    [12, 0, 0]
]
cell = left + top - topleft

prefix = [
    [1,  3, 6],
    [5,  7, 0],
    [12, 14, 0]
]
"""
# [1][0]
prefix = [[0] * len(matrix[0]) for _ in range(len(matrix))]


# if on top, or on top left, calculate natin pababa or paright

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if row == 0 and col == 0:
            # Lahat ng top and left side should be computed first, kasi yun lang yung mapagkukuhaan natin ng sum initially
            prefix[0][0] = matrix[0][0]
        elif row == 0 and col != 0: # means it is on the top (horizontal) BUT not the first one
            prefix[row][col] = matrix[row][col] + prefix[row][col-1]
        elif col == 0 and row != 0: # means it is on the left (vertical) BUT not the first one
            prefix[row][col] = matrix[row][col] + prefix[row-1][col]
        else:
            prefix[row][col] = matrix[row][col] + prefix[row-1][col] + prefix[row][col-1] - prefix[row-1][col-1]
print(prefix)
