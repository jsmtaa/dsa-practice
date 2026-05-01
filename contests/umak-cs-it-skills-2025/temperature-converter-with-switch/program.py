def temperature_convert(choice, value):
    pass


def main():
    assert temperature_convert(1, 25.0) == 77.00
    assert temperature_convert(2, 0.0) == 273.15
    assert temperature_convert(3, 32.0) == 0.00
    print("All tests passed.")


if __name__ == "__main__":
    main()