from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])

        res = [[0 for _ in range(row)] for _ in range(col)]
        for i in range(row):
            for j in range(col):
                res[j][i] = matrix[i][j]

        return res
# leetcode submit region end(Prohibit modification and deletion)
