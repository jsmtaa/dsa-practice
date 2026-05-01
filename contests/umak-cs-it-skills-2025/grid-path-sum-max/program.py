def max_path_sum(grid):
    pass


def main():
    g1 = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
    assert max_path_sum(g1) == 12

    g2 = [
        [5,1],
        [2,10]
    ]
    assert max_path_sum(g2) == 17

    print("All tests passed.")


if __name__ == "__main__":
    main()