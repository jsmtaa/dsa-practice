def is_isogram(s):
    seen = {}
    s = ''.join(c.lower() for c in s)

    for i in range(len(s)):
        if s[i] in seen:
            return "Output: Not an isogram"
        seen[s[i]] = 1
    return "Output: Isogram"


def main():
    assert is_isogram("background") == "Output: Isogram"
    assert is_isogram("hello") == "Output: Not an isogram"
    assert is_isogram("Alphabet") == "Output: Not an isogram"
    print("All tests passed.")


if __name__ == "__main__":
    main()