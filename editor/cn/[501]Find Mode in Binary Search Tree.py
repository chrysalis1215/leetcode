# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        count = 0
        max_count = 0
        pre = None

        def dfs(node: Optional[TreeNode]):
            if not node:
                return

            dfs(node.left)
            nonlocal count, pre, max_count, res

            if pre is None or pre == node.val:
                count += 1
            else:
                count = 1

            if count > max_count:
                res = [node.val]
                max_count = count
            elif count == max_count:
                res.append(node.val)

            pre = node.val

            dfs(node.right)

        dfs(root)
        return res
        
# leetcode submit region end(Prohibit modification and deletion)
