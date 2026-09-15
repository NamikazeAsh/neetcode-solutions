# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        #recursive helper
        def sameTree(root,subroot):
            if not root and not subroot:
                return True
            if root and subroot and root.val == subroot.val:
                return(sameTree(root.right,subroot.right) and sameTree(root.left,subroot.left))
            return False

        if not subRoot:
            return True
        if not root:
            return False
        
        if sameTree(root,subRoot):
            return True
        return ( (self.isSubtree(root.right,subRoot)) or (self.isSubtree(root.left,subRoot)) )
        
        
        