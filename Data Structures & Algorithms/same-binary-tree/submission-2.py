# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def checkEq(a,b):
            if a==None and b==None:
                return True
            elif a==None or b==None:
                return False
            else:
                return (a.val==b.val and checkEq(a.left,b.left) and checkEq(a.right,b.right))
        
        return checkEq(p,q) 
        