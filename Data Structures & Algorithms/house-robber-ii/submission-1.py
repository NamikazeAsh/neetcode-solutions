class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)<=2:
                return max(nums)

        def helper(nums):
            dp = ([0]*len(nums))

            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])

            # print(dp)

            for i in range(2,len(nums)):
                dp[i] = max(dp[i-1],nums[i] + dp[i-2])

            return max(dp)
        
        nums1=nums[1:]
        nums2=nums[:-1]
        dpm1 = helper(nums1)
        dpm2 = helper(nums2)
        return max(dpm1,dpm2)