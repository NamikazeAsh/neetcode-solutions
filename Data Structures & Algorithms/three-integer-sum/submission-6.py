class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        # print(nums)

        res = []

        for i in range(len(nums)-2):
            target = -nums[i]
            j = i+1
            k = len(nums)-1
            
            while j<k:
                if target == (nums[j]+nums[k]):
                    x = sorted([nums[i],nums[j],nums[k]])
                    if x not in res:
                        res.append(x)
                    j+=1
                    k-=1
                #target bigger
                elif target > (nums[j]+nums[k]):
                    j+=1
                #target smalla
                elif target < (nums[j]+nums[k]):
                    k-=1
        return res