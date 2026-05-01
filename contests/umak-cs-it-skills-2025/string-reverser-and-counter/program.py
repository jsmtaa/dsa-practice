def reverse_and_count(s):
    return f"Reversed: {s[::-1]}\nVowels: {sum(1 for c in s if c in set("aeiou"))}"
    

def main():
    assert reverse_and_count("CodeChum") == "Reversed: muhCedoC\nVowels: 3"
    assert reverse_and_count("hello") == "Reversed: olleh\nVowels: 2"
    assert reverse_and_count("xyz") == "Reversed: zyx\nVowels: 0"
    print("All tests passed.")


if __name__ == "__main__":
    main()