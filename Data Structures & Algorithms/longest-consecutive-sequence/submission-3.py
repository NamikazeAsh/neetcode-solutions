class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # print((sorted(set(nums))))
        nums = sorted(set(nums))
        start = 0
        count = 1
        cl = []

        if nums==[]:
            return 0

        if len(nums)==0 or len(nums)==1:
            return 1

        if len(nums)>=2:
            for i in range(len(nums)-1):
                if nums[i+1] == nums[i]+1:
                    # print("yes:",nums[i],nums[i+1])
                    count+=1
                    cl.append(count)
                else:
                    count=1
                    cl.append(count)
        return max(cl)