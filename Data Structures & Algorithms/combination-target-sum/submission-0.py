class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        start = 0

        def backtrack(start,temp):
            if sum(temp) == target:
                res.append(temp.copy())
                return
            

            for i in range(start,len(nums)):
                num = nums[i]
                if sum(temp) + num > target:
                    continue

                temp.append(num)
                backtrack(i,temp)
                temp.pop()
                
        backtrack(start,temp)
        return res


# def backtrack(params):
# 	if base_case_condition:
# 		results.append(copy_of_solution)
# 		return
	
# 	for choice in choices:
# 		if violates_constraints:
# 			continue
	
# 		make_choice
# 		backtrack(updated_parameters)
# 		undo_choice
