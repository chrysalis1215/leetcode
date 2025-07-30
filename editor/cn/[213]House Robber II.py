# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        def findMax(nums: List[int]) -> int:
            size = len(nums)

            pre2, pre1 = nums[0], nums[0]

            if size > 1: pre1 = max(pre2, nums[1])

            cur = pre1

            for i in range(2, size):
                cur = max(pre1, pre2 + nums[i])
                pre2 = pre1
                pre1 = cur

            return cur
        return max(findMax(nums[1:]), findMax(nums[:-1]))



# leetcode submit region end(Prohibit modification and deletion)
