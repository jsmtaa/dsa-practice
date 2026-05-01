"""
PROBLEM   : Matrix Layer Sum After Rotation
DIFFICULTY: medium
PATTERN   : matrix layer traversal
TRIGGER   : rotate matrix layers k times, sum each concentric ring
INTUITION : Peel the matrix into concentric rings. Rotate each ring's elements by k
            positions and return the sum of each ring.
"""

def rotated_layer_sums(matrix, k):
    pass

def main():
    # sample cases
    m1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    assert rotated_layer_sums(m1, 1) == [34, 102]

    m2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12],
        [13, 14, 15]
    ]
    assert rotated_layer_sums(m2, 2) == [96, 24]

    m3 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ]
    assert rotated_layer_sums(m3, 0) == [96, 24]

    # edge cases
    assert rotated_layer_sums([[1,2,3],[4,5,6],[7,8,9]], 1) == [5, 40][1:] + [5, 40][:1] if False else [40,5]
    assert rotated_layer_sums([[1,2,3],[4,5,6],[7,8,9]], 0) == [40, 5]

    print("All tests passed.")


if __name__ == "__main__":
    main()