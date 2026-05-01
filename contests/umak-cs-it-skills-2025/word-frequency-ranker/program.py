def word_frequency_ranker(k, text):
    # Implement:
    # 1) normalize (lowercase, remove punctuation)
    # 2) frequency count
    # 3) top k frequent (count desc, word asc)
    # 4) top k longest (length desc, word asc)
    # 5) count words with freq == 1
    # top_freq, top_len, unique_count
    
    text = text.split()
    for i, word in enumerate(text):
        text[i] = word.strip(".!?:;-").lower()

    from collections import Counter
    freq = Counter(text)

    top_freq = []
    for w, v in freq.most_common(k):
        top_freq.append((w, v))
    
    top_len = []
    freq = dict(sorted(dict(freq).items(), key=lambda x: len(x[0]), reverse=True))
    for w, v in freq.items()[:k]:
        top_len.append((w, v))
    
    unique_count = sum(1 for _, v in freq.items() if v == 1)

# ---------------- TESTS ----------------

def run_tests():
    # Sample 1
    k = 3
    text = "The quick brown fox jumps over the lazy dog. The dog was very lazy."
    
    top_freq, top_len, unique_count = word_frequency_ranker(k, text)
    
    assert top_freq == [("the", 3), ("dog", 2), ("lazy", 2)], f"Top freq incorrect: {top_freq}"
    assert top_len == [("brown", 5), ("jumps", 5), ("quick", 5)], f"Top len incorrect: {top_len}"
    assert unique_count == 5, f"Unique count incorrect: {unique_count}"


    # Sample 2
    k = 2
    text = "programming is fun and programming is challenging"
    
    top_freq, top_len, unique_count = word_frequency_ranker(k, text)
    
    assert top_freq == [("is", 2), ("programming", 2)], f"Top freq incorrect: {top_freq}"
    assert top_len == [("challenging", 11), ("programming", 11)], f"Top len incorrect: {top_len}"
    assert unique_count == 3, f"Unique count incorrect: {unique_count}"


    # Edge Case 1: all unique
    k = 3
    text = "a b c d e"
    
    top_freq, top_len, unique_count = word_frequency_ranker(k, text)
    
    assert unique_count == 5


    # Edge Case 2: punctuation + case
    k = 2
    text = "Hello, hello! HELLO?"
    
    top_freq, top_len, unique_count = word_frequency_ranker(k, text)
    
    assert top_freq == [("hello", 3)]
    assert unique_count == 0


    # Edge Case 3: ties in frequency
    k = 2
    text = "cat bat mat cat bat"
    
    top_freq, top_len, unique_count = word_frequency_ranker(k, text)
    
    assert top_freq == [("bat", 2), ("cat", 2)], f"Tie sort incorrect: {top_freq}"


    print("All tests passed!")


if __name__ == "__main__":
    run_tests()