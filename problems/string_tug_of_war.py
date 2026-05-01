"""
PROBLEM   : Weave Strings
DIFFICULTY: easy
PATTERN   : two pointers, string interleaving
TRIGGER   : interleave two strings character by character, zip-style merge
INTUITION : Step through both strings simultaneously, appending characters alternately
            from each until both are exhausted.
"""

def weave_strings(s1, s2):
    pass


def main():
    # sample cases
    assert weave_strings("ace", "bdf") == "abcdef"
    assert weave_strings("cat", "cow") == "cacotw"
    assert weave_strings("ax", "axy") == "aaxxy"

    # edge cases
    assert weave_strings("a", "a") == "aa"
    assert weave_strings("abc", "") == "abc"
    assert weave_strings("", "xyz") == "xyz"

    # prefix / tie behavior
    assert weave_strings("ab", "abc") == "aabbc"
    assert weave_strings("axa", "axb") == "aaxabxb"

    print("All tests passed.")


if __name__ == "__main__":
    main()