"""
PROBLEM   : Top K Frequent Elements (LC #347)
DIFFICULTY: medium
PATTERN   : hashing, heap
TRIGGER   : k most frequent elements, frequency count, top-k
INTUITION : Count frequencies with Counter, then use most_common(k) to extract the k
            elements with the highest counts in O(n log k).
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        return [x[0] for x in Counter(nums).most_common(k)]
      
      


def main():
    nums = [1,1,1,2,2,3]
    k = 2
    print(Solution().topKFrequent(nums, k))

if __name__ == "__main__":
    main()
        
        