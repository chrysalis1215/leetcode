# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.predecessor = float('-inf')

        def dfs(root):
            if not root:
                return True

            if root.left and not dfs(root.left):
                return False

            if root.val > self.predecessor:
                self.predecessor = root.val
            else:
                return False

            if root.right and not dfs(root.right):
                return False

            return True


        return dfs(root)
        
# leetcode submit region end(Prohibit modification and deletion)
