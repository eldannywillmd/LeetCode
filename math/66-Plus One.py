class Solution:
    def plusOne(self, digits):
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits = [1] + digits
            else:
                digits[i] += 1
                break
        return digits

digits = [1,0,9]

solution = Solution()
print(solution.plusOne(digits))