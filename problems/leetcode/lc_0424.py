"""
PROBLEM   : Longest Repeating Character Replacement
DIFFICULTY: medium
PATTERN   : sliding window
TRIGGER   : replace at most k characters, longest substring with same character
INTUITION : Expand the window; a window is valid when (window size - count of most frequent
            char) ≤ k. Shrink from the left whenever the window becomes invalid.
"""

class Solution(object):
    def characterReplacement(self, s, k):
        l = 0
        seen = {}
        max_freq = 0
        res = 0

        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            max_freq = max(max_freq, seen[s[r]])

            while (r - l + 1) - max_freq > k:
                seen[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

def main():
    sol = Solution()

    # Core cases
    assert sol.characterReplacement("ABAB", 2) == 4
    assert sol.characterReplacement("AABABBA", 1) == 4

    # Edge cases
    assert sol.characterReplacement("AAAA", 2) == 4
    assert sol.characterReplacement("ABCDE", 1) == 2

    # Mixed
    assert sol.characterReplacement("BAAAB", 2) == 5
    assert sol.characterReplacement("ABBB", 2) == 4

    print("All tests passed!")


if __name__ == "__main__":
    main()