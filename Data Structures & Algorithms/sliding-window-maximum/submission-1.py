class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k: return []

        res, window = [], {}
        l = 0

        for r in range(k - 1):
            window[nums[r]] = 1 + window.get(nums[r], 0)
        
        for r in range(k - 1 , len(nums)):
            n = nums[r]
            window[n] = 1 + window.get(n, 0)

            res.append(max(window.keys()))

            window[nums[l]] -= 1
            if window[nums[l]] == 0:
                del window[nums[l]]  # critical!
            l += 1

        return res
