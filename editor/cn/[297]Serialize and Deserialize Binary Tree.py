from idlelib.tree import TreeNode
from typing import Optional

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = []
        res = []

        if not root:
            return ''

        queue.append(root)

        while queue:
            size = len(queue)

            while size > 0:
                size -= 1
                node = queue.pop(0)
                if not node:
                    res.append('#')
                else:
                    res.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

        return ','.join(str(x) for x in res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        size = len(data)

        if size == 0:
            return
        list = data.split(',')
        root = TreeNode(list[0])
        queue = [root]

        i = 1

        while queue and i < size:
            node = queue.pop(0)
            if list[i] == '#':
                node.left = None
            else:
                node.left = TreeNode(list[i])
                queue.append(node.left)

            if i + 1 == size:
                break
            elif list[i + 1] == '#':
                node.right = None
            else:
                node.right = TreeNode(list[i + 1])
                queue.append(node.right)

            i += 2

        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)
