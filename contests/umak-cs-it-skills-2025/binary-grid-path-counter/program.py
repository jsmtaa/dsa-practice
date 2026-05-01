def binary_grid_paths(n, m, grid):
    # Implement path counting + max path sum (right/down moves only)
    pass


# ---------------- TESTS ----------------

def run_tests():
    # Sample 1
    n, m = 3, 3
    grid = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    
    paths, max_sum = binary_grid_paths(n, m, grid)
    
    assert paths == 2, f"Paths incorrect: {paths}"
    assert max_sum == 7, f"Max sum incorrect: {max_sum}"


    # Sample 2
    n, m = 3, 4
    grid = [
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1]
    ]
    
    paths, max_sum = binary_grid_paths(n, m, grid)
    
    assert paths == 1, f"Paths incorrect: {paths}"
    assert max_sum == 9, f"Max sum incorrect: {max_sum}"


    # Sample 3 (no path)
    n, m = 2, 2
    grid = [
        [1, 0],
        [0, 1]
    ]
    
    paths, max_sum = binary_grid_paths(n, m, grid)
    
    assert paths == 0, f"Paths incorrect: {paths}"
    assert max_sum == 0, f"Max sum incorrect: {max_sum}"


    # Edge Case 1: Single path straight line
    n, m = 1, 4
    grid = [[1, 2, 3, 4]]
    
    paths, max_sum = binary_grid_paths(n, m, grid)
    
    assert paths == 1
    assert max_sum == 10


    # Edge Case 2: All blocked except start
    n, m = 3, 3
    grid = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    
    paths, max_sum = binary_grid_paths(n, m, grid)
    
    assert paths == 0
    assert max_sum == 0


    # Edge Case 3: All ones (combinatorics paths)
    n, m = 3, 3
    grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    
    paths, max_sum = binary_grid_paths(n, m, grid)
    
    assert paths == 6  # C(4,2)
    assert max_sum == 5  # path length = 5 cells


    print("All tests passed!")


if __name__ == "__main__":
    run_tests()