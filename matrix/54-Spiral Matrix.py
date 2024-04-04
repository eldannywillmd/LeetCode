class Solution:
    def spiralOrder(self, matrix):
        spiral = []
        visited = set()
        h1, h2 = 0, len(matrix) - 1 # rows
        w1, w2 = 0, len(matrix[0]) - 1 # columns
        m, n = 0, 0

        spiral.append(matrix[m][n])
        visited.add((m, n))
        while w1 <= w2 and h1 <= h2:
            # right
            while n < w2:
                n += 1
                if (m,n) in visited:
                    return spiral
                spiral.append(matrix[m][n])
                visited.add((m,n))
            h1 += 1
            # down
            while m < h2:
                m += 1
                if (m,n) in visited:
                    return spiral
                spiral.append(matrix[m][n])
                visited.add((m, n))
            w2 -= 1
            # left
            while n > w1:
                n -= 1
                if (m,n) in visited:
                    return spiral
                spiral.append(matrix[m][n])
                visited.add((m, n))
            h2 -= 1
            # up
            while m > h1:
                m -= 1
                if (m,n) in visited:
                    return spiral
                spiral.append(matrix[m][n])
                visited.add((m, n))
            # update borders
            w1 += 1

        return spiral

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]
solution = Solution()
print(solution.spiralOrder(matrix))