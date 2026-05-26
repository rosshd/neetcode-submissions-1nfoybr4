class Solution:
    def trap(self, height: List[int]) -> int:
        minHold, l, r = 0, 0, len(height) - 1
        res = 0
        while l < r:
            minHold = max(minHold, min(height[l], height[r]))
            if height[l] < height[r]:
                res += minHold - height[l]
                l += 1
            else:
                res += minHold - height[r]
                r -= 1
                   
        return res