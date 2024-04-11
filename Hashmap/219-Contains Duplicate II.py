class Solution:
    def containsNearbyDuplicate(self, nums, k):
        nums_d = {}
        for index, num in enumerate(nums):
            if num in nums_d.keys():
                if abs(index - nums_d[num]) <= k:
                    return True
            nums_d[num] = index
        return False

nums = [1,2,3,1,2,3]
k = 2
solution = Solution()
print(solution.containsNearbyDuplicate(nums, k))