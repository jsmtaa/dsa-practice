"""
PROBLEM   : 2D Prefix Sum with Range Queries
DIFFICULTY: medium
PATTERN   : prefix sum (2D)
TRIGGER   : submatrix sum, O(1) query, 2D grid, range (r1,c1)→(r2,c2)
INTUITION : Build a (m+1)×(n+1) prefix table with a sentinel zero border.
            Query (r1,c1,r2,c2) = p[r2+1][c2+1] - p[r1][c2+1] - p[r2+1][c1] + p[r1][c1].
"""

matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]

def main():
    prefix = getPrefix(matrix)
    displayPrefix(prefix)
    #           r1, c1, r2, c2
    queries =  (0,  0,  4,  4)

    response = query(prefix, queries[0], queries[1], queries[2], queries[3])

    print(response) 

def getPrefix(m):
    sr,sc=len(m)+1,len(m[0])+1
    p = [[0] * sc for _ in range(sr)]

    for r in range(1, sr):
        for c in range(1, sc):
            p[r][c] = m[r-1][c-1] + p[r-1][c] + p[r][c-1] - p[r-1][c-1]

    return p

def displayPrefix(prefix):
    max_width = max(len(str(prefix[i][j])) for i in range(len(prefix)) for j in range(len(prefix[0])))
    
    for i in range(len(prefix)):
        if i == 0:
            print("⎡", end=" ")
        elif i == len(prefix) - 1:
            print("⎣", end=" ")
        else:
            print("⎢", end=" ")
        
        for j in range(len(prefix[0])):
            print(str(prefix[i][j]).rjust(max_width), end="  ")
        
        if i == 0:
            print("⎤")
        elif i == len(prefix) - 1:
            print("⎦")
        else:
            print("⎥")

def query(p, r1, c1, r2, c2):
    return (p[r2+1][c2+1] 
            - p[r1][c2+1] # top
            - p[r2+1][c1] # left
            + p[r1][c1]) # topleft

main()