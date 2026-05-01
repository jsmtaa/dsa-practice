def student_records(data):
    pass


def main():
    data = [
        ("Alice", [85, 90, 88]),
        ("Bob", [78, 82, 80]),
        ("Charlie", [92, 95, 93])
    ]

    result = student_records(data)

    assert result == (
        "Alice: 87.67\n"
        "Bob: 80.00\n"
        "Charlie: 93.33\n"
        "Class Average: 87.00"
    )

    print("All tests passed.")


if __name__ == "__main__":
    main()