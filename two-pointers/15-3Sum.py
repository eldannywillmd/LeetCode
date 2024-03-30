class Solution:
    def threeSum(self, nums):
        ans = []
        answer = set()
        nums.sort()
        length = len(nums)
        for i in range(length):
            l = i + 1
            r = length - 1
            while l < r:
                if nums[l] + nums[r] == -nums[i]:
                    answer.add((nums[i], nums[l], nums[r]))
                    r -= 1
                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                else:
                    r -= 1
            if nums[i] >= 0:
                break
        for i in answer:
            ans.append(list(i))
        return ans

solution = Solution()
nums = [-4,-3,-2,-1,0,0,1,2,3,4]
print(solution.threeSum(nums))