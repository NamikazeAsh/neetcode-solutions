class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d.get(n,0)+1
        # print(d)
        res = set()
        
        while k!=0:
            tmp = 0
            tmp_k = 0
            for i in d:
                if d[i]>tmp and (i not in res):
                    tmp = d[i]
                    tmp_k = i
            res.add(tmp_k)
            k-=1
        return (list(res))