def fibonacci(n):
    pass


def main():
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
    print("All tests passed.")


if __name__ == "__main__":
    main()