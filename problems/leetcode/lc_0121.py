"""
PROBLEM   : Best Time to Buy and Sell Stock
DIFFICULTY: easy
PATTERN   : sliding window, two pointers
TRIGGER   : buy low sell high, one transaction, maximize profit
INTUITION : Left pointer tracks the minimum price seen so far. For each day, check if
            selling today beats max profit. If today's price is lower than left, shift
            left here — there is no point buying on a day we cannot beat.
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=0
        mp=0
        for r in range(1, len(prices)):
          if prices[r] > prices[l]:
            p=prices[r]-prices[l]
            mp=max(mp,p)
          else:
            l=r
        return mp
def main():
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))
    
if __name__ == "__main__":
    main()
        
        