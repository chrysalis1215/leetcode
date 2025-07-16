# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = root

        def dfs(root: 'TreeNode'):
            if not root or root == p or root == q:
                return root

            left = dfs(root.left)
            right = dfs(root.right)

            if left and right:
                return root

            return left or right

        res = dfs(root)

        return res



# leetcode submit region end(Prohibit modification and deletion)
