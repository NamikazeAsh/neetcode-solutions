class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # print((sorted(set(nums))))

        #starting if and only if its start of a seq
        # AKA consider only those nums
        if not nums:
            return 0
        nums = sorted(set(nums))
        if len(nums)==1:
            return 1

        c=0
        lc = []
        for i in range(len(nums)-1):
            if i==0 or (nums[i-1] != nums[i]-1):
                start = nums[i]
                c=1
                lc.append(c)
            print(nums[i])

            if nums[i]+1==nums[i+1]:
                #increasing sequence
                c+=1
                lc.append(c)
                
        return max(lc)
            
            
               
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
        # nums = sorted(set(nums))
        # start = 0
        # count = 1
        # cl = []

        # if nums==[]:
        #     return 0

        # if len(nums)==0 or len(nums)==1:
        #     return 1

        # if len(nums)>=2:
        #     for i in range(len(nums)-1):
        #         if nums[i+1] == nums[i]+1:
        #             # print("yes:",nums[i],nums[i+1])
        #             count+=1
        #             cl.append(count)
        #         else:
        #             count=1
        #             cl.append(count)
        # return max(cl)