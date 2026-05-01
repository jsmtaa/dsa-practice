"""
PROBLEM   : Digital Root Calculator
DIFFICULTY: easy
PATTERN   : math, modulo
TRIGGER   : sum digits repeatedly until single digit, digital root
INTUITION : Formula: digital_root(n) = 1 + (n - 1) % 9 for n > 0, else 0.
            Avoids iterating through digits entirely.
"""

def digital_root(n):
    # O(1) formula using modulo 9
    pass     

def main():
    # core cases
    assert digital_root(123) == 6
    assert digital_root(9875) == 2
    assert digital_root(9) == 9

    # edge cases
    assert digital_root(1) == 1
    assert digital_root(10) == 1
    assert digital_root(11) == 2

    # larger numbers
    assert digital_root(999999999) == 9
    assert digital_root(1000000000) == 1

    # random checks
    assert digital_root(38) == 2   # 3+8=11 → 1+1=2
    assert digital_root(4444) == 7 # 4+4+4+4=16 → 1+6=7

    print("All tests passed.")


if __name__ == "__main__":
    main()