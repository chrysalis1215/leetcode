# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return True

        slow = fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        if fast: slow = slow.next

        pre = None

        while slow:
            temp = slow.next
            slow.next = pre

            pre = slow
            slow = temp

        while pre:

            if pre.val == head.val:
                pre = pre.next
                head = head.next
            else:
                return False


        return True

        
# leetcode submit region end(Prohibit modification and deletion)
