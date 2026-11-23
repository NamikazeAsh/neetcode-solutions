class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        
        l=0
        res=0

        for i in range(len(s)):
            #not in seen
            if s[i] not in seen:
                seen.add(s[i])
                res=max(len(seen),res)
            #in seen
            else: 
                while l<i:
                    if s[l] in seen:
                        seen.remove(s[l])
                        if s[l]==s[i]:
                            seen.add(s[i])
                            l+=1
                            break
                    l+=1
        return res
                 






























        # l = 0
        # result = 0
        # charS = set()

        # if len(s)==0:
        #     return 0

        # if len(s)==1:
        #     return 1

        # for r in range(len(s)):
        #     while s[r] in charS:
        #         charS.remove(s[l])
        #         l+=1
        #     charS.add(s[r])
        #     result = max(result,(r-l)+1)
        # return result