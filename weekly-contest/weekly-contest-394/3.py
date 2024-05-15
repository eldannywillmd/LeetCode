from collections import Counter


class Solution:
    def minimumOperations(self, grid):
        height = len(grid)
        width = len(grid[0])
        count = 0

        # Flatten the grid
        flat_list = [item for sublist in grid for item in sublist]
        # Count each number
        count_num = Counter(flat_list)

        for i in range(height):
            for j in range(width):
                if j + 1 == width:
                    pass
                else:
                    if grid[i][j] == grid[i][j + 1]:
                        if grid[i][j] == 0:
                            grid[i][j + 1] = 1
                        else:
                            if i + 1 == height:
                                grid[i][j + 1] = grid[i][j] - 1
                            else:
                                grid[i][j + 1] = grid[i + 1][j + 1]
                        count += 1
                if i + 1 == height:
                    pass
                else:
                    if grid[i][j] != grid[i + 1][j]:
                        if count_num[grid[i][j]] >= count_num[grid[i + 1][j]]:
                            grid[i][j] = grid[i + 1][j]
                        else:
                            grid[i + 1][j] = grid[i][j]
                        count += 1

        return count

grid = [[2],[8],[6],[7],[8],[2],[0],[9],[0],[8]]
solution = Solution()