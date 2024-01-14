from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path):
            if not node:
                return []

            path.append(str(node.val))

            if not node.left and not node.right:
                return ['->'.join(path)]

            left_paths = dfs(node.left, path.copy())
            right_paths = dfs(node.right, path.copy())

            return left_paths + right_paths

        if not root:
            return []

        return dfs(root, [])

binary_tree = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))

solution = Solution()
result = solution.binaryTreePaths(binary_tree)

print("Root-to-leaf paths:", result)