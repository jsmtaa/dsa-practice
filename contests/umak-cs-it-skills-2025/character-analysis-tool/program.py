def char_analysis(s):
    pass


def main():
    assert char_analysis("Hello World 2025!") == (2, 8, 4, 2)
    assert char_analysis("ABC") == (3, 0, 0, 0)
    print("All tests passed.")


if __name__ == "__main__":
    main()