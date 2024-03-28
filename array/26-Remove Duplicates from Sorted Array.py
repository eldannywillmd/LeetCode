class Solution:
    def removeDuplicates(self, nums):
        k = 0
        is_repeat = {}
        indexs = []

        for index, num in enumerate(nums):
            if index < len(nums) - 1 and num == nums[index + 1] and num not in is_repeat.keys():
                is_repeat[num] = index
                k += 1
            if index < len(nums) - 1 and num == nums[index + 1] and num in is_repeat.keys():
                indexs.append(index)

        for index in reversed(indexs):
            del nums[index]

        print(f'nums: {nums}\n k: {k}')

    def removeDuplicates2(self, nums):
        k = 0

        for i in range(len(nums)):
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                k += 1
                n = i
                while n < len(nums) - 1 and nums[n] == nums[n + 1]:
                    del nums[n + 1]
                if i == len(nums) - 1:
                    break

        print(f'nums: {nums}\n k: {k}')

solution = Solution()
nums = [0,0,1,1,1,2,2,3,3,4,4,4,4,4,4]
solution.removeDuplicates(nums)
