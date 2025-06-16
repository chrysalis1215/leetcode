# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        left_head = dummy

        # 寻找 left 的前一个元素，作为反转子链的左边 head 连接点
        for i in range(left - 1):
            left_head = left_head.next

        right_head = left_head.next
        cur = right_head
        pre = None

        # 反转 left - right 的链表
        # 反转结束后，pre 为反转后链表的头部， cur 为遗留链表的头部
        for i in range(left, right + 1):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        left_head.next = pre
        right_head.next = cur

        return dummy.next



        
# leetcode submit region end(Prohibit modification and deletion)
