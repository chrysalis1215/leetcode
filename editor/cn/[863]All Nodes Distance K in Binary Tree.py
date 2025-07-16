# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}
        res = []

        def dfs(node: TreeNode, parent):
            if not node:
                return
            parents[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        visited = set()
        queue = []

        queue.append((target, 0))

        while queue:
            node, dist = queue.pop(0)
            if not node or node in visited:
                continue

            visited.add(node)

            if dist == k:
                res.append(node.val)
            elif  dist < k:
                queue.append((node.left, dist + 1))
                queue.append((node.right, dist + 1))
                queue.append((parents[node], dist + 1))

        return res



# leetcode submit region end(Prohibit modification and deletion)
