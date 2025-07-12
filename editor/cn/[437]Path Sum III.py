# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        self.res = 0

        def dfs(root, target) :
            if not root:
                return

            if root.val == target:
                self.res += 1

            dfs(root.left, )




        
# leetcode submit region end(Prohibit modification and deletion)
