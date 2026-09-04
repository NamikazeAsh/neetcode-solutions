class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        for i in s:
            if i not in d1:
                d1[i] = 0
            d1[i]+=1
        for j in t:
            if j not in d2:
                d2[j] = 0
            d2[j]+=1
        if d1==d2:
            return True
        else:
            return False