class Solution:
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        dif = max(nums) - min(nums)
        cost_1 = dif * (len(nums) - 1) * cost1
        if len(nums) > 3:
            cost_2 = dif * (len(nums) - 1) * cost2 // 2
        else:
            cost_2 = cost_1

        return min(cost_1, cost_2)

nums = [4,1]
cost1 = 5
cost2 = 2
solution = Solution()
print(solution.minCostToEqualizeArray(nums, cost1, cost2))