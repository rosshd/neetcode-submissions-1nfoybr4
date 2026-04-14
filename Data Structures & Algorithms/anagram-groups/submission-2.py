class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #["act","pots","tops","cat","stop","hat"]
        #to
        #[["hat"],["act", "cat"],["stop", "pots", "tops"]]
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)
        
        return list(res.values())