"""
PROBLEM   : Container With Most Water
DIFFICULTY: medium
PATTERN   : two pointers
TRIGGER   : maximize area, pair of heights, water container
INTUITION : Two pointers at the ends. Area = min(h[l], h[r]) * (r - l). Move the shorter
            pointer inward — that is the only side that could possibly improve the area.
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        largest = 0
        l, r = 0, len(height) - 1
        while l < r:
          area = min(height[l], height[r]) * (r - l)
          
          if height[l] > height[r]:
            r-=1
          else:
            l += 1
          largest = max(area, largest)
          
        return largest

def main():
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))
    
if __name__ == "__main__":
    main()
        
        