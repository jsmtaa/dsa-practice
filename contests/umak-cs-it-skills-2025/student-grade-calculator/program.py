def student_grade(a, b, c):
    pass


def main():
    assert student_grade(85, 90, 78) == ("Average: 84.33", "Result: Passed")
    assert student_grade(70, 70, 70) == ("Average: 70.00", "Result: Failed")
    print("All tests passed.")


if __name__ == "__main__":
    main()