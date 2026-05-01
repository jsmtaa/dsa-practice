"""
PROBLEM   : Remove Duplicates from Sorted Array
DIFFICULTY: easy
PATTERN   : two pointers
TRIGGER   : sorted in non-decreasing order
INTUITION : `write` is an anchor that stays still while `read` scans forward. Once `read` finds a value
            not equal to the anchor, shift by right by 1 and write its value there. Since the
            array is sorted, duplicates are always grouped, so comparing `read` against the anchor cleanly
            skips all of them without visiting each one.
"""

def removeDuplicates(nums):
    write = 0
    for read in range(1, len(nums)):
        if nums[read] != nums[write]:
            write += 1
            nums[write] = nums[read]
    print(nums)
    return write + 1