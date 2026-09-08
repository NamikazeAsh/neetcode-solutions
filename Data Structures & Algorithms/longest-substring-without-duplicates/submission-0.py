class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        result = 0
        charS = set()

        if len(s)==0:
            return 0

        if len(s)==1:
            return 1

        for r in range(len(s)):
            while s[r] in charS:
                charS.remove(s[l])
                l+=1
            charS.add(s[r])
            result = max(result,(r-l)+1)
        return result