def string_ops(a, b):
    pass


def main():
    assert string_ops("Hello", "World") == (
        "HelloWorld",
        "Hello is shorter",
        "Hello comes first alphabetically"
    )
    print("All tests passed.")


if __name__ == "__main__":
    main()