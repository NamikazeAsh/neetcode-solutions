class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = len(nums)-1
        l = 0
        print("start",l,r)
        while l!=r:
            if nums[l]>nums[r]:
                l+=1
                print(l,r)
            elif nums[r]>nums[l]:
                r-=1
                print(l,r)
        print(l,r)
        return nums[l]