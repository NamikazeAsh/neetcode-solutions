class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #diff method
        l = []
        for n in range(len(nums)):
            diff = target - nums[n]
            if diff in nums:
                l=[n,nums.index(diff)]
                
        
        return sorted(l)