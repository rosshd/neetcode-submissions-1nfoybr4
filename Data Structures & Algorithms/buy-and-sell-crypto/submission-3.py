class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        most = 0

        l, r = 0,1

        while r < len(prices):
            if prices[r] < prices[l]:
                l, r = r, r+1
                continue
            most = max(prices[r] - prices[l],most)
            r += 1
        return most
              

        