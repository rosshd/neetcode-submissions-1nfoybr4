class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #["act","pots","tops","cat","stop","hat"]
        #to
        #[["hat"],["act", "cat"],["stop", "pots", "tops"]]
        anagrams = {}
        out = []
        index = 0
        
        for i, s in enumerate(strs):
            tempString = str(sorted(s))
            if anagrams.get(tempString, -1) == -1:
                anagrams[tempString] = index
                out.append([s])
                index += 1
            else:
                out[anagrams[tempString]].append(s)

        return out


              
                