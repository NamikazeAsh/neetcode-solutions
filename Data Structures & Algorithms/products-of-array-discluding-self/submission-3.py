class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        output = []
        rez = 1
        for num in nums:
            rez*=num 
            prefix.append(rez) 

        rez = 1
        for i in range(len(nums)-1,-1,-1):
            rez*=nums[i]
            postfix.append(rez)
        postfix = postfix[::-1]

        for j in range(len(nums)):
            #prefix-1 x postfix+1
            if j==0:
                output.append(1*postfix[j+1])
            elif j==len(nums)-1:
                output.append(prefix[j-1]*1)
            else:
                output.append(prefix[j-1]*postfix[j+1])
        return output