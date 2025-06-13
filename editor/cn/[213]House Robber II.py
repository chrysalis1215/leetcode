# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]

        def find_rob_linear(nums: List[int]) -> int:
            n = len(nums)
            if n == 0:
                return 0
            elif n == 1:
                return nums[0]


            pre2 = nums[0]

            pre1 = max(pre2, nums[1])

            cur = pre1

            for i in range(2, n):
                cur = max(pre1, nums[i] + pre2 )
                pre2 = pre1
                pre1 = cur

            return cur

        return max(find_rob_linear(nums[:-1]), find_rob_linear(nums[1:]))




# leetcode submit region end(Prohibit modification and deletion)
