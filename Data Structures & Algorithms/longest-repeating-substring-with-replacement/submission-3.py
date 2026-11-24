class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #dict for keeping mapping of every char freq in window?
        #replacement needed = window length - most frequent ----> so should be <=k
        #decrease window when win_len-most_freq > k
        
        d = {}
        res = 0
        l = 0

        for i in range(len(s)):
            #init dic
            d[s[i]] = d.get(s[i], 0) + 1
        
            #window len - most freq check
            window_len = (i-l)+1
            # print(s[l:i+1], d)
            if window_len - max(d.values()) <= k: 
                res = max(res,window_len)
            else:
                d[s[l]] = d.get(s[l])-1
                l+=1
                
        return (res)





























        # l = 0
        # count = {}
        # result = 0
        
        # for r in range(len(s)):
        #     count[s[r]] = 1 + count.get(s[r],0) #initializing shortcut

        #     while ((r-l)+1) - max(count.values()) > k:
        #         count[s[l]] -= 1
        #         l +=1
        #     result = max(result, (r-l)+1)
        # return result

