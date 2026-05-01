def process_string(operation, s):
    from collections import Counter

    if operation == "compress":
        if Counter(s) == Counter(set(s)):
            return (s, "0.0")

        l = 0
        seen = {}
        res = []
        k = 0
        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            
            if len(seen) > 1:
                res.append(f"{s[r-1]}{seen[s[r-1]]}")
            
            while len(seen) > 1:
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    del seen[s[l]]
                l += 1
            r = k
        res.append(f"{s[k-1]}{seen[s[k-1]]}")

        res = ''.join(res)
        X = (len(s) - len(res))/len(s) * 100
        return (res, f"{X:.2f}")
    else:
        l = 0
        res = []
        for r in range(1, len(s), 2):
            res.append(s[l] * int(s[r]))
            l += 2
            print(res)
        return ''.join(res)


def main():
    print(process_string("compress", "abcdef"))
    assert process_string("compress", "aabcccccaaa") == ("a2b1c5a3", "27.27")
    assert process_string("compress", "abcdef") == ("abcdef", "0.0")
    assert process_string("decompress", "a2b1c5a3") == "aabcccccaaa"
    print("All tests passed.")


if __name__ == "__main__":
    main()