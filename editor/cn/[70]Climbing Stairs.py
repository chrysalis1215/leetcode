# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * n

        dp[0] = 1
        if n > 1: dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n-1]
# leetcode submit region end(Prohibit modification and deletion)
