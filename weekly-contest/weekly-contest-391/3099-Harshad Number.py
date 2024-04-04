class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum = 0
        number = x
        while number >= 10:
            sum += number % 10
            number = number // 10
        sum += number

        if x % sum == 0:
            return sum
        else:
            return -1
