# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -1001

        def dsf(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left = max(0, dsf(root.left))
            right = max(0, dsf(root.right))


            self.res = max(self.res, left + right + root.val)

            return root.val + max(left, right)

        dsf(root)

        return self.res



# leetcode submit region end(Prohibit modification and deletion)
