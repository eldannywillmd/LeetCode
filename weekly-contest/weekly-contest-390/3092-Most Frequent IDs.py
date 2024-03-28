class Solution:
    def mostFrequentIDs(self, nums, freq):
        count_nums = {}
        ans = [] # list with the highest freq in each step
        high_number = []
        for i in range(len(freq)):
            if nums[i] not in count_nums:
                count_nums[nums[i]] = 0
            count_nums[nums[i]] += freq[i]
            # if negative, make it zero
            if count_nums[nums[i]] < 0:
                count_nums[nums[i]] = 0

            if len(ans) == 0 or count_nums[nums[i]] >= ans[-1]:
                ans.append(count_nums[nums[i]])
                high_number.append(nums[i])
            elif len(ans) != 0 and count_nums[nums[i]] < ans[-1] and high_number[-1] != nums[i]:
                ans.append(ans[-1])
                high_number.append(high_number[-1])
            else:
                key = max(count_nums, key=count_nums.get)
                ans.append(count_nums[key])
                high_number.append(key)


        return ans


nums = [2, 3, 2, 1]
freq = [3, 2, -3, 1]

solution = Solution()
print(solution.mostFrequentIDs(nums, freq))