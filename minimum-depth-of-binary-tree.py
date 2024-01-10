from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            if not node.left and not node.right:
                # Found a leaf node, return its depth
                return depth

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

binary_tree = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))

solution = Solution()
result = solution.minDepth(binary_tree)

print("Minimum depth of the binary tree:", result)
