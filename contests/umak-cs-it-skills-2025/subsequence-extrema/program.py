def subsequence_extrema(s, k):
    # Implement lexicographically smallest and largest subsequence of length k
    pass


# ---------------- TESTS ----------------

def run_tests():
    # Basic test
    s = "abcde"
    k = 3
    
    smallest, largest = subsequence_extrema(s, k)
    
    assert smallest == "abc", f"Smallest incorrect: {smallest}"
    assert largest == "cde", f"Largest incorrect: {largest}"


    # Mixed order
    s = "bdac"
    k = 2
    
    smallest, largest = subsequence_extrema(s, k)
    
    assert smallest == "ac", f"Smallest incorrect: {smallest}"
    assert largest == "dc", f"Largest incorrect: {largest}"


    # All same characters
    s = "aaaaa"
    k = 3
    
    smallest, largest = subsequence_extrema(s, k)
    
    assert smallest == "aaa"
    assert largest == "aaa"


    # k = 1
    s = "zxy"
    k = 1
    
    smallest, largest = subsequence_extrema(s, k)
    
    assert smallest == "x"
    assert largest == "z"


    # k = len(s)
    s = "bac"
    k = 3
    
    smallest, largest = subsequence_extrema(s, k)
    
    assert smallest == "bac"
    assert largest == "bac"


    # Edge Case: decreasing string
    s = "zyxwv"
    k = 2
    
    smallest, largest = subsequence_extrema(s, k)
    
    assert smallest == "wv"
    assert largest == "zy"


    print("All tests passed!")


if __name__ == "__main__":
    run_tests()