class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curBuy, maxP = sys.maxsize, 0

        for i in range(len(prices)):
            if prices[i] < curBuy:
                curBuy = prices[i]
                continue
            maxP = max(maxP, prices[i] - curBuy)
        
        return maxP