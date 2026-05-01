# 1. Frequency Map (dict)
# Variation: return element with highest frequency (not the map)
def most_frequent_element(arr):
    # return the element that appears most
    f={}
    mx=0
    r=None
    for x in arr:
      f[x]=f.get(x,0)+1
      if f[x] > mx:
        mx=f[x]
        r=x    
    return r


# 2. Frequency Map (Counter)
# Variation: return list of elements that appear exactly k times
def elements_with_k_frequency(arr, k):
    # return list (order doesn't matter)
    from collections import Counter as C
    
    return [x[0] for x in dict(C(arr)).items() if x[1] == k]


# 3. Contains Duplicate
# Variation: return first duplicate encountered (not just True/False)
def first_duplicate(nums):
    # return the first value that appears twice
    # return None if no duplicate
    s=set()
    for x in nums:
      if x in s:
        return x
      s.add(x)
    return None

# 4. Two Sum
# Variation: return True/False instead of indices
def has_pair_with_sum(nums, target):
    # return True if any pair sums to target
    s=set()
    for x in nums:
      cp=target-x
      if cp in s:
        return True
      s.add(x)
    return False

# 5. Valid Anagram
# Variation: ignore spaces and case
def valid_anagram_loose(s, t):
    # ignore spaces and uppercase/lowercase
    s=[c.lower() for c in s if c.isalnum()]
    t=[c.lower() for c in t if c.isalnum()]
    from collections import Counter as C
    return C(s) == C(t)


# ================= TESTS =================

def test_most_frequent_element():
    assert most_frequent_element([1,1,2,3,3,3]) == 3
    assert most_frequent_element([5]) == 5
    assert most_frequent_element([1,2,2,3]) == 2

def test_elements_with_k_frequency():
    assert sorted(elements_with_k_frequency([1,1,2,3,3,3], 2)) == [1]
    assert sorted(elements_with_k_frequency([1,1,2,2,3], 2)) == [1,2]
    assert elements_with_k_frequency([], 1) == []

def test_first_duplicate():
    assert first_duplicate([1,2,3,1]) == 1
    assert first_duplicate([1,2,3,4]) == None
    assert first_duplicate([2,2,2]) == 2

def test_has_pair_with_sum():
    assert has_pair_with_sum([2,7,11,15], 9) == True
    assert has_pair_with_sum([1,2,3], 7) == False
    assert has_pair_with_sum([3,3], 6) == True

def test_valid_anagram_loose():
    assert valid_anagram_loose("anagram", "nagaram") == True
    assert valid_anagram_loose("Dormitory", "Dirty room") == True
    assert valid_anagram_loose("rat", "car") == False


def run_all_tests():
    test_most_frequent_element()
    test_elements_with_k_frequency()
    test_first_duplicate()
    test_has_pair_with_sum()
    test_valid_anagram_loose()
    print("All tests passed.")


if __name__ == "__main__":
    run_all_tests()