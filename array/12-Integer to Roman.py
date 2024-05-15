import unittest

class Solution:
    def intToRoman(self, num):
        roman_dict = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        word = ''
        numbers = {}

        numbers[1000] = (num // 1000)
        numbers[100] = ((num % 1000) // 100)
        numbers[10] = ((num % 100) // 10)
        numbers[1] = (num % 10)

        for key in numbers.keys():
            if numbers[key] == 0:
                continue
            if numbers[key] * key in roman_dict:
                word += roman_dict[numbers[key] * key]
            elif numbers[key] * key == 4 * key or numbers[key] * key == 9 * key:
                word += roman_dict[key]
                word += roman_dict[numbers[key] * key + key]
            elif numbers[key] * key > 5 * key and numbers[key] not in roman_dict:
                word += roman_dict[5 * key]
                for n in range(numbers[key] - 5):
                    word += roman_dict[key]
            else:
                for n in range(numbers[key]):
                    word += roman_dict[key]
        return word

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_intToRoman(self):
        self.assertEqual(self.solution.intToRoman(12), 'XII')
        self.assertEqual(self.solution.intToRoman(1), 'I')
        self.assertEqual(self.solution.intToRoman(5), 'V')
        self.assertEqual(self.solution.intToRoman(10), 'X')
        self.assertEqual(self.solution.intToRoman(50), 'L')
        self.assertEqual(self.solution.intToRoman(100), 'C')
        self.assertEqual(self.solution.intToRoman(500), 'D')
        self.assertEqual(self.solution.intToRoman(1000), 'M')

if __name__ == '__main__':
    unittest.main()