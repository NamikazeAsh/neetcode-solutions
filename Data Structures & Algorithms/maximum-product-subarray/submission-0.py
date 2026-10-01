#kadane method, obscure ahh shi
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        curmin = nums[0]
        curmax = nums[0]
        goat_val = nums[0]

        for i in range(1,len(nums)):
            cur = nums[i]
            tmp = curmax
            curmax = max(cur,cur*curmax,cur*curmin)
            curmin = min(cur,cur*curmin,cur*tmp)
            goat_val = max(goat_val,curmax)

        return goat_val