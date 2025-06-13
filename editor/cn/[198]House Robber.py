# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        pre2 = nums[0]
        pre1= max(nums[0], nums[1])
        cur = pre1
        for i in range(2, len(nums)):
            cur= max(pre1, pre2 + nums[i])
            pre2 = pre1
            pre1 = cur

        return cur


        
# leetcode submit region end(Prohibit modification and deletion)
