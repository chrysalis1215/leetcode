# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        res = 0
        max_flag = float('-inf')
        for start, end in points:
            if start > max_flag:
                max_flag = end
                res += 1
        return  res
# leetcode submit region end(Prohibit modification and deletion)
