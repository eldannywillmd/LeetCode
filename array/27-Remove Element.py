import random

class Solution:
    def removeElement(self, nums, val):
        print(f'nums before: {nums}\n{len(nums)}')

        length = len(nums)
        k = 0
        for i in range(length):
            if nums[i] == val:
                k += 1
                for j in range(i, len(nums)):
                    while j < length - k and nums[j + k] == val:
                        k += 1
                    if j < length - k:
                        nums[j] = nums[j + k]
                    if j == length - k:
                        break

        print(f'nums /after: {nums}\n{len(nums)}\n k: {k} \n value: {val}')

    def removeElement2(self, nums, val):
        print(f'nums before: {nums}\n{len(nums)}')

        k = 0
        indexs = []

        for index, num in enumerate(nums):
            if num == val:
                indexs.append(index)
                k += 1

        for index in reversed(indexs):
            del nums[index]

        print(f'nums /after: {nums}\n{len(nums)}\n k: {k} \n value: {val}')


def generate_nums():
    length = random.randint(0, 100)
    nums = []
    for i in range(length):
        nums.append(random.randint(0, 50))
    return nums

solution = Solution()
#
# for i in range(1000):
#     nums = generate_nums()
#     solution.removeElement2(nums, random.choice(nums))

nums = [0,1,2,2,3,0,4,2]
solution.removeElement2(nums, 2)