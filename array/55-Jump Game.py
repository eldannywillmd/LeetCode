class Solution:
    def canJump(self, nums):
        jumps = [0]
        is_visited = set()

        #dfs (faster than bfs) fifo
        while jumps:
            jump = jumps.pop(-1)
            if jump < len(nums) and nums[jump] != 0:
                for i in range(1, nums[jump] + 1):
                    if jump + i not in is_visited:
                        is_visited.add(jump + i)
                        jumps.append(jump + i)
                if jump == len(nums) - 1:
                    return True
            if jump == len(nums) - 1:
                return True
        return False

solution = Solution()
nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
print(solution.canJump(nums))
