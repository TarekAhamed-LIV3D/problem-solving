from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def preorder(node):
            if node:
                result.append(node.val)
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        return result

binary_tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))

solution = Solution()
result = solution.preorderTraversal(binary_tree)

print("Preorder traversal:", result)