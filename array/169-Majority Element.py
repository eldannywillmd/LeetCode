class Solution:
    def majorityElement(self, nums):
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            if count[num] > len(nums) / 2:
                return num


solution = Solution()
nums = [2,2,1,1,1,2,2,3,3,3,3,3,3,3]
print(solution.majorityElement(nums))

