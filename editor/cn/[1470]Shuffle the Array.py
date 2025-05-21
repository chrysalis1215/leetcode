from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i, _ in enumerate(nums):
            j = 2 * i if i < n else 2 * (i - n) + 1
            # 将 num[i] 的原始数值 储存在目标 num[j] 的高 10 位
            nums[j] |= (nums[i] & 1023) << 10

        for i, _ in enumerate(nums):
            nums[i] >>= 10

        return nums

# leetcode submit region end(Prohibit modification and deletion)
