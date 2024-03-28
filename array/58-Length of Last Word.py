class Solution:
    def lengthOfLastWord(self, s):
        i = len(s) - 1
        while s[i] == " ":
            i -= 1
        mark = i
        while s[i] != " " and i != -1:
            i -= 1

        return mark - i

solution = Solution()
s = "Hello Worlddd"
print(solution.lengthOfLastWord(s))