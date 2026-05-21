class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s, longest=set(nums), 0
        for n in s:
            if n - 1 in s:
                continue
            l = 1
            while n + l in s:
                l += 1
            longest = max(l, longest)
        return longest
            
                