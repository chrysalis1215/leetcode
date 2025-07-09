from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        res = 0
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols

        def findMaxArea(heights: List[int])  -> int:
            area = 0
            heights.append(0)
            stack = []
            for i in range(len(heights)):

                while stack and heights[i] < heights[stack[-1]]:
                    index = stack.pop()
                    width = i if not stack else i - (stack[-1] + 1)
                    area = max(area, heights[index] * width)
                stack.append(i)
            heights.pop()
            return area

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            res = max(findMaxArea(heights), res)

        return res

# leetcode submit region end(Prohibit modification and deletion)
