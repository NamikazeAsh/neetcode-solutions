class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for w in strs:
            s+=str(len(w))+"#"+w
        print("encode",s)
        return s

    def decode(self, s: str) -> List[str]:
        result = []
        i=0

        while i<len(s):
            j=i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            result.append(s[j+1:j+1+length])
            i=j+1+length #move it to pt right after j
        return result