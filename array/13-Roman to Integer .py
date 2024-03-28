class Solution:
    def romanToInt(self, s):
        num = 0
        block = 0
        roman_dict = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'IX': 9, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        for i in reversed(range(len(s))):
            unit = 0
            if block != 0:
                block -= 1
            if i - 2 >= 0 and block == 0:
                num3 = s[i - 2] + s[i - 1] + s[i]
                if num3 in roman_dict.keys():
                    unit = roman_dict[num3]
                    block = 3
                    num += unit

            if i - 1 >= 0 and block == 0:
                num2 = s[i - 1] + s[i]
                if num2 in roman_dict.keys():
                    unit = roman_dict[num2]
                    block = 2

                    num += unit

            if unit == 0 and block == 0:
                unit = roman_dict[s[i]]
                num += unit

        return num



solution = Solution()
s = "DCCC"
print(solution.romanToInt(s))