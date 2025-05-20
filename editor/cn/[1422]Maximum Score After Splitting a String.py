# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxScore(self, s: str) -> int:
        left = 1 if s[0] == '0' else 0
        ans = score = left + s[1:].count('1')

        for i in s[1:-1]:
            score = score + 1 if i == '0' else score - 1
            ans = max(ans, score)


        return ans

# leetcode submit region end(Prohibit modification and deletion)

Solution().maxScore("011101")