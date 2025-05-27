from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[right] + numbers[left]
            if sum == target:
                return [left + 1, right + 1]
            elif sum > target:
                right -= 1
            else:
                left += 1
        return []

# leetcode submit region end(Prohibit modification and deletion)

Solution().twoSum([2,7,11,15], 9)
