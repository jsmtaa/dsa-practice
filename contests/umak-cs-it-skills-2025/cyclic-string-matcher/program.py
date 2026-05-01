def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    for i in range(len(s2)):
        if s1[i:] + s1[:i] == s2:
            return True
    return False


def main():
    assert is_rotation("abcde", "cdeab") == True
    assert is_rotation("abc", "acb") == False
    assert is_rotation("a", "a") == True
    assert is_rotation("water", "terwa") == True
    print("All tests passed.")


if __name__ == "__main__":
    main()