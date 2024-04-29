class Solution:
    def specialNumbers(self, word):
        count = {}
        ans = 0
        for char in word:
            if ord(char) not in count:
                count[ord(char)] = 1
                if ord(char) >= 65 and ord(char) <= 90:
                    if ord(char) + 32 in count.keys():
                        ans += 1
                        count[ord(char) + 32] = 0
            else:
                if ord(char) - 32 in count.keys() and count[ord(char)] == 0:
                    ans -= 1
                    count[ord(char)] = 1
        return ans

word = "AbBCab"
solution = Solution()
print(solution.specialNumbers(word))