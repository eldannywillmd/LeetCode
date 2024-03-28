class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length = m
        while nums2:
            num2 = nums2.pop(-1)
            for index1, num1 in enumerate(nums1):
                if num2 < num1:
                    buffer = nums1[index1:(m + n - 1)]
                    nums1 = nums1[:index1] + [num2] + buffer
                    length += 1
                    break
                else:
                    if index1 == length:
                        nums1[index1] = num2
                        length += 1
                        break
                    continue

    def merge2(self, nums1, m, nums2, n) -> None:

        while nums2:
            num2 = nums2.pop(-1)
            if num2 >= nums1[m - 1]:
                nums1[m] = num2
                m += 1
            else:
                nums1[m] = nums1[m - 1]
                nums1[m - 1] = num2
                if m == 1:
                    m += 1
                    num2 = None
                elif num2 is not None:
                    self.merge(nums1, m - 1, [num2], 1)
                    m += 1

    def merge3(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while nums2:
            num2 = nums2.pop(-1)
            if num2 >= nums1[m - 1]:
                nums1[m] = num2
                m += 1
            else:
                nums1[m] = nums1[m - 1]
                nums1[m - 1] = num2
                if m == 1:
                    m += 1
                    num2 = None
                elif num2 is not None:
                    for i in range(m - 1, -1, -1):
                        if num2 >= nums1[i - 1]:
                            nums1[i] = num2
                            m += 1
                            break
                        else:
                            nums1[i] = nums1[i - 1]
                            nums1[i - 1] = num2
                            if i == 1:
                                m += 1
                                break

    def merge4(self, nums1, m, nums2, n) -> None:

        while nums2:
            num2 = nums2.pop(-1)
            if num2 >= nums1[m - 1]:
                nums1[m + n - 1] = num2
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
                self.merge3(nums1, m, [num2], 1)

            print(nums1)

solution = Solution()
nums1 = [7,0,0,0]
m = 1
nums2 = [4, 11, 11]
n = 3

solution.merge4(nums1, m, nums2, n)
