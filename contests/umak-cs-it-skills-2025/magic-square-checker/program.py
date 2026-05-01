def is_magic_square(n, grid):
    # Implement magic square check + magic constant + 1..n^2 validation
    pass


# ---------------- TESTS ----------------

def run_tests():
    # Sample 1
    n = 3
    grid = [
        [2, 7, 6],
        [9, 5, 1],
        [4, 3, 8]
    ]
    
    is_magic, const, consecutive = is_magic_square(n, grid)
    
    assert is_magic == True, f"Should be magic: {is_magic}"
    assert const == 15, f"Constant incorrect: {const}"
    assert consecutive == True, f"Consecutive check failed: {consecutive}"


    # Sample 2
    n = 3
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    is_magic, const, consecutive = is_magic_square(n, grid)
    
    assert is_magic == False, f"Should NOT be magic: {is_magic}"
    assert const == 0, f"Constant should be 0: {const}"
    assert consecutive == False, f"Consecutive should be False: {consecutive}"


    # Sample 3
    n = 4
    grid = [
        [16, 2, 3, 13],
        [5, 11, 10, 8],
        [9, 7, 6, 12],
        [4, 14, 15, 1]
    ]
    
    is_magic, const, consecutive = is_magic_square(n, grid)
    
    assert is_magic == True
    assert const == 34
    assert consecutive == True


    # Edge Case 1: Duplicate values
    n = 3
    grid = [
        [2, 7, 6],
        [9, 5, 1],
        [4, 3, 7]  # duplicate 7
    ]
    
    is_magic, const, consecutive = is_magic_square(n, grid)
    
    assert is_magic == False


    # Edge Case 2: Correct sums but not consecutive
    n = 3
    grid = [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ]
    
    is_magic, const, consecutive = is_magic_square(n, grid)
    
    assert is_magic == False


    # Edge Case 3: Minimal size (2x2, impossible)
    n = 2
    grid = [
        [1, 2],
        [3, 4]
    ]
    
    is_magic, const, consecutive = is_magic_square(n, grid)
    
    assert is_magic == False


    print("All tests passed!")


if __name__ == "__main__":
    run_tests()