def pascal_triangle(n):
    pass


def main():
    assert pascal_triangle(1) == "1"

    assert pascal_triangle(2) == (
        "1\n"
        "1 1"
    )

    assert pascal_triangle(4) == (
        "1\n"
        "1 1\n"
        "1 2 1\n"
        "1 3 3 1"
    )

    print("All tests passed.")


if __name__ == "__main__":
    main()