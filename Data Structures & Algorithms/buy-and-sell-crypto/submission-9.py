class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        l = 0

        for r in range(len(prices)):

            maxp = max(maxp, prices[r] - prices[l])

            if prices[l] > prices[r]:
                l = r    
            r += 1    
        
        return maxp