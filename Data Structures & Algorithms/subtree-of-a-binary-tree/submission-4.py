# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check(root,subroot):
            if not root and not subroot: #both empty
                return True
            elif root and not subroot: 
                return False
            elif not root and subroot:
                return False

            if root.val == subroot.val:
                return check(root.left,subroot.left) and check(root.right,subroot.right)
            else:
                return False

        def dfs(root,subroot):
            if not root:
                return False

            if root and subroot:
                if root.val == subroot.val: #either in parent's node, child left node or child right node
                    return check(root,subroot) or dfs(root.left,subroot) or dfs(root.right,subroot)
                else:
                    return dfs(root.left,subroot) or dfs(root.right,subroot)

        return dfs(root,subRoot)