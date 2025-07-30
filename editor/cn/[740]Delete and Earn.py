# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        hash = defaultdict(int)
        for i in range(len(nums)):
            hash[nums[i]] += nums[i]

        keys = sorted(hash.keys())
        dp = [0] * len(keys)

        dp[0] = hash[keys[0]]
        if len(keys) > 1: dp[1] = max(hash[keys[0]], hash[keys[1]]) if keys[0] + 1 == keys[1] else hash[keys[0]] + hash[keys[1]]
        for i in range(2, len(keys)):
            if keys[i] - 1 == keys[i - 1]:
                dp[i] = max(dp[i - 2] + hash[keys[i]], dp[i - 1])
            else:
                dp[i] = dp[i - 1] + hash[keys[i]]

        return dp[-1]


        
# leetcode submit region end(Prohibit modification and deletion)
