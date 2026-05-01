"""
PROBLEM   : K-Palindrome Validator
DIFFICULTY: easy
PATTERN   : two pointers
TRIGGER   : palindrome, allow at most k mismatches, YES/NO
INTUITION : Squeeze l and r inward, counting mismatched pairs. If the count is ≤ k,
            the string can become a palindrome by fixing those pairs.
"""

def is_k_palindrome(s, k):
    l, r = 0, len(s) - 1
    c = 0
    while l <= r:
        if s[l] != s[r]:
            c+=1
        r -= 1
        l += 1
    return "YES" if c <= k else "NO"

def main():
    # core cases
    assert is_k_palindrome("racecar", 0) == "YES"
    assert is_k_palindrome("racecar", 2) == "YES"

    assert is_k_palindrome("apple", 1) == "NO"
    assert is_k_palindrome("apple", 2) == "YES"

    # edge cases
    assert is_k_palindrome("a", 0) == "YES"
    assert is_k_palindrome("ab", 0) == "NO"
    assert is_k_palindrome("ab", 1) == "YES"

    # mixed cases
    assert is_k_palindrome("abc", 0) == "NO"
    assert is_k_palindrome("abc", 1) == "YES"
    assert is_k_palindrome("abcd", 1) == "NO"
    assert is_k_palindrome("abcd", 2) == "YES"

    # already near-palindrome
    assert is_k_palindrome("abca", 1) == "YES"
    assert is_k_palindrome("abca", 0) == "NO"

    print("All tests passed.")


if __name__ == "__main__":
    main()