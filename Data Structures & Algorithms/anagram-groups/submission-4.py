class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:

            content = [0] * 26

            for c in s:
                content[ord(c) - ord('a')] += 1
            
            res[tuple(content)].append(s)
        
        return list(res.values())