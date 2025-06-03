from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        # 遍历数组会造成空间浪费（数组中可能存在重复的元素）
        for num in s:
            seq = 1
            if num - 1 in s:
                continue
            else:
                while num + seq in s:
                    seq += 1

            res = max(res, seq)
        return res
# leetcode submit region end(Prohibit modification and deletion)

Solution().longestConsecutive([100,4,200,1,3,2])