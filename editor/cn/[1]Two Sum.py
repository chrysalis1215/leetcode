from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        restDic = {}
        for i, num in enumerate(nums):
            rest = target - num
            if rest in restDic:
                return [restDic[rest], i]
            restDic[num] = i

        return []

# leetcode submit region end(Prohibit modification and deletion)
