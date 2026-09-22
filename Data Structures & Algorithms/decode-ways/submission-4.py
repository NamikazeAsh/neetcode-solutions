class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0]=="0":
            return 0
        if len(s)==1:
            return 1
        
        n = len(s)
        dp = [0]*n
        dp[0] = 1

        if s[1]!="0":
            if 10<=int(s[0:2])<=26:
                dp[1] = 2
            else:
                dp[1] = 1
        else:
            if 10<=int(s[0:2])<=26:
                dp[1]=1
            else:
                return 0
        


        for i in range(2,n):
            if s[i]!="0":
                if 10<=int(s[i-1:i+1])<=26:
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1] 
            else:
                if 10<=int(s[i-1:i+1])<=26:
                    dp[i]=dp[i-2]
                else:
                    return 0
        
        return dp[-1]



#more optimized solution cuz mines slow af
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         dp = {}

#         def dfs(i):
#             if i in dp:
#                 return dp[i]
            
#             if i >= len(s):
#                 return 1
            
#             if s[i] == "0":
#                 return 0
            
#             res = dfs(i + 1)

#             if i + 1 < len(s) and 10 <= int(s[i : i + 2]) <= 26:
#                 res += dfs(i + 2)
            
#             dp[i] = res
#             return res
        
#         return dfs(0)