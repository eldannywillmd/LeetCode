class Solution:
    def minSubArrayLen(self, target, nums):
        ans = 0
        curr_sum = 0
        count = 0
        for index, num in enumerate(nums):
            curr_sum += num

            while curr_sum >= target:
                if ans != 0 and index - count + 1 < ans:
                    ans = index - count + 1
                elif ans == 0:
                    ans = index - count + 1
                curr_sum -= nums[count]
                count += 1

        return ans


target = 7
nums = [2,3,1,3,1,5,1,2,2,2]
solution = Solution()
print(solution.minSubArrayLen(target, nums))