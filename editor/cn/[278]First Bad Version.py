# leetcode submit region begin(Prohibit modification and deletion)
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    # def __init__(self, bad: int):
    #     self.bad = bad

    # def isBadVersion(self, n: int):
    #     if n >= self.bad:
    #         return  True
    #     return False

    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        while start < end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
        return end

        
# leetcode submit region end(Prohibit modification and deletion)

Solution(1).firstBadVersion(1)
