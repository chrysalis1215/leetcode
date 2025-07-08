# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                top_index = stack.pop()
                res[top_index] = i - top_index
            stack.append(i)

        return res

Solution().dailyTemperatures([73,74,75,71,69,72,76,73])
        
# leetcode submit region end(Prohibit modification and deletion)
