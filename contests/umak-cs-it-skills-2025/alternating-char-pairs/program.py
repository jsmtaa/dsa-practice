def alternating_pairs(s):
    # prefix transform
    pref = [0]
    vowels = set("aeiou")
    for c in s:
        pref.append(pref[-1] + (1 if c in vowels else -1))

    l = 0
    c = 0
    for r in range(1, len(s)):
        if pref[r+1] - pref[l] == 0:
            c += 1
        l += 1
    return c

def main():
    assert alternating_pairs("apple") == 2
    assert alternating_pairs("rhythm") == 0
    assert alternating_pairs("hello") == 3
    print("All tests passed.")


if __name__ == "__main__":
    main()