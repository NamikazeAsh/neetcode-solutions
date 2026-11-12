# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        #one's higher than root, other's lower than root hence root is the lca
        if q.val>=root.val>=p.val or p.val>=root.val>=q.val:
            return root
        
        #right subtree
        elif q.val>p.val>root.val or p.val>q.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        #left subtree
        elif root.val>p.val>q.val or root.val>q.val>p.val:
            return self.lowestCommonAncestor(root.left,p,q)
