# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        queue = [root]
        order = []
        
        while queue:
            # print([q.val for q in queue])

            q_size = len(queue)
            q_vals = []

            for _ in range(q_size):      
                node = queue.pop(0)
                q_vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            order.append(q_vals)


        return order