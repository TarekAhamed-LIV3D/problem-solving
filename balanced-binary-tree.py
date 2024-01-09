from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            return max(left_height, right_height) + 1

        def isBalancedHelper(node):
            if not node:
                return True

            left_height = height(node.left)
            right_height = height(node.right)

            if abs(left_height - right_height) > 1:
                return False

            return isBalancedHelper(node.left) and isBalancedHelper(node.right)

        return isBalancedHelper(root)

balanced_tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
unbalanced_tree = TreeNode(1, TreeNode(2, right=TreeNode(4)), TreeNode(3))

solution = Solution()
result_balanced = solution.isBalanced(balanced_tree)
result_unbalanced = solution.isBalanced(unbalanced_tree)

print("Is the balanced tree height-balanced?", result_balanced)
print("Is the unbalanced tree height-balanced?", result_unbalanced)
