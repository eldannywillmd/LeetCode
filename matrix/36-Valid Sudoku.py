from collections import Counter


class Solution:
    def isValidSudoku(self, board):
        count = Counter()

        # first: each row must contain a digit through 1-9 without repetition
        for row in board:
            for col in row:
                if col != '.':
                    count[col] += 1
                    if count[col] > 1:
                        return False
            count.clear()

        # second: same for column
        for j in range(9):
            for i in range(9):
                if board[i][j] != '.':
                    count[board[i][j]] += 1
                    if count[board[i][j]] > 1:
                        return False
            count.clear()

        # third: same thing for each of the nine 3x3 boxes -> board[0:3][0:3]
        ranges_row = [(0,3), (3,6), (6,9)]
        ranges_col = ranges_row
        for x in ranges_row:
            for y in ranges_col:
                for i in range(x[0],x[1]):
                    for j in range(y[0],y[1]):
                        if board[i][j] != '.':
                            count[board[i][j]] += 1
                            if count[board[i][j]] > 1:
                                return False
                count.clear()
        return True



board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
solution = Solution()
print(solution.isValidSudoku(board))