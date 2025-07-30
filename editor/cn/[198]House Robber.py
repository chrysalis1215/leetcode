# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [0] * size

        dp[0] = nums[0]
        if size > 1: dp[1] = max(nums[1], nums[0])

        for i in range(2, size):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[size - 1]

        
# leetcode submit region end(Prohibit modification and deletion)
