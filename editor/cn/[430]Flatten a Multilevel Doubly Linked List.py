# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        list = []
        node = head

        while node:
            if node.child:
                if node.next:
                    list.append(node.next)

                node.next = node.child
                node.child.prev = node
                node.child = None


            if not node.next and list:
                child_node = list.pop(-1)
                node.next = child_node
                child_node.prev = node
            node = node.next

        return head

# leetcode submit region end(Prohibit modification and deletion)
