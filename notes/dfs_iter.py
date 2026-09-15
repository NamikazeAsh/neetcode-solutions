class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root



# --- DFS iterative ----
def dfs_iterative(root):

    if root is None:
        return []

    stack = [root]
    order = []

    while stack:

        node = stack.pop()
        order.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return order

values = [8, 3, 10, 1, 6, 9, 14, None, None, 4, 7, None, None, None, 13]
root = build_tree(values)
print(dfs_iterative(root))