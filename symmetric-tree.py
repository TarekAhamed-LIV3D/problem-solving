from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isMirror(left, right):
            if not left and not right:
                return True

            if not left or not right:
                return False

            return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)

        return isMirror(root.left, root.right)

symmetric_tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
non_symmetric_tree = TreeNode(1, TreeNode(2, right=TreeNode(3)), TreeNode(2, right=TreeNode(3)))

solution = Solution()
result_symmetric = solution.isSymmetric(symmetric_tree)
result_non_symmetric = solution.isSymmetric(non_symmetric_tree)

print("Is the symmetric tree symmetric?", result_symmetric)
print("Is the non-symmetric tree symmetric?", result_non_symmetric)
