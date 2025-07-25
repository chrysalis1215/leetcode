# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.res = float('inf')
        self.pre = None
        def dfs(node: Optional[TreeNode]):
            if not node:
                return

            dfs(node.left)
            if self.pre is not None:
                self.res = min(self.res, abs(node.val - self.pre))
            self.pre = node.val
            dfs(node.right)


        dfs(root)
        return self.res

        
# leetcode submit region end(Prohibit modification and deletion)
