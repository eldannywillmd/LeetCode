from collections import Counter


class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        # directions left, right, down, up and all diagonals
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        count = Counter()
        width = len(board)
        height = len(board[0])

        for i in range(width):
            for j in range(height):
                for d in dir:
                    if 0 <= i + d[0] < width and 0 <= j + d[1] < height and board[i + d[0]][j + d[1]] == 1:
                        count[(i,j)] += 1

        for i in range(width):
            for j in range(height):
                # with fewer than two live neighbors dies as if caused by under-population.
                # if cell has < 2 neighbours -> cell==0
                if count[(i,j)] < 2:
                    board[i][j] = 0
                # with two or three live neighbors lives on to the next generation.
                # if cell == 1 AND has >= 2 or <= 3 alive neighbors -> cell==1
                elif (count[(i,j)] == 2 or count[(i,j)] == 3) and board[i][j] == 1:
                    pass
                # with more than three live neighbors dies, as if by over-population.
                # if cell has > 3 alive neighbours -> cell==0
                elif count[(i,j)] > 3:
                    board[i][j] = 0
                # with exactly three live neighbors becomes a live cell, as if by reproduction.
                # if cell == 0 AND cell has == 3 alive neighbours -> cell==1
                elif count[(i,j)] == 3 and board[i][j] == 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

solution = Solution()
board = solution.gameOfLife(board)