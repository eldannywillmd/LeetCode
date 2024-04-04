class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = []
        height = len(matrix)
        width = len(matrix[0])
        # the last row is the first column and so on
        for j in range(width):
            for i in reversed(range(height)):
                # first row
                row.append(matrix[i][j])
            matrix.append(row)
            row = []
        for i in range(height):
            matrix.pop(0)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
solution = Solution()
solution.rotate(matrix)