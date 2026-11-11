# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == []:
            return 0
        
        depth=0

        def dfs(node):
            #preorder because increment THEN travel
            if not node:
                return 0
            #process
            return 1+max(dfs(node.left),dfs(node.right)) 

        return dfs(root)
        