# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        size = len(height)
        res = 0
        left, right = 0, size -1
        while left < right:
            width = right - left

            res = max(res, width * min(height[right], height[left]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1


        return res
        
# leetcode submit region end(Prohibit modification and deletion)
