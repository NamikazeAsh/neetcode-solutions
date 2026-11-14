# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #inorder then verify?
        order = []

        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            #process
            order.append(node.val)
            dfs(node.right)
        
        dfs(root)   
        for i in range(1,len(order)):
            if order[i]>order[i-1]:
                continue
            else:
                return False
        return True