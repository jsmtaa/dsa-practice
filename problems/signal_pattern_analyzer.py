"""
PROBLEM   : Signal Pattern Analyzer
DIFFICULTY: medium
PATTERN   : simulation, bitwise operations
TRIGGER   : index parity, value parity, XOR, bit shift, conditional transforms
INTUITION : For each element, pick one of four transforms based on (index parity, value parity).
            Count values exceeding the key, accumulate total, and track the max.
"""

def analyze_signals(arr, key):
    count = 0
    total = 0
    max_val = float('-inf')

    for i, s in enumerate(arr):
        if i % 2 == 0:
            if s % 2 == 0:
                val = (s + i) ^ (key & 255)
            else:
                val = (s - i) * (key >> 8)
        else:
            if s % 2 == 0:
                val = s + (key ^ (s & i))
            else:
                val = s - (key ^ (s | i))

        if val > key:
            count += 1

        total += val
        if val > max_val:
            max_val = val

    return count, total, max_val


def main():
    # sample cases
    assert analyze_signals([10, 21, 30, 43, 50], 300) == (0, -436, 38)
    assert analyze_signals([100, 200, 300, 400], 150) == (4, 1582, 550)
    assert analyze_signals([101, 201, 301, 401], 255) == (0, 184, 147)

    # edge cases
    assert analyze_signals([0], 0) == (0, 0, 0)
    assert analyze_signals([2], 1) == (1, ((2 + 0) ^ (1 & 255)), ((2 + 0) ^ (1 & 255)))

    # mixed
    assert analyze_signals([1, 2, 3, 4], 10)[0] >= 0  # sanity check
    assert isinstance(analyze_signals([5, 6, 7], 20), tuple)

    print("All tests passed.")


if __name__ == "__main__":
    main()