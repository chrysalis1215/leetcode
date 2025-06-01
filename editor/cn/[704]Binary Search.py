# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] ==  target:
                return mid
            else:
                left = mid + 1

        return -1
        
# leetcode submit region end(Prohibit modification and deletion)
