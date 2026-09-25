class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        def helper(row,col,wi):
            if wi==len(word):
                return True
            if (row<0 or col<0 or row>=len(board) or col>=len(board[0]) or board[row][col]!=word[wi] or (row,col) in path):
                return False
            
            path.add((row,col))
            result = (helper(row+1,col,wi+1) or helper(row,col+1,wi+1) or helper(row,col-1,wi+1) or helper(row-1,col,wi+1))
            path.remove((row,col))
            return result
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if helper(i,j,0):
                    return True
        return False

            


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