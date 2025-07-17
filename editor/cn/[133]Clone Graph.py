# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return []

        queue = [node]

        while queue:
            cur = queue.pop(0)
            self.node = cur.val





        
# leetcode submit region end(Prohibit modification and deletion)
