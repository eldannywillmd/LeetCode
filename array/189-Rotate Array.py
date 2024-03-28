class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            swap = nums.pop(-1)
            nums.insert(0, swap)

        print(nums)
