class Solution:
    def isSubsequence(self, s, t):
        i = 0
        l = len(s)
        if s == "":
            return True
        for char in t:
            if char == s[i]:
                if i == l - 1:
                    return True
                i += 1
        return False


s = "axc"
t = "ahbgdc"
solution = Solution()
print(solution.isSubsequence(s, t))