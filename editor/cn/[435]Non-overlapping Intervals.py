# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])

        last = float('-inf')
        res = 0
        for start, end in intervals:
            if start >= last:
                last = end
            else:
                res += 1
        return res






# leetcode submit region end(Prohibit modification and deletion)
