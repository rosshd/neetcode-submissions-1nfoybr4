class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lengths = {}
        best = 0

        for n in nums:
            if n in lengths:
                continue

            left = lengths.get(n - 1, 0)
            right = lengths.get(n + 1, 0)
            total = left + 1 + right

            best = max(best, total)

            # The merged run goes from start to end:
            start = n - left
            end = n + right

            # Store the run length at the boundaries (and at n if you want, but not required)
            lengths[start] = total
            lengths[end] = total
            lengths[n] = total  # optional, but convenient for duplicate check above

        return best