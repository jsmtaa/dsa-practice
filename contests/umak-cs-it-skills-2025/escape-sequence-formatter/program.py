def receipt(items):
    pass


def main():
    data = [
        ("Apple", 5, 20.50),
        ("Banana", 10, 15.00),
        ("Orange", 3, 25.75)
    ]
    result = receipt(data)
    assert "GRAND TOTAL" in result
    print("All tests passed.")


if __name__ == "__main__":
    main()