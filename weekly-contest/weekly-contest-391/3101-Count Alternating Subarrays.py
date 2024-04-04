class Solution:
    def soma(self, sub):
        soma = 0
        for i in range(1, len(sub) + 1):
            soma += i
        return soma

    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        sub = []
        subs = []
        sum = 0
        # alternating subarrays of nums
        for index, num in enumerate(nums):
            if index + 1 < len(nums) and nums[index + 1] != num:
                sub.append(num)
            else:
                sub.append(num)
                subs.append(sub)
                sub = []

        for sub in subs:
            sum += self.soma(sub)

        return sum