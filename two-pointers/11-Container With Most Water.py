class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        area = 0
        while l <= r:
            if height[l] < height[r]:
                if area < height[l] * (r - l):
                    area = height[l] * (r - l)
                l += 1
            else:
                if area < height[r] * (r - l):
                    area = height[r] * (r - l)
                r -= 1
        return area



height = [1,1]
solution = Solution()
print(solution.maxArea(height))