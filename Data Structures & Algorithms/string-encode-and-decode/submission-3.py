class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            encodedStr += (str(len(s)) + "#" + s)
        return encodedStr
    
    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        i = 0
        
        while i < len(s):
            if s[i] != "#":
                i += 1
                continue
            
            length = int(s[start:i])
            
            res.append(s[i+1 : i+1+length])
            
            start = i + 1 + length
            i = start
            
        return res