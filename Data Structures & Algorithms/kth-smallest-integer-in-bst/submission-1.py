# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #dfs inorder = returns stuff in ascending order

        order = []
        def dfs(node):
            if node.left:
                dfs(node.left)
            #process
            order.append(node.val)
            if node.right:
                dfs(node.right)
        
        dfs(root)
        return(order[k-1])
