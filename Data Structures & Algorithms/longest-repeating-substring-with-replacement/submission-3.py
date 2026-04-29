class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        maxCount = 0
        l = mlen = 0

        for r in range(len(s)):

            seen[s[r]] = 1 + seen.get(s[r], 0)

            if seen[s[r]] > maxCount:
                maxCount = seen[s[r]]

            while (r - l + 1) - maxCount > k:
                seen[s[l]] -= 1
                l += 1

            mlen = r - l + 1
        return mlen
            