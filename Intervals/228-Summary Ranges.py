class Solution:
    def summaryRanges(self, nums):
        ans = []
        length = len(nums)
        for index, num in enumerate(nums):
            if ans:
                if num - nums[index - 1] != 1:
                    if ans[-1] != str(nums[index - 1]):
                        ans[-1] += "->" + str(nums[index - 1])
                    ans.append(str(num))
                elif index == length - 1:
                    ans[-1] += "->" + str(num)
            else:
                ans.append(str(num))

        return ans


nums = [0,2,3,4,6,8,9]
solution = Solution()
print(solution.summaryRanges(nums))