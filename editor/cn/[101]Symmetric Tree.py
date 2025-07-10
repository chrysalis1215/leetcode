# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            quene = []
            quene.append(p)
            quene.append(q)

            while quene:
                l = quene.pop(0)
                r = quene.pop(0)
                if not l and not r:
                    continue
                if not l or not r:
                    return False
                if l.val != r.val:
                    return False

                quene.append(l.left)
                quene.append(r.right)

                quene.append(l.right)
                quene.append(r.left)

            return True

        return check(root, root)

        
# leetcode submit region end(Prohibit modification and deletion)
