class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo={}
        def helper(s):
            #basecase
            if s=="":
                return True
            if s in memo:
                return memo[s]
            for w in wordDict:
                if s.startswith(w):
                    if helper(s[len(w):]):
                        memo[s]=True
                        return True
            
            memo[s] = False
            return False
        
        return helper(s)






# correct but inefficient, leetcode sucks ahh shit.
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
#         if s=="":
#             return True

#         for w in wordDict:
#             if s.startswith(w):
#                 if self.wordBreak(s[len(w):],wordDict):
#                     return True
#         return False
