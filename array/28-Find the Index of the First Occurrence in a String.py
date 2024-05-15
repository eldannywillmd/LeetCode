class Solution:
    def strStr(self, haystack, needle):
        length = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i + length] == needle: return i
        return -1

haystack = "leetcode"
needle = "leeto"

solution = Solution()
print(solution.strStr(haystack, needle))