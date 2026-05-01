def zigzag_transform(arr):
    l = 0
    for r in range(1, len(arr)):
        if arr[l] > arr[r]:
            l += 1
            continue
        if arr[r] < arr[l]:


def main():
    assert zigzag_transform([1,2,3,4,5]) == (2, [2,1,4,3,5])
    assert zigzag_transform([4,3,7,8,6,2,1]) == (2, [4,3,8,6,7,1,2])
    assert zigzag_transform([10,10,10,10]) == (0, [10,10,10,10])
    print("All tests passed.")


if __name__ == "__main__":
    main()