def transpose(matrix):
    pass


def main():
    m = [
        [1,2],
        [3,4],
        [5,6]
    ]
    assert transpose(m) == [
        [1,3,5],
        [2,4,6]
    ]
    print("All tests passed.")


if __name__ == "__main__":
    main()