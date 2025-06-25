# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        return self.resverse(None, head)


    def resverse(self, pre:[ListNode], cur:Optional[ListNode]):
        temp = cur.next
        cur.next = pre
        if not temp:
            return cur

        return  self.resverse(cur, temp)


        
# leetcode submit region end(Prohibit modification and deletion)