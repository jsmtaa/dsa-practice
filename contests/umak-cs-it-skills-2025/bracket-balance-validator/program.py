def validate_brackets(s):
    pass


def main():
    assert validate_brackets("{[()]}") == "Valid\nMax Depth: 3"
    assert validate_brackets("{[(])}") == "Invalid"
    assert validate_brackets("((()))[]{}") == "Valid\nMax Depth: 3"
    print("All tests passed.")


if __name__ == "__main__":
    main()