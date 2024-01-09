from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
tree2 = TreeNode(1, TreeNode(2), TreeNode(3))

solution = Solution()
result = solution.isSameTree(tree1, tree2)
print("Are the two trees the same?", result)