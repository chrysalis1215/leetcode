from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            if nums[mid] == nums[left] == nums[right]:
                left += 1
                right -= 1

            elif nums[mid] >= nums[left]:
                if  nums[mid] > target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False

        
# leetcode submit region end(Prohibit modification and deletion)
Solution().search([3,1], 1)