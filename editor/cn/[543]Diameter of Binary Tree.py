# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.res = 0

        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left = dfs(root.left)

            right = dfs(root.right)

            self.res = max(left + right, self.res)

            return max(right, left) + 1
        dfs(root)
        return self.res
        
# leetcode submit region end(Prohibit modification and deletion)
