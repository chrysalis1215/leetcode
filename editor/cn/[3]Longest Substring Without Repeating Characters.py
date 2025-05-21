# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        start = 0
        hashMap = {}
        for i, char in enumerate(s):
            if char in hashMap:
                # start 为递增数列，该限制条件可约束 start 越界重置
                start = max(start, hashMap[char] + 1)
            hashMap[char] = i
            ans = max(ans, i - start + 1)

        return ans
# leetcode submit region end(Prohibit modification and deletion)
