class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            d[n] = d.get(n,0) + 1
        for k  in d:
            val = d.get(k)
            if val>1:
                return True
        return False