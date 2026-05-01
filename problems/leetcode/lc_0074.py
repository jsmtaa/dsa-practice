"""
PROBLEM   : Search a 2D Matrix
DIFFICULTY: medium
PATTERN   : binary search
TRIGGER   : sorted matrix, row-major order, search target in O(log mn)
INTUITION : Treat the m×n matrix as a flattened sorted array of length m*n. Standard binary
            search with index translation: row = mid // n, col = mid % n.
"""

matrix = [
    [1 , 3 , 5 , 7 ],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
    ]
target = 3

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == target:
            print(True)
            exit()

print(False)