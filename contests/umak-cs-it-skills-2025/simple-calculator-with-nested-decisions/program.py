def calculator(a, b, op):
    pass


def main():
    assert calculator(10, 5, '+') == "Result: 15.00"
    assert calculator(10, 0, '/') == "Error: Division by zero"
    assert calculator(10, 3, '%') == "Result: 1.00"
    print("All tests passed.")


if __name__ == "__main__":
    main()