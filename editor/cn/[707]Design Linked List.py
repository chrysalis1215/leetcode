# leetcode submit region begin(Prohibit modification and deletion)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode(0, None)
        self.size = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        node = self.dummy

        for i in range(index + 1):
            node = node.next

        return node.val
        

    def addAtHead(self, val: int) -> None:
        self.dummy.next = ListNode(val, self.dummy.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        cur = self.dummy

        while cur.next:
            cur = cur.next

        cur.next = ListNode(val, None)
        self.size += 1


        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        cur = self.dummy

        for i in range(index):
            cur = cur.next

        cur.next = ListNode(val, cur.next)
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return

        cur = self.dummy

        for i in range(index):
            cur = cur.next

        cur.next = cur.next.next if cur.next else None

        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# leetcode submit region end(Prohibit modification and deletion)
