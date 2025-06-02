# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                mid_l = mid_r = mid
                while mid_l > 0 and nums[mid_l - 1] == target: mid_l -= 1
                while mid_r < len(nums) - 1 and nums[mid_r + 1] == target: mid_r += 1

                return [mid_l, mid_r]

            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1

        return [-1, -1]

        
# leetcode submit region end(Prohibit modification and deletion)
