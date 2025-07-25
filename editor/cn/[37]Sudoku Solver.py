# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        GRID = 9
        col_map = {i: set() for i in range(GRID)}
        row_map = {i: set() for i in range(GRID)}
        box_map = {i: set() for i in range(GRID)}
        blank = []

        for row in range(GRID):
            for col in range(GRID):
                if board[row][col] != '.':
                    b = (row // 3) * 3 + (col // 3)
                    col_map[col].add(board[row][col])
                    row_map[row].add(board[row][col])
                    box_map[b].add(board[row][col])
                else:
                    blank.append([row, col])

        def backtrack(start):
            if start == len(blank):
                return True

            row, col = blank[start]
            box_index = (row // 3) * 3 + (col // 3)

            for ch in map(str, range(1, 10)):
                if ch in row_map[row] or ch in col_map[col] or ch in box_map[box_index]:
                    continue
                board[row][col] = ch
                col_map[col].add(board[row][col])
                row_map[row].add(board[row][col])
                box_map[box_index].add(board[row][col])
                if backtrack(start + 1):
                    return True
                col_map[col].remove(board[row][col])
                row_map[row].remove(board[row][col])
                box_map[box_index].remove(board[row][col])
                board[row][col] = '.'
            return False

        backtrack(0)





# leetcode submit region end(Prohibit modification and deletion)
