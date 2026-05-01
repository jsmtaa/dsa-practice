"""
PROBLEM   : Format String Validator
DIFFICULTY: medium
PATTERN   : greedy, string parsing
TRIGGER   : ordered placeholders (%d < %f < %c < %s), escape sequences, validate
INTUITION : Scan the string. For each placeholder, verify it is not out of order relative
            to the last seen type. For each escape sequence, verify it is one of the
            allowed forms (\\n, \\t, \\\\, \\"). Return INVALID on any violation.
"""

def is_valid_format(s):
    order = {'d': 0, 'f': 1, 'c': 2, 's': 3}
    max_seen = -1
    i = 0
    n = len(s)

    while i < n:
        ch = s[i]

        # handle placeholders
        if ch == '%':
            if i + 1 >= n or s[i + 1] not in order:
                return "INVALID"
            curr = order[s[i + 1]]
            if curr < max_seen:
                return "INVALID"
            max_seen = curr
            i += 2
            continue

        # handle escape sequences
        if ch == '\\':
            if i + 1 >= n or s[i + 1] not in {'n', 't', '\\', '"'}:
                return "INVALID"
            i += 2
            continue

        i += 1

    return "VALID"


def main():
    # valid cases
    assert is_valid_format("Count: %d, Avg: %f, Grade: %c, Name: %s") == "VALID"
    assert is_valid_format("%d %d %f %c %s") == "VALID"
    assert is_valid_format("Line1\\nLine2\\tTabbed\\\\Backslash\\\"Quote") == "VALID"

    # invalid placeholder order
    assert is_valid_format("Error at %f, correcting with %d.") == "INVALID"

    # invalid placeholder type
    assert is_valid_format("Value: %x") == "INVALID"
    assert is_valid_format("Percent only %") == "INVALID"

    # invalid escape sequences
    assert is_valid_format("This is an invalid escape: \\z.") == "INVALID"
    assert is_valid_format("Bad escape at end \\") == "INVALID"

    # mixed invalid
    assert is_valid_format("%d %c %f") == "INVALID"  # wrong order

    print("All tests passed.")


if __name__ == "__main__":
    main()