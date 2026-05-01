def matrix_collapse(n, k, matrix):
    pass


def main():
    n1, k1 = 3, 10
    m1 = [
        [4,6,1],
        [6,4,1],
        [1,1,1]
    ]
    assert matrix_collapse(n1, k1, m1) == (
        1,
        [
            [5,5,1],
            [5,5,1],
            [1,1,1]
        ]
    )

    n2, k2 = 4, 4
    m2 = [
        [2,2,2,2],
        [6,6,6,6],
        [1,1,1,1],
        [1,1,1,1]
    ]
    assert matrix_collapse(n2, k2, m2)[0] == 1

    print("All tests passed.")


if __name__ == "__main__":
    main()