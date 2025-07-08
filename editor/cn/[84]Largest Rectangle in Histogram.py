# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        res = 0
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                res = max(res, width * height)
            stack.append(i)
        return res
        
# leetcode submit region end(Prohibit modification and deletion)
