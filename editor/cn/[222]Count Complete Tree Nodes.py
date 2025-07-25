# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        hl, hr = 0, 0
        noder, nodel = root, root
        while nodel:
            nodel = nodel.left
            hl += 1

        while noder:
            noder = noder.right
            hr += 1

        if hr == hl:
            return int(math.pow(2, hl) - 1)


        return  self.countNodes(root.left) + self.countNodes(root.right) + 1
        
# leetcode submit region end(Prohibit modification and deletion)
