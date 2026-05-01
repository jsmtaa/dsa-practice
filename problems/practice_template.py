# 1. Frequency Map (dict)
def freq_map_dict(arr):
  return

# 2. Frequency Map (Counter)
def freq_map_counter(arr):
  return

# 3. Contains Duplicate
def contains_duplicate(nums):
  return
# 4. Two Sum
def two_sum(nums, target):
  return

# 5. Valid Anagram
def valid_anagram(s, t):
  return

def test_freq_map_dict():
    assert freq_map_dict([1,1,2,3,3,3]) == {1:2, 2:1, 3:3}
    assert freq_map_dict([]) == {}
    assert freq_map_dict([5]) == {5:1}

def test_freq_map_counter():
    assert freq_map_counter([1,1,2,3,3,3]) == {1:2, 2:1, 3:3}
    assert freq_map_counter([]) == {}
    assert freq_map_counter([5]) == {5:1}

def test_contains_duplicate():
    assert contains_duplicate([1,2,3,1]) == True
    assert contains_duplicate([1,2,3,4]) == False
    assert contains_duplicate([]) == False

def test_two_sum():
    res = two_sum([2,7,11,15], 9)
    assert sorted(res) == [0,1]

    res = two_sum([3,2,4], 6)
    assert sorted(res) == [1,2]

    res = two_sum([3,3], 6)
    assert sorted(res) == [0,1]

def test_valid_anagram():
    assert valid_anagram("anagram", "nagaram") == True
    assert valid_anagram("rat", "car") == False
    assert valid_anagram("", "") == True


def run_all_tests():
    test_freq_map_dict()
    test_freq_map_counter()
    test_contains_duplicate()
    test_two_sum()
    test_valid_anagram()
    print("All tests passed.")


if __name__ == "__main__":
    run_all_tests()