def longest_palindrome(s):

    res = ""
    resLen = 0
    c = 0
    for i in range(len(s)):
        
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            c += 1
            if r - l + 1 > resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            l -= 1
            r += 1
            
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            c += 1
            if r - l + 1 > resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            l -= 1
            r += 1

    return (res, resLen, c)

def main():
    assert longest_palindrome("babad") == ("bab", 3, 7)
    assert longest_palindrome("cbbd") == ("bb", 2, 5)
    assert longest_palindrome("racecar") == ("racecar", 7, 10)
    print("All tests passed.")


if __name__ == "__main__":
    main()