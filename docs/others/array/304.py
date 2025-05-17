class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        # self.sums = [[0] * (n + 1)] * m
        # Error !!! use the same reference 
        self.sums = [[0] * (n + 1) for _ in range(m + 1)]

        for row, arr in enumerate(matrix):
            for col, num in enumerate(arr):
                self.sums[row + 1][col + 1] = self.sums[row][col + 1]  + self.sums[row + 1][col] -  self.sums[row][col] + num
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        

        return self.sums[row2 + 1][col2 + 1] - self.sums[row1][col2 + 1 ] - self.sums[row2 + 1][col1] + self.sums[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)