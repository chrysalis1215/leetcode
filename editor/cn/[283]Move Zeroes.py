# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)  == 1:
            return

        zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            else:
                nums[i - zero] = nums[i]

        for i in range(zero):
            nums[-(i + 1)] = 0

        
# leetcode submit region end(Prohibit modification and deletion)
