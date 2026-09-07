class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output=[]
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1

            target = nums[i]
            while j<k:
                if target==-(nums[j]+nums[k]):
                    opx = [target,nums[j],nums[k]]
                    if opx not in output:
                        output.append(opx)
                    j+=1
                    # print("o",output)
                elif target>-(nums[j]+nums[k]):
                    k-=1
                    # print("k-")
                elif target<-(nums[j]+nums[k]):
                    j+=1
                    # print("j+")
        return output