# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        pq = []
        uid = 0  # Unique ID counter
        dummy = ListNode(0, None)
        cur = dummy
        for i in range(k):
            node = lists[i]
            if node:
                uid += 1
                heapq.heappush(pq,(node.val, uid, node))

        while pq:

            _, _, node = heapq.heappop(pq)
            cur.next = node
            cur = cur.next
            if node.next:
                uid += 1
                heapq.heappush(pq, (node.next.val, uid, node.next))

        return dummy.next




        
# leetcode submit region end(Prohibit modification and deletion)
