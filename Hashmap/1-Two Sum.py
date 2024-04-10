class Solution:
    def twoSum(self, nums, target):
        # each input has exactly one solution
        map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map.keys():
                return [map[complement], i]
            map[nums[i]] = i

        return None

nums = [2,7,11,15]
target = 9

solution = Solution()
print(solution.twoSum(nums, target))