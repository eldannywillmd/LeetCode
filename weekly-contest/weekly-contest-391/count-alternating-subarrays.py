from collections import Counter


class Solution:
    def countAlternatingSubarrays(self, nums):
        l = 0
        r = 1
        sub = []
        count = 0
        while l < r:
            if r < len(nums) and nums[r-1] != nums[r]:
                sub.append(nums[l:r+1])
                count += 1
                r += 1
            else:
                l += 1
                if r - l > 1 and nums[l] != nums[l+1]:
                    sub.append(nums[l:r])
                    count += 1

        return count

nums = [0,1,0,1]
solution = Solution()
print(solution.countAlternatingSubarrays(nums))