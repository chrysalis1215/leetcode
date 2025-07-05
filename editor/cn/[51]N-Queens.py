# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        chess_board = [['.' for _ in range(n)] for _ in range(n)]
        col_set = set()
        dig1_set = set()
        dig2_set = set()
        def backtrack(row, board):
            if row == n:
                res.append([''.join(r) for r in board])
                return

            for col in range(n):
                if col not in col_set and (row - col) not in dig1_set and (row + col) not in dig2_set:
                    col_set.add(col)
                    dig1_set.add(row - col)
                    dig2_set.add(row + col)

                    board[row][col] = 'Q'
                    backtrack(row + 1, board)
                    # remove col
                    board[row][col] = '.'
                    col_set.remove(col)
                    dig1_set.remove(row - col)
                    dig2_set.remove(row + col)
                else:
                    continue



        backtrack(0, chess_board)

        return res
        
# leetcode submit region end(Prohibit modification and deletion)
