class Solution:
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1

numbers = [1,2,3,6,6,25,75,100]
target = 10
solution = Solution()
print(solution.twoSum(numbers, target))