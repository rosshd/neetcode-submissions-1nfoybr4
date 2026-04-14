class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lengths = set(nums)
        best = 0

        for n in nums:
            if (n - 1) not in lengths:
                length = 0;
                while (n + length) in lengths:
                    length += 1
                best = max(length, best)
        return best