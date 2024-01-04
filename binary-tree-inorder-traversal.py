class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    result = []
    stack = []

    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        current = stack.pop()
        result.append(current.val)

        root = current.right

    return result

tree = TreeNode(1, TreeNode(2), TreeNode(3))

result = inorderTraversal(tree)
print("Inorder traversal:", result)