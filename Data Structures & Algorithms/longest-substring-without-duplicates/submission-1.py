class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_set = set()
        l, longest = 0, 0

        for r in range(len(s)):  # r is the right pointer
            while s[r] in char_set:  # duplicate found - contract window
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])  # add new character
            longest = max(longest, r - l + 1)  # update length

        return longest


