class Solution:
    def removeDuplicates(self, nums):
        k = 0
        repeated = []

        for i, num in enumerate(nums):
            if i < len(nums) - 1 and num != nums[i + 1]:
                pass
            index = i + 1
            while index < len(nums) and num == nums[index] and num in repeated:
                nums.pop(index)
            if i < len(nums) - 1 and num == nums[i + 1]:
                repeated.append(num)
                k += 1


        print(f'nums: {nums}\nk: {k}')

solution = Solution()
nums = [-1, -1, -1, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4]
solution.removeDuplicates(nums)