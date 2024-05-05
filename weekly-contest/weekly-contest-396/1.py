class Solution:
    def isValid(self, word):
        numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'}
        count_vowels = 0
        count_consonants = 0
        if len(word) < 3:
            return False
        for char in word:
            if char not in numbers and char not in vowels and char not in consonants:
                print("hey")
                return False
            if char in vowels:
                count_vowels = 1
            if char in consonants:
                count_consonants = 1
        if count_vowels == 0 or count_consonants == 0:
            return False
        return True

word = "OwP"
solution = Solution()
print(solution.isValid(word))