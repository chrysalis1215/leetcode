# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(root, height) -> TreeNode:
            if not root:
                return

            if root.left:
                dfs(root.left, height + 1)
            if root.right:
                dfs(root.right, height + 1)

            if not root.left and not root.right:
                return height
# leetcode submit region end(Prohibit modification and deletion)
