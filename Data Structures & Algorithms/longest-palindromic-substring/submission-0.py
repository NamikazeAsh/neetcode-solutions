class Solution:
    def longestPalindrome(self, s: str) -> str:
        lp_index = 0
        lp_len = 0

        for i in range(len(s)):
            #for odd
            l,r = i,i
            while (l>=0) and r<len(s) and s[l] == s[r]:
                if (r-l+1) > lp_len:
                    lp_len = r-l+1
                    lp_index = l
                l-=1
                r+=1
            

            #for even
            l,r = i,i+1
            while (l>=0) and r<len(s) and s[l] == s[r]:
                if (r-l+1) > lp_len:
                    lp_len = r-l+1
                    lp_index = l
                l-=1
                r+=1
            
        return s[lp_index:lp_index+lp_len]
