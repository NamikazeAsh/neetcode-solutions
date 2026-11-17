class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds,dt = {},{}

        for i in s:
            ds[i] = ds.get(i,0) + 1
        
        for j in t:
            dt[j] = dt.get(j,0) + 1
        
        if ds==dt:
            return True
        return False