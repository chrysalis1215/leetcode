# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []

        def tarverse(quene):
            if not quene:
                return
            size = len(quene)
            levels = []
            while size > 0:
                size -= 1
                node = quene.pop(0)
                levels.append(node.val)
                if node.left:
                    quene.append(node.left)
                if node.right:
                    quene.append(node.right)
            res.append(levels)

            tarverse(quene)

        tarverse([root])
        return res

# leetcode submit region end(Prohibit modification and deletion)
