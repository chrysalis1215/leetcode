# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        if not root:
            return self.res

        def dfs(root, target, path):

            path.append(root.val)

            if not root.left and not root.right:
                if target == root.val:
                    self.res.append(path[:])
                path.pop()
                return

            if root.left:
                dfs(root.left, target - root.val, path)

            if root.right:
                dfs(root.right, target - root.val, path)

            path.pop()


        dfs(root, targetSum, [])

        return self.res

        
# leetcode submit region end(Prohibit modification and deletion)
