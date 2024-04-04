class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        height = len(matrix)
        width = len(matrix[0])
        coord_i = set()
        coord_j = set()

        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    coord_i.add(i)
                    coord_j.add(j)
        for i in range(height):
            for j in range(width):
                if i in coord_i or j in coord_j:
                    matrix[i][j] = 0

        print(matrix)


matrix = [[1,1,1],[1,0,1],[1,1,1]]
solution = Solution()
solution.setZeroes(matrix)