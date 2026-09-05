class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #init dict
        d={}

        for n in nums:
            if n not in d:
                
                d[n]=0
            d[n]+=1
        sol = []
        while k!=0:
            c=0
            v=0
            for key in d:
                if d[key]>c:
                    c = d[key]
                    v = key
            sol.append(v)
            del d[v]
            k-=1
            
        return sol
        