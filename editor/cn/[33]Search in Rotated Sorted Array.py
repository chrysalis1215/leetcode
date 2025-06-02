# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # 确定left -> mid是升序的
            if nums[mid] > nums[left]:
                if nums[mid] > target >= nums[left]:
                    right = mid
                else:
                    left = mid + 1
            # 确定mid -> right 是升序列的
            else:
                if nums[mid] < target <= nums[right - 1]:
                    left = mid + 1
                else:
                    right = mid

        return -1
        
# leetcode submit region end(Prohibit modification and deletion)
