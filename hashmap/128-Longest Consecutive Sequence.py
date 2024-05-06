class Solution:
    def longestConsecutive(self, nums):
        nums = sorted(set(nums))
        length = len(nums)
        count_max = 0
        count = 1
        if nums:
            for index, num in enumerate(nums):
                if index < length - 1:
                    if nums[index + 1] - num == 1:
                        count += 1
                        if count > count_max:
                            count_max = count
                    else:
                        count = 1
        else:
            return 0
        return count_max

nums = [100,4,200,1,3,2]
solution = Solution()
print(solution.longestConsecutive(nums))