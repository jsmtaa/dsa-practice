def array_statistics(n, arr):
    # Implement sum, average, max, min
    return [sum(arr), sum(arr)/n, max(arr), min(arr)]
    
# ---------------- TESTS ----------------

def run_tests():
    # Sample Test
    n = 5
    arr = [10, 25, 8, 42, 15]
    
    total, avg, mx, mn = array_statistics(n, arr[:])
    
    assert total == 100, f"Sum incorrect: {total}"
    assert round(avg, 2) == 20.00, f"Average incorrect: {avg}"
    assert mx == 42, f"Max incorrect: {mx}"
    assert mn == 8, f"Min incorrect: {mn}"


    # Edge Case 1: Single element
    n = 1
    arr = [7]
    
    total, avg, mx, mn = array_statistics(n, arr[:])
    
    assert total == 7
    assert round(avg, 2) == 7.00
    assert mx == 7
    assert mn == 7


    # Edge Case 2: All equal
    n = 4
    arr = [5, 5, 5, 5]
    
    total, avg, mx, mn = array_statistics(n, arr[:])
    
    assert total == 20
    assert round(avg, 2) == 5.00
    assert mx == 5
    assert mn == 5


    # Edge Case 3: Negative numbers
    n = 5
    arr = [-10, -20, -3, -4, -5]
    
    total, avg, mx, mn = array_statistics(n, arr[:])
    
    assert total == -42
    assert round(avg, 2) == -8.40
    assert mx == -3
    assert mn == -20


    # Edge Case 4: Mixed values
    n = 6
    arr = [0, -1, 1, -2, 2, 3]
    
    total, avg, mx, mn = array_statistics(n, arr[:])
    
    assert total == 3
    assert round(avg, 2) == 0.50
    assert mx == 3
    assert mn == -2


    print("All tests passed!")


if __name__ == "__main__":
    run_tests()