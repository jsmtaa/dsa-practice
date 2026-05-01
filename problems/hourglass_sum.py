"""
PROBLEM   : Hourglass Sum (HackerRank)
DIFFICULTY: easy
PATTERN   : 2D array traversal
TRIGGER   : hourglass shape, 6×6 grid, maximum sum
INTUITION : For each valid top-left position (r, c) where r < 4 and c < 4, compute the
            hourglass sum (top row + center + bottom row) and track the maximum.
"""

def hourglassSum(arr):
  max_sum = 0
  for r in range(4):
      for c in range(4):
        cur_sum = sum(arr[r][c:c+3]) + arr[r+1][c+1] + sum(arr[r+2][c:c+3])
        max_sum = max(max_sum, cur_sum)
  return max_sum
  
if __name__ == '__main__':
    arr = [
        [-9, -9, -9,  1, 1, 1],
        [ 0, -9,  0,  4, 3, 2],
        [-9, -9, -9,  1, 2, 3],
        [ 0,  0,  8,  6, 6, 0],
        [ 0,  0,  0, -2, 0, 0],
        [ 0,  0,  1,  2, 4, 0]
    ]

    result = hourglassSum(arr)
    print(result)
    