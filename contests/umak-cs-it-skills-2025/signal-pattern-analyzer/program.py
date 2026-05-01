def signal_pattern(arr):
    pass


def main():
    assert signal_pattern([1,2,3,2,1]) == "peak"
    assert signal_pattern([5,4,3,2]) == "decreasing"
    assert signal_pattern([1,2,3,4]) == "increasing"
    assert signal_pattern([1,3,2,4]) == "mixed"
    print("All tests passed.")


if __name__ == "__main__":
    main()