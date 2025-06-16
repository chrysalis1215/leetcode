# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        for i in range(n):
            fast = fast.next

        slow = dummy

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next if slow.next else None

        return dummy.next
        
# leetcode submit region end(Prohibit modification and deletion)
