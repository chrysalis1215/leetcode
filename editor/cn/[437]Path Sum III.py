from collections import defaultdict
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(root: Optional[TreeNode], count):

            if not root:
                return 0

            count += root.val

            res = prefix[count - targetSum]

            prefix[count] += 1

            res += dfs(root.left, count)
            res += dfs(root.right, count)

            prefix[count] -= 1

            return res

        return dfs(root, 0)





        
# leetcode submit region end(Prohibit modification and deletion)
