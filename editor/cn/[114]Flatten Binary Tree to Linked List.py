# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        node = root

        while node:
            if node.left:
                predecessor = node.left
                while predecessor.right:
                    predecessor = predecessor.right

                predecessor.right = node.right
                node.right = node.left
                node.left = None

            node = node.right
















# leetcode submit region end(Prohibit modification and deletion)
