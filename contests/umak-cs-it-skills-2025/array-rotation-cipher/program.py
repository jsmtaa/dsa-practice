def array_rotation_cipher(n, arr, operations):
    # Take the rotations
    n = len(arr)

    net = 0
    for d, k in operations:
        if d == "L":
            net += k
        else:
            net -= k

    net %= n
    rotated = arr[net:] + arr[:net]
    
    res = []
    # Check prime indices
    for i in range(n):
        if i < 2:
            continue
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
    
        if is_prime:
            res.append(chr(rotated[i]))
    
    # Cipher
    return rotated, ''.join(res)

def run_tests():
    def check(test_id, n, arr, ops, expected_arr, expected_msg):
        result = array_rotation_cipher(n, arr[:], ops[:])
        if result is None:
            print(f"Test {test_id}: Function returned None")
            return

        final_arr, msg = result
        ok = (final_arr == expected_arr and msg == expected_msg)

        print(f"Test {test_id}: {'PASS' if ok else 'FAIL'}")
        if not ok:
            print("  Expected array:", expected_arr)
            print("  Got array     :", final_arr)
            print("  Expected msg  :", expected_msg)
            print("  Got msg       :", msg)
        print()

    # Test Case 1
    check(
        1,
        7,
        [72, 101, 108, 108, 111, 33, 65],
        [('R', 2)],
        [33, 65, 72, 101, 108, 108, 111],
        "Hel"
    )

    # Test Case 2
    check(
        2,
        10,
        [65, 66, 72, 101, 70, 108, 80, 108, 90, 111],
        [],
        [65, 66, 72, 101, 70, 108, 80, 108, 90, 111],
        "Hell"
    )

    # Test Case 3
    check(
        3,
        8,
        [97, 98, 99, 100, 101, 102, 103, 104],
        [('L', 2), ('R', 1)],
        [98, 99, 100, 101, 102, 103, 104, 97],
        "dega"
    )

    # Test Case 4
    check(
        4,
        6,
        [65, 66, 67, 68, 69, 70],
        [('R', 3)],
        [68, 69, 70, 65, 66, 67],
        "FAC"
    )


def main():
    run_tests()


if __name__ == "__main__":
    main()

