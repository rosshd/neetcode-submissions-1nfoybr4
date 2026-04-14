class Solution:
        def trap(self, height: List[int]) -> int:
            l, r = 0, len(height) - 1
            maxL, maxR = 0, 0
            total = 0

            while l < r:
                # Update maxes seen so far
                maxL = max(maxL, height[l])
                maxR = max(maxR, height[r])

                # Process the side with the smaller max (the bottleneck)
                if maxL < maxR:
                    # Water trapped at l is maxL - height[l]
                    total += maxL - height[l]
                    l += 1
                else:
                    # Water trapped at r is maxR - height[r]
                    total += maxR - height[r]
                    r -= 1

            return total    